import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf 
from tensorflow import keras
keras=tf.keras
cf10=keras.datasets.cifar10

(train_images,train_labels),(test_images,test_labels)=cf10.load_data()

class_names=['airplane','automobile','bird',
                'cat','deer','dog','frog',
                'horse','ship','truck']

train_images=train_images/255.0

test_images=test_images/255.0

model=keras.Sequential([
    
    keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(32,32,3)),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Conv2D(64, (3,3), activation='relu'),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Flatten(),
    keras.layers.Dense(128,activation='relu'),
    keras.layers.Dropout(0.4),
    keras.layers.Dense(10,activation='softmax')
])

model.compile(optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])

model.fit(train_images,train_labels,epochs=20,batch_size=32)

test_loss,test_acc=model.evaluate(test_images,test_labels)
print(f'test accuracy :{test_acc*100:.2f}')

predictions=model.predict(test_images)

def plot_image(i, predictions_array, true_label, img):
    predictions_array, true_label, img = predictions_array, int(true_label[i][0]), img[i]
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
        100 * np.max(predictions_array),
        class_names[true_label]),
        color=color
    )





num_rows = 3
num_cols = 5
plt.figure(figsize=(2 * 2 * num_cols, 2 * num_rows))
for i in range(num_rows * num_cols):
    plt.subplot(num_rows, num_cols, i + 1)
    plot_image(i, predictions[i], test_labels, test_images)
plt.tight_layout()
plt.show()


