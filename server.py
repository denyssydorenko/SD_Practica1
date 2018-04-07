# Eduard Fores Ferrer, Denys Sydorenko
# 7/04/2018 v1.0
# python server.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Importamos las librerias que necesitamos de Python. '''
import requests,os

''' Creamos la funcion para iniciar el Server en la carpeta pasada por parametro. '''
def iniServer(carpeta):
    os.chdir(carpeta)
    os.system("python -m SimpleHTTPServer")

''' Main del Server. '''
if __name__ == '__main__':

    ''' Creamos la carpeta Files dentro del directorio en el cual nos encontramos. '''
    os.system("mkdir -p Files")

    ''' Llamamos a la funcion iniServer() con el string Files (el nombre de la carpeta que hemos creado) de parametro. '''
    iniServer("Files")
