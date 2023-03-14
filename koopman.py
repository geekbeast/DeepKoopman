import tensorflow as tf

print("TensorFlow version: ", tf.__version__)

from tensorflow.keras.layers import Dense
from tensorflow.keras import Model

class KoopmanNetwork(Model):
    def __init__(self):
        super(MyModel, self).__init__()
        