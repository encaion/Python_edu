import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

df = pd.read_csv("auto_mpg.csv")
df.head(2)

df.isna().sum()

df2 = df.dropna()
df2.head(2)

set(df2["Origin"])

origin = df2.pop("Origin")
df2.head(2) # Origin이 빠짐

origin_dum = pd.get_dummies(origin, prefix = "class")
origin_dum.columns = ["USA", "Europe", "Japan"]
origin_dum.head(2)

df3 = pd.concat([df2, origin_dum], axis = 1)
df3.head(2)

train = df3.sample(frac = 0.8, random_state = 0)
test  = df3.drop(train.index) # train 부분을 제외하고 입력
test.head()

train_stats = train.describe()
train_stats.pop("MPG")
train_stats = train_stats.transpose()
train_stats

train_y = train.pop("MPG")
test_y = test.pop("MPG")

def norm(x):
  return (x - train_stats["mean"]) / train_stats["std"]

normed_train_data = norm(train)
normed_test_data = norm(test)

model = keras.Sequential([layers.Dense(64, activation = "relu", 
                                       input_shape = [len(train.columns)]),
                            layers.Dense(64, activation = "relu"),
                            layers.Dense(1)])
model.compile(loss="mse",
              optimizer = tf.keras.optimizers.RMSprop(learning_rate = 0.001),
              metrics=["mae", "mse"])              
model.summary()

history = model.fit(normed_train_data, train_labels,
                    epochs=1000, validation_split = 0.2, verbose = 0)
                    
df_hist = pd.DataFrame(history.history)
df_hist["epoch"] = history.epoch
df_hist.tail()

import matplotlib.pyplot as plt

def plot_history(history):
  df_hist = pd.DataFrame(history.history)
  df_hist["epoch"] = history.epoch

  plt.figure(figsize=(8,12))

  plt.subplot(2,1,1)
  plt.xlabel("Epoch")
  plt.plot(df_hist["epoch"], df_hist["mae"],
           label = "Train Error")
  plt.plot(df_hist["epoch"], df_hist["val_mae"],
           label = "Val Error")
  plt.ylim([0,5])
  plt.legend()

  plt.subplot(2,1,2)
  plt.xlabel("Epoch")
  plt.plot(df_hist["epoch"], df_hist["mse"],
           label = "Train Error")
  plt.plot(df_hist["epoch"], df_hist["val_mse"],
           label = "Val Error")
  plt.ylim([0,20])
  plt.legend()
  plt.show()
  
plot_history(history)
