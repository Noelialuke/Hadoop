# Paso 1: Instalacion de Haddoop"""

#Instalacion de Haddoop

!wget -q https://downloads.apache.org/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz

"""## Paso 2: Con el comando tar lo descomprimimos"""

!tar -xzf hadoop-3.3.0.tar.gz

!ls

# Copiamos el directorio de hadoop en usr/local
!cp -r hadoop-3.3.0/ /usr/local/

"""# Paso 3: Configurar el Hadoop JAVA HOME"""

!readlink -f /usr/bin/java | sed "s:bin/java::"

"""Establecemos mediante codigo python el valor de esta variable"""

import os 
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk-amd64/"
os.environ["PATH"]=os.environ["PATH"] + ":" + "/usr/local/hadoop-3.3.0/bin"

os.environ["JAVA_HOME"]
os.environ["PATH"]

"""# Paso 4: Ejecutando hadoop"""

#NOTA:Las siguientes sentencias unicamente sirven para probar comando basicos de HDFS no para gestionar una 
#infraestructura que en google colab no existe.

# Todos los comandos HDFS se invocan mediante el script bin/hdfs:

!ls /content/

# Es como un ls 
!hdfs dfs -ls /content/

!hdfs dfs -ls

#Crear un directorio
!hdfs dfs -mkdir prueba

#En vez de cp para copiar usamos put
!hdfs dfs -put user.txt

# borrar
!hdfs dfs -rm user.txt

"""Ejemplo"""

# Commented out IPython magic to ensure Python compatibility.
# ##Ejemplo de bash
# %%bash 
# echo "ejemplo de HDFS" > user.txt
# echo 'date' >> user.txt
# cat user.txt

##Para copiar como dijimos y lo mandamos al directorio pruebas
!hdfs dfs -put user.txt prueba/

!hdfs dfs -ls prueba/

"""# Ejercicio"""

#Ejercicio creado en otro colab
#1 cree un directorio files en HDFS
#2 listar el contenido de un directorio/
#3 cargar el archivo today.txt em HDFS
#date > hoy.txt
#whoami >> hoy.txt
#4 Mostrar el contenido del archivo hoy.txt
#5 copiar el archivo hoy.txt del origen al directorio fules.
#6 copiar el archivo jps.txt desde/hacia el sistema de archivos local a HDFS
#jps jps.txt
#7Mover el archivo jps.text
