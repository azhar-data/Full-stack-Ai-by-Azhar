import tensorflow as tf
keras=tf.keras
mnist=keras.datasets.fashion_mnist

(X_train,y_train),(X_test,y_test)=mnist.load_data()
X_train,X_test=X_train/255.0,X_test/255.0

model=tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10,activation='softmax'),
    
])


print('model optimizer :',model.compile(optimizer='adam',
                                         loss='sparse_categorical_crossentropy',
                                         metrics=['accuracy']
                                         ))

print('Fit of the modle',model.fit(X_train,y_train,epochs=9,batch_size=20))

preduction=model.predict(X_test)
print(preduction[0])
print(model.evaluate(X_test,y_test))

model.summary()

