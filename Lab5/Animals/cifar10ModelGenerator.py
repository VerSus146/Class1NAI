import tensorflow as tf

from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

(train_images, train_labels),   (test_images, test_labels) = datasets.cifar10.load_data()

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i])
    # The CIFAR labels happen to be arrays,
    # which is why you need the extra index
    plt.xlabel(class_names[train_labels[i][0]])
plt.show()

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10))

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=10,
                    validation_data=(test_images, test_labels))

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
model.save('cifar10_model.h5')

model.summary()

print(test_loss, test_acc)


# import numpy
# from keras.models import Sequential
# from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D
# from keras.constraints import maxnorm
# from keras.optimizers import SGD
# from keras.utils import np_utils
# from keras import backend as K
# from pandas.tests.tools.test_to_datetime import epochs
#
# K.set_image_dim_ordering('tf')
# from keras.datasets import cifar10
# # let's load data
# (X_train, y_train), (X_test, y_test) = cifar10.load_data()
#
# #normalizing inputs from 0-255 to 0.0-1.0
# X_train = X_train.astype('float32')
# X_test = X_test.astype('float32')
# X_train = X_train / 255.0
# X_test = X_test / 255.0
#
# # one hot encode outputs
# y_train = np_utils.to_categorical(y_train)
# y_test = np_utils.to_categorical(y_test)
# num_classes = y_test.shape[1]
#
# # Create the model
# model = Sequential()
#
# model.add(Conv2D(32, (3, 3), input_shape=(32,32,3), activation='relu', padding='same'))
# model.add(Dropout(0.2))
# model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
# model.add(Dropout(0.2))
# model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
# model.add(Dropout(0.2))
# model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Flatten()) model.add(Dropout(0.2))
# model.add(Dense(1024, activation='relu', kernel_constraint=maxnorm(3)))
# model.add(Dropout(0.2))
# model.add(Dense(512, activation='relu', kernel_constraint=maxnorm(3)))
# model.add(Dropout(0.2))
# model.add(Dense(num_classes, activation='softmax'))
#
# # Compile model
# lrate = 0.01
# decay = lrate/epochs
# sgd = SGD(lr=lrate, momentum=0.9, decay=decay, nesterov=False)
# model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
#
# model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100, batch_size=32)
# # Final evaluation of the model
# scores = model.evaluate(X_test, y_test, verbose=0)
# print("Accuracy: %.2f%%" % (scores[1]*100))
#
# from keras.models import load_model
# model.save('project_model.h5')
#
#
# #loading the saved model
# from keras.models import load_model
# model = load_model('project_model.h5')
# import numpy as np
# from keras.preprocessing import image
# # Give the link of the image here to test
# test_image1 =image.load_img('/home/ai34/Downloads/c1.jpeg',target_size =(32,32))
#
# test_image =image.img_to_array(test_image1)
# test_image =np.expand_dims(test_image, axis =0)
# result = model.predict(test_image)
# print(result)
# if result[0][0]==1:
#     print("Aeroplane")
# elif result[0][1]==1:
#     print('Automobile')
# elif result[0][2]==1:
#     print('Bird')
# elif result[0][3]==1:
#     print('Cat')
# elif result[0][4]==1:
#     print('Deer')
# elif result[0][5]==1:
#     print('Dog')
# elif result[0][6]==1:
#     print('Frog')
# elif result[0][7]==1:
#     print('Horse')
# elif result[0][8]==1:
#     print('Ship')
# elif result[0][9]==1:
#     print('Truck')
# else:
#     print('Error')