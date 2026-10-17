import tensorflow as tf
from keras.utils import to_categorical
keras=tf.keras
clf100=keras.datasets.cifar100
from keras import Sequential
from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
from keras.metrics import Precision,Recall
import numpy as np 
import matplotlib.pyplot as plt

(train_images,train_labels),(test_images,test_labels)=clf100.load_data()

def  show_images(train_images,
                 class_names,
                 train_labels,
                 nb_samples=12,nb_row=4):
    
    plt.figure(figsize=(12,12))
    for i in range(nb_samples):
        plt.subplot(nb_row,nb_row,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i],cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labels[i][0]])
    plt.show()

class_names = [
    'apple', 'aquarium_fish', 'baby', 'bear', 'beaver', 'bed', 'bee', 'beetle',
    'bicycle', 'bottle', 'bowl', 'boy', 'bridge', 'bus', 'butterfly', 'camel',
    'can', 'castle', 'caterpillar', 'cattle', 'chair', 'chimpanzee', 'clock',
    'cloud', 'cockroach', 'couch', 'crab', 'crocodile', 'cup', 'dinosaur',
    'dolphin', 'elephant', 'flatfish', 'forest', 'fox', 'girl', 'hamster',
    'house', 'kangaroo', 'keyboard', 'lamp', 'lawn_mower', 'leopard', 'lion',
    'lizard', 'lobster', 'man', 'maple_tree', 'motorcycle', 'mountain', 'mouse',
    'mushroom', 'oak_tree', 'orange', 'orchid', 'otter', 'palm_tree', 'pear',
    'pickup_truck', 'pine_tree', 'plain', 'plate', 'poppy', 'porcupine',
    'possum', 'rabbit', 'raccoon', 'ray', 'road', 'rocket', 'rose', 'sea',
    'seal', 'shark', 'shrew', 'skunk', 'skyscraper', 'snail', 'snake', 'spider',
    'squirrel', 'streetcar', 'sunflower', 'sweet_pepper', 'table', 'tank',
    'telephone', 'television', 'tiger', 'tractor', 'train', 'trout', 'tulip',
    'turtle', 'wardrobe', 'whale', 'willow_tree', 'wolf', 'woman', 'worm'
]

show_images(train_images,class_names,train_labels)


max_pixel_value=255
train_images=train_images/max_pixel_value
test_images=test_images/max_pixel_value


train_labels=to_categorical(train_labels,len(class_names))
test_labels=to_categorical(test_labels,len(class_names))

INPUT_SHAPE=(32,32,3)
FILTER1_SIZE=32
FILTER2_SIZE=64
FLITER_SHAPE=(3,3)
POOL_SHAPE=(2,2)
FULLY_CONNECT_NUM=128
NUM_CLASSES=len(class_names)


model=Sequential()
model.add(Conv2D(FILTER1_SIZE,FLITER_SHAPE,activation='relu',input_shape=INPUT_SHAPE))
model.add(MaxPooling2D(POOL_SHAPE))
model.add(Conv2D(FILTER2_SIZE,FLITER_SHAPE,activation='relu'))
model.add(Flatten())
model.add(Dense(FULLY_CONNECT_NUM,activation='relu'))
model.add(Dense(NUM_CLASSES,activation='softmax'))


METRICS=metrics=['accuracy',
                 Precision(name='precision'),
                 Recall(name='recall')]


model.compile(optimizer='adam',
               loss='categorical_crossentropy',
               metrics=METRICS)



training_history=model.fit(train_images,train_labels,
                       epochs=1,batch_size=30,
                       validation_data=(test_images,test_labels))

print('model summary:',model.summary())


import matplotlib.pyplot as plt

def show_performance_curve(training_result,metric,metric_label):
    train_pref=training_result.history[str(metric)]
    validation_pref=training_result.history['val_'+str(metric)]
    intersection_idx=np.argwhere(np.isclose(train_pref,validation_pref,atol=1e-2)).flatten()

    plt.plot(train_pref,label=metric_label)
    plt.plot(validation_pref,label='val_'+str(metric))
    plt.axvline(x=intersection_idx,color='r',linestyle='----',label='Intersection')
    plt.annotate(f'Optimal Value: {intersection_value:.4f}',
             xy=(intersection_idx,intersection_value),
             xycoords='data',
             fontsize=10,
             color='green')

    plt.xlabel('Epoch')
    plt.ylabel(metric_label)
    plt.legend(loc='lower right')



show_performance_curve(training_history,'accuracy','accuracy')
show_performance_curve(training_history,'recall','recall')
show_performance_curve(training_history, 'precision','Precision')
