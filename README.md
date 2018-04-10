### PASOS A SEGUIR PARA EL FUNCIONAMIENTO DEL PROGRAMA SECUENCIAL
```plain
- paso 1: Nos movemos al directorio donde se encuentra la práctica con todos los archivos.
- paso 2: Escribimos la comanda para iniciar el proceso del archivo secuencial y le pasamos el nombre del archivo por parámetro. (Comanda: python SD_p1_secuencial.py big.txt)
- paso 3: Observamos el HashMap y el tiempo de ejecución del programa.
```

### PASOS A SEGUIR PARA EL FUNCIONAMIENTO DEL PROGRAMA DINAMICO
```plain
- paso 1: Nos movemos al directorio donde se encuentra la práctica con todos los archivos.
- paso 2: Encendemos el server.py, registry.py y los host.py gracias al fichero de startup.sh. (Comanda: sh startup.sh)
- paso 3: En el mismo terminal en el cual hemos hecho el paso anterios endendemos el client.py con sus parametros correspondientes, primero un fichero.txt y después el número de mappers que queremos utilizar (el número de mappers no puede ser mayor de 5, ya que lo hemos programado así). (Comanda: python client.py big.txt 5)
- paso 4: Observamos en el mismo terminal el resultado de nuestra llamada en el paso 3. Un HashMap, el número total de palabras que hay en el fichero y el tiempo de ejecución de nuestro programa.
```
### DESCRIPCIÓN DE LA SOLUCIÓN
- Hemos creado un programa que contiene una clase Server y un Main. En la comanda para inicializar el client.py le pasamos por parámetro el archivo.txt y el número de Mappers que vayamos a utilizar. Acto seguido, los asignamos a dos variables.
- Primero, cogemos el archivo y lo partimos en tantos archivos como Mappers haya introducido el usuario. Cada fichero se renombra con un identificador único.
- El siguiente paso es coger las referencias del host del Registry donde se encuentran los Mappers y el Reducer que han sido inicializados previamente.
- Continuamos con la asignación de cada secuencia (secuencia limpia de caracteres innecesarios) a cada Mapper.
- Uno de los últimos pasos es llamar a la función count_words() que se encarga de llamar a la función CountingWords, que nos devuelve el número total de palabras que hay en la secuencia seleccionada, y a la función WordCount() que nos devuelve el HashMap de la secuencia pasada por parámetro.
- Para terminar, pasamos el número total de palabras de la secuencia y el HashMap a la función reducer() que se encarga de hacer el sumatorio de los diferentes números de palabras de cada secuencia y la concatenación de los diferentes HashMap.
- Finalmente, imprimimos el HashMap, el número total de palabras del archivo introducido por parámetro y el tiempo de ejecución de nuestro programa por pantalla.

### JUEGO DE PRUEBAS
**DATOS SECUENCIAL:**
*Tabla 1 - Archivos Originales*
| Archivo       | Tiempo de Ejecución |
| :-----------: | :----------------------: |
| pg10.txt      | 0.284196853638       |
| pg2000.txt | 0.146966934204        |
| big.txt         | 0.386319875717       |
