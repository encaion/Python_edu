import tensorflow as tf

# summation
a = tf.constant([1234])
b = tf.constant([5000])

print(a + b)
print(tf.add(a, b))

def f(x): 
    return tf.add(x, 1.)

scalar = tf.constant(1.0)
vector1 = tf.constant([1.0])
vector2 = tf.constant([1.0, 1.0])
matrix1 = tf.constant([[3.0]])
matrix2 = tf.constant([[3.0], [4.0]])
matrix3 = tf.constant([[3.0, 1.0], [4.0, -2.0]])

print(f(scalar))
print(f(vector1))
print(f(vector2))
print(f(matrix1))
print(f(matrix2))
print(f(matrix3))

def f_var(x, d):
    return tf.add(x, d)

# multiplication
a = tf.constant([2])
b = tf.constant([3])
c = tf.constant([4])

print(a + b * c)
print((a + b) * c)

print(tf.add(a, tf.multiply(b, c)))
print(tf.multiply(tf.add(a, b), c))
