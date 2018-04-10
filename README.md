### PASOS A SEGUIR PARA EL FUNCIONAMIENTO DEL PROGRAMA SECUENCIAL
```plain
-paso 1: Nos movemos al directorio donde se encuentra la práctica con todos los archivos.
-paso 2: Escribimos la comanda para iniciar el proceso del archivo secuencial y le pasamos el nombre del archivo por parámetro. (Comanda: python SD_p1_secuencial.py big.txt)
-paso 3: Observamos el HashMap y el tiempo de ejecución del programa.
```

### PASOS A SEGUIR PARA EL FUNCIONAMIENTO DEL PROGRAMA DINAMICO
```plain
-paso 1: Nos movemos al directorio donde se encuentra la práctica con todos los archivos.
-paso 2: Encendemos el server.py, registry.py y los host.py gracias al fichero de startup.sh. (Comanda: sh startup.sh)
-paso 3: En el mismo terminal en el cual hemos hecho el paso anterios endendemos el client.py con sus parametros correspondientes, primero un fichero.txt y después el número de mappers que queremos utilizar (el número de mappers no puede ser mayor de 5, ya que lo hemos programado así). (Comanda: python client.py big.txt 5)
-paso 4: Observamos en el mismo terminal el resultado de nuestra llamada en el paso 3. Un HashMap, el número total de palabras que hay en el fichero y el tiempo de ejecución de nuestro programa.
```