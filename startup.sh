# Eduard Fores Ferrer, Denys Sydorenko
# 7/04/2018 v1.0
# sh startup.sh

#!/bin/bash

# Fichero que utilizamos para iniciar el server.py, registry.py, host-x.py y reducer.py.

gnome-terminal -e "python server.py"
gnome-terminal -e "python registry.py"
gnome-terminal -e "python host-0.py"
gnome-terminal -e "python host-1.py"
gnome-terminal -e "python host-2.py"
gnome-terminal -e "python host-3.py"
gnome-terminal -e "python host-4.py"
gnome-terminal -e "python reducer.py"
