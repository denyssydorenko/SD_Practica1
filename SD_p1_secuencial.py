# Eduard Fores Ferrer, Denys Sydorenko
# 13/03/2018 v1.0
# python SD_practica1.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Importamos la libreria re de Python. '''
import re

''' Abrimos el fichero en modo de lectura y lo guardamos en la variable sequence. '''
f = open("big.txt", "r")
sequence = f.read()
f.close()

''' Hacemos una llamda a la funcion sub de la libreria re para utilizarla y borrar todos los simbolos que son "basura" en el fichero. '''
sequence1 = re.sub('[^ a-zA-Z0-9]', ' ', sequence)

''' Creamos la funcion CountingWords para que nos retorne el numero total de palabras que hay en la secuencia. '''
def CountingWords(sequence):
	wordcount = len(sequence1.split())
	return wordcount

''' Creamos la funcion WordCount para hacer un HashMap de la secuencia que le pasamos por parametro. '''
def WordCount(sequence):
	map_list = {}
	for word in sequence.split():
	    word = int(word) if word.isdigit() else word
	    if word in map_list:
	        map_list[word] += 1
	    else:
	        map_list[word] = 1

	return map_list

''' Creamos una lista vacia para guardar el resultado de la funcion WordCount. '''
map_list = {}

''' Llamamos a la funcion que nos hara el HashMap. '''
map_list = WordCount(sequence1)

''' Llamamos a la funcion que nos retorna el numero total de palabras que hay en la secuencia. '''
wordcount =CountingWords(sequence1)

''' Imprimimos los resultados para comprobar que lo hayamos hecho bien. '''
print map_list
print "Count words in a sequence: ", wordcount
