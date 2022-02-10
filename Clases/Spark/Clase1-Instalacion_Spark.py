######################  CUADERNO EJECUTADO EN COLAB  ##########################
"https://colab.research.google.com/drive/13hUs4LUg-unk3GgkBRIiNI2qzYjO_X4P?usp=sharing"

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


#--------------------------- PASO COMUN PARA USAR SPARK ------------------------------------

#Descargar ngrok
!wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip


!unzip ngrok-stable-linux-amd64.zip
!ls


get_ipython().system_raw('./ngrok http 4050 &')


#Se crea un puente entre ngroc desde el localhost (4050) y colab
!curl -s http://localhost:4040/api/tunnels | python3 -c "import sys, json; print(json.load(sys.stdin)['tunnels'][0]['public_url'])"


#Calcular el metodo de MonteCarlo
import random
num_samples=100000
def inside(p):
  x,y = random.random(),random.random()
  return x*x + y*y <1

count = sc.parallelize(range(0,num_samples)).filter(inside).count()
count

pi= 4 * count / num_samples
print(pi)

sc.stop()
