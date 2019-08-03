# 1.4 -> 2.0

> [Source]
> https://github.com/tensorflow/tensorflow/issues/26349

Type of breakage: Breakage with changing code.

APIs that are affected:

tf.train.GradientDescentOptimizer
tf.train.MomentumOptimizer
tf.train.RMSPropOptimizer
tf.train.AdamOptimizer
tf.train.AdadeltaOptimizer
tf.train.AdagradOptimizer
tf.train.FtrlOptimizer
Side Note: there are two extra tf.contrib-owned optimizers that will also have breaking changes:

tf.contrib.opt.NadamOptimizer
tf.contrib.opt.AdaMaxOptimizer
Description of change: The current endpoint tf.train.xxxOptimizer() is being deprecated in favor of tf.keras.optimizers.xxx(). Specifically:

tf.train.GradientDescentOptimizer(lr=???) -> tf.keras.optimizers.SGD(learning_rate=???)
tf.train.MomentumOptimizer(lr=???, momentum=???) -> tf.keras.optimizers.SGD(learning_rate=???, momentum=???)
tf.train.RMSPropOptimizer(lr=???) -> tf.keras.optimizers.RMSprop(learning_rate=???)
tf.train.AdamOptimizer(lr=???, beta1=???, beta2=???) -> tf.keras.optimizers.Adam(learning_rate=???, beta_1=???, beta_2=???)
tf.train.AdadeltaOptimizer(lr=???) -> tf.keras.optimizers.Adadelta(learning_rate=???)
tf.train.AdagradOptimizer(lr=???) -> tf.keras.optimizers.Adagrad(learning_rate=???)
tf.train.FtrlOptimizer(lr=???) -> tf.keras.Ftrl(learning_rate=???)
TensorFlow users of tf.train.xxxOptimizer() will be updated to tf.keras.optimizers.xxx(), and checkpoints from the old tf.train.xxxOptimizer() calls will no longer work.

Variable name change map: The tf.keras.optimizers.xxx weights are in different format than existing tf.train.xxxOptimizer. There isn't direct mapping for that.

Target time window: Undecided since the update requires non-trivial user side change.
