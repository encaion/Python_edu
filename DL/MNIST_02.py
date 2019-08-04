import numpy as np
import tensorflow as tf
import cv2
import os

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape = (28, 28)),
  tf.keras.layers.Dense(128, activation = "relu"),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation = "softmax")
])
model.compile(optimizer = "adam",
              loss = "sparse_categorical_crossentropy",
              metrics = ["accuracy"])
              
model.fit(x_train, y_train, epochs = 5, verbose = 0)
model.evaluate(x_test, y_test)

dir_path = "handwritten_nums/"
listt = os.listdir(dir_path)

img_set = [[]]
for n in range(len(listt)):
    img_sub = cv2.imread(dir_path + listt[n], cv2.IMREAD_GRAYSCALE)
    img_sub = (255 - img_sub)/255.0
    img_set[0].insert(n, img_sub)

x_test_my = img_set
y_test_my = [int(path[5:6]) for path in listt]

model.evaluate(x_test_my, y_test_my)
