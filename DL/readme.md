# 1.4 -> 2.0

> [Source]
> https://github.com/tensorflow/tensorflow/issues/26349

Type of breakage: Breakage with changing code.

------------------
APIs that are affected: <br>

tf.train.GradientDescentOptimizer <br>
tf.train.MomentumOptimizer <br>
tf.train.RMSPropOptimizer <br>
tf.train.AdamOptimizer <br>
tf.train.AdadeltaOptimizer <br>
tf.train.AdagradOptimizer <br>
tf.train.FtrlOptimizer <br>
----------------------

Side Note: there are two extra tf.contrib-owned optimizers that will also have breaking changes: <br>

tf.contrib.opt.NadamOptimizer <br>
tf.contrib.opt.AdaMaxOptimizer <br>
Description of change: The current endpoint tf.train.xxxOptimizer() is being deprecated in favor of tf.keras.optimizers.xxx(). Specifically: <br>

tf.train.GradientDescentOptimizer(lr=???) -> tf.keras.optimizers.SGD(learning_rate=???) <br>
tf.train.MomentumOptimizer(lr=???, momentum=???) -> tf.keras.optimizers.SGD(learning_rate=???, momentum=???) <br>
tf.train.RMSPropOptimizer(lr=???) -> tf.keras.optimizers.RMSprop(learning_rate=???) <br>
tf.train.AdamOptimizer(lr=???, beta1=???, beta2=???) -> tf.keras.optimizers.Adam(learning_rate=???, beta_1=???, beta_2=???) <br>
tf.train.AdadeltaOptimizer(lr=???) -> tf.keras.optimizers.Adadelta(learning_rate=???) <br>
tf.train.AdagradOptimizer(lr=???) -> tf.keras.optimizers.Adagrad(learning_rate=???) <br>
tf.train.FtrlOptimizer(lr=???) -> tf.keras.Ftrl(learning_rate=???) <br>
<br>
<br>
-------------------
TensorFlow users of tf.train.xxxOptimizer() will be updated to tf.keras.optimizers.xxx(), and checkpoints from the old tf.train.xxxOptimizer() calls will no longer work.

Variable name change map: The tf.keras.optimizers.xxx weights are in different format than existing tf.train.xxxOptimizer. There isn't direct mapping for that. <br>
 <br>
Target time window: Undecided since the update requires non-trivial user side change.
