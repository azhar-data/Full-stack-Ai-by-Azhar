import tensorflow as tf 
ra=tf.random.normal([1000,50])
print(ra)
print()
print(tf.reduce_sum(ra))