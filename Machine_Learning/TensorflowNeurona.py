import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
import tensorflow as tf

# importamos librerías adicionales
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd

# Neurona con TensorFlow
# Defino las entradas
entradas = tf.placeholder("float", name='Entradas')
datos = np.array([[0, 0]
                 ,[1, 0]
                 ,[0, 1]
                 ,[1, 1]])

# Defino las salidas
uno = lambda: tf.constant(1.0)
cero = lambda: tf.constant(0.0)

with tf.name_scope('Pesos'):
    # Definiendo pesos y sesgo
    pesos = tf.placeholder("float", name='Pesos')
    sesgo = tf.placeholder("float", name='Sesgo')

with tf.name_scope('Activacion'):
    # Función de activación
    activacion = tf.reduce_sum(tf.add(tf.matmul(entradas, pesos), sesgo))

with tf.name_scope('Neurona'):
    # Defino la neurona
    def neurona():
        return tf.case([(tf.less(activacion, 0.0), cero)], default=uno)
    
    # Salida
    a = neurona()

# path de logs
logs_path = '/tmp/tensorflow_logs/neurona'
# Lanzar la Sesion
with tf.Session() as sess:
    # para armar el grafo
    summary_writer = tf.train.SummaryWriter(logs_path, 
                                             graph=sess.graph)
    # para armar tabla de verdad
    x_1 = []
    x_2 = []
    out = []
    act = []
    for i in range(len(datos)):
        t = datos[i].reshape(1, 2)
        salida, activ = sess.run([a, activacion], feed_dict={entradas: t,
                                        pesos:np.array([[1.],[1.]]),
                                        sesgo: -1.5})
        # armar tabla de verdad en DataFrame
        x_1.append(t[0][0])
        x_2.append(t[0][1])
        out.append(salida)
        act.append(activ)
    tabla_info = np.array([x_1, x_2, act, out]).transpose()
    tabla = pd.DataFrame(tabla_info, 
                         columns=['x1', 'x2', 'f(x)', 'x1 AND x2'])
tabla