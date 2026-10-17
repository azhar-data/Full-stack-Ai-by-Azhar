import numpy as np 
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
keras=tf.keras
minst=keras.datasets.fashion_mnist

(train_images,train_labels),(test_images,test_labels)=minst.load_data()

class_names=['T-shirt/top','Trouser',
             'Pullover','Dress','Coat','Sandal',
             'Shirt','Sneaker','Bag','Ankle boot']

train_images=train_images/255.0
test_images=test_images/255.0

model=keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128,activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(10,activation='softmax')
    ])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy']
              )

#train model
model.fit(train_images,train_labels,epochs=5,batch_size=32)

#Evaluate model
test_loss,test_acc=model.evaluate(test_images,test_labels)
print(f'test Accuracy:{test_acc*100:.2f}%')

predictions=model.predict(test_images)

def plot_image(i, predictions_array, true_label, img):
    predictions_array, true_label, img = predictions_array, true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% (True: {})".format(
        class_names[predicted_label],
        100*np.max(predictions_array),
        class_names[true_label]),
        color=color
    )

num_rows = 3
num_cols = 5
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_rows*num_cols):
    plt.subplot(num_rows, num_cols, i+1)
    plot_image(i, predictions[i], test_labels, test_images)
plt.tight_layout()
plt.show()

