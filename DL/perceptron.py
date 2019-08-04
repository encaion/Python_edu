import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

## [single perceptron]
# with NumPy
import numpy as np
W = np.array([2, 3, 4])
X = np.array([1, 2, 3])
np.dot(W, X)

W@X.reshape((3, 1))

# with TensorFlow
W = tf.constant([2, 3, 4], shape = [1, 3])
X = tf.constant([1, 2, 3], shape = [3, 1])
print(W)
print(X)
print(tf.matmul(W, X))

## [multi perceptron]
# with NumPy
W = np.random.rand(2,4)
X = np.random.rand(4,1)
b = np.random.rand(2,1)

print(X)
print(W)
print(b)

W@X + b

# with TensorFlow
W = tf.constant(np.random.rand(8), shape = (2, 4))
X = tf.constant(np.random.rand(4), shape = (4, 1))
b = tf.constant(np.random.rand(2), shape = (2, 1))

print(X)
print(W)
print(b)

print(tf.add(tf.matmul(W, X), b))
