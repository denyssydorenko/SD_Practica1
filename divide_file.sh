# Eduard Fores Ferrer, Denys Sydorenko
# 7/04/2018 v1.0
# sh divide_file.sh

#!/bin/bash

# Fichero que utilizamos para particionar el fichero original en tantas partes como mappers ha elegido el usuario.

nl=$(wc -l $1 | awk {' print $1 '})
aux=$(( $nl%$2 ))
nl=$(( $nl+$(( $2-$aux ))))
partes=$(( $nl/$2 ))
IFS=$"."
name=$(echo $1 | awk {' print $1 "-"'})
IFS=$"\n"
split -l $partes $1 -d $name
