######################  CUADERNO EJECUTADO EN COLAB  

#instalar spark Hadoop

!wget -q http://apache.osuosl.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop2.7.tgz


#Descomprimir archivo

!tar xf spark-3.2.1-bin-hadoop2.7.tgz


#Instalamos librerias

!pip install -q findspark
!pip install -q pyspark


#Buscar la maquina Java

!readlink -f /usr/bin/java | sed "s:bin/java::"


#Definimos las variables de entorno

import os
os.environ["JAVA_HOME"]="/usr/lib/jvm/java-11-openjdk-amd64"
os.environ["SPARK_HOME"]="/content/spark-3.2.1-bin-hadoop2.7.tgz"


#Comprobamos que la variable de entorno se encuentra en la direccion en la que hemos indicado arriba

os.environ["JAVA_HOME"]


# Iniciamos Spark para iniciar la sesion

import findspark
findspark.init()
#Esta sesion siempre hay que pararlo al finalizar



#Creamos el contexto Spark

import pyspark
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark import SparkContext, SparkConf



#CONFIGURACION
#Abrir puerto

conf = SparkConf()
conf.set("spark.ui.port", "4050")
conf.set("spark.appName", "Pi")
# create the context
sc = pyspark.SparkContext(conf=conf)
spark = SparkSession.builder.getOrCreate()
sc


#Descargar ngrok

!wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip



!unzip ngrok-stable-linux-amd64.zip
!ls



get_ipython().system_raw('./ngrok http 4050 &')



#Se crea un puente entre ngroc desde el localhost (4050) y colab

!curl -s http://localhost:4040/api/tunnels | python3 -c "import sys, json; print(json.load(sys.stdin)['tunnels'][0]['public_url'])"



