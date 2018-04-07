# Eduard Fores Ferrer, Denys Sydorenko
# 7/04/2018 v1.0
# python host-4.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Importamos las librerias que necesitamos de PyActor. '''
from pyactor.context import set_context, create_host, serve_forever

''' Configuramos el mapper con la ip seleccionada y su puerto unico. '''
if __name__ == "__main__":

    ''' Inicializamos variables. '''
    set_context()

    ''' Creamos un host en la maquina con el puerto correspondiente. '''
    host = create_host('http://127.0.0.1:1280/')

    ''' Cogemos la ip del registry para poder registar el mapper. '''
    registry=host.lookup_url('http://127.0.0.1:6000/regis','Registry','registry')

    ''' Guardamos el nombre del mapper en la ip del registry para que en el client.py podamos coger todo lo que tiene el registy y asi conseguir todas las ips de los mappers. '''
    registry.bind('host3',host)

    print 'host listening at port 1280'

    serve_forever()
