# Eduard Fores Ferrer, Denys Sydorenko
# 7/04/2018 v1.0
# python client.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Importamos las librerias que necesitamos de Python. '''
import re
import os
import sys
import requests
import time

''' Importamos las librerias que necesitamos de PyActor. '''
from pyactor.context import set_context, create_host, Host, sleep, shutdown
from pyactor.exceptions import TimeoutError

''' Creamos la clase Server que utilizaremos a continuacion. '''
class Server(object):
    _ask = ['wordCount', 'countingWords', 'totalWords', 'finalMap', 'totalTime']
    _tell = ['reducer', 'count_words', 'startTime']
    _ref= ['count_words', 'reducer']

    memoria=[]
    map_final={}
    wordcount=0
    count=0
    start=0
    finish=0

    ''' Funcion que envia el Map de cada trozo de fichero junto con el numero de palabras que tiene. '''
    def count_words(self, f, i, reducer):
        sequence = requests.get("http://localhost:8000/"+f).text
        sequence1 = re.sub('[^ a-zA-Z0-9]', ' ', sequence)
        map_list = {}
        map_list = self.wordCount(sequence1)
        wc = self.countingWords(sequence1)
        reducer.reducer(i, map_list, wc)

    ''' Funcion que devuelve el numero total de palabras de una secuencia. '''
    def countingWords(self, sequence):
        wordcount = len(sequence.split())
        return wordcount

    ''' Funcion que devuelve el numero total de palabras del fichero original. '''
    def totalWords(self):
        return self.wordcount

    ''' Funcion que devuelve el HashMap final. '''
    def finalMap(self):
        return self.map_final

    ''' Funcion que inicia el tiempo. '''
    def startTime(self):
        self.start=time.time()

    ''' Funcion que nos devuelve el tiempo total de ejecucion. '''
    def totalTime(self):
        return (self.finish-self.start)

    ''' Funcion que devuelve el Map del trozo de secuencia que se le pasa por parametro. '''
    def wordCount(self, sequence):
        map_list={}
        for word in sequence.split():
            word=word.encode('utf-8')
            if word not in map_list:
                map_list[word] = 1
            else:
                map_list[word] += 1
        return map_list

    ''' Funcion que reduce todos los diccionarios a uno. La union de los Maps no se hara hasta que no haya acabado todos los mappers. '''
    def reducer(self, i, map_l, wc):
        self.count=self.count+1
        self.memoria.append(map_l)
        self.wordcount=self.wordcount+wc
        if self.count>=i:
            for m in self.memoria:
                if len(self.map_final)==0:
                    self.map_final=m
                else:
                    for k in m.keys():
                        if self.map_final.has_key(k):
                            self.map_final[k]=self.map_final.get(k)+m.get(k)
                        else:
                            self.map_final[k]=m.get(k)
            self.finish=time.time()

''' Main del programa. '''
if __name__ == "__main__":

    ''' Asignamos los parametros introducidos con el comando a dos variables. '''
    fil=sys.argv[1]
    n=int(sys.argv[2])

    ''' Si el segundo parametro introducido es superior a 5, entonces se muestra el mensaje de error. '''
    if n > 5:
        print "\nNo pueden haber mas de 5 mappers.\n"
        sys.exit(0)

    ''' Si el segundo parametro introducido es inferior a 1, entonces se muestra el mensaje de error. '''
    if n < 1:
        print "\nNo pueden haber menos de 1 mappers.\n"
        sys.exit(0)

    ''' Comprobamos que el fichero introducido por parametro exista, en caso contrario se muestra el mensaje de error. '''
    if os.path.isfile(fil):

        tabla=["00","01","02","03","04"]

        ''' Particionamos nuestro fichero original en la cantidad de mappers que haya seleccionado el usuario. '''
        os.system("cp -p ./divide_file.sh ./Files")
        os.system("cp -p ./"+fil+" ./Files")
        os.chdir("Files")
        os.system("./divide_file.sh"+" "+fil+" "+str(n))

        ''' Creamos el host. '''
        set_context()
        host = create_host('http://127.0.0.1:1679')

        ''' Cogemos la referencia del registry donde se encuentran los mappers. '''
        registry = host.lookup_url('http://127.0.0.1:6000/regis', 'Registry','registry')
        port=1277

        ''' Cogemos la referencia del reducer que se le pasara a cada uno de los mappers, para que estos envien sus diccionarios al reducer mas adelante. '''
        reducer=registry.lookup('reducer')
        ref_reducer = reducer.spawn('reducer', 'client/Server')

        ''' Creamos la variable fil1 que contiene el nombre del fichero que pasamos por parametro menos los ultimos 4 caracteres (.txt). '''
        fil1 = fil[:-4]
        sequence = ''
        sequence1 = ''
        mapper = []

        ''' Cogemos todos los mappers necesarios y ejecutamos la funcion count_words(), a la cual le pasamos el texto que tiene que trabajar, la referencia del reducer y el numero total de mappers que ha indicado el usuario. '''
        for i in range(0,n):
            remote_host=registry.lookup('host'+str(i))
            if remote_host is not None:
                mapper.append(remote_host.spawn('host'+str(i), 'client/Server'))
            port=port+1

        ref_reducer.startTime()

        for j in range(0,n):
            mapper[j].count_words(fil1+"-"+tabla[j], n, ref_reducer)

        sleep(20)
        ''' Imprimos el HashMap final, el numero total de palabras del fichero y el tiempo de ejecucuion.'''
        print "\nMapFinal: ", ref_reducer.finalMap()
        print "\nWordCount: ", ref_reducer.totalWords() 
        print ("\nTime in execution: --- %s seconds --- " % ref_reducer.totalTime())

        sleep(20)
        shutdown()

    else:
        print "\nEl nombre del fichero introducido no existe.\n"
    sys.exit(0)
