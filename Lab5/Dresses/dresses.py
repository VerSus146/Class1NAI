import os
from sklearn.metrics import confusion_matrix
from keras.models import load_model
import itertools
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from keras.preprocessing import image as keras_image


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt), horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('Correct label')
    plt.xlabel('Prediction')
    plt.show()


fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

if os.path.isfile('fashion-mnist_model.h5') != True:
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10)
    ])

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    test_image_one = test_images[0]
    np.delete(test_images, [0])
    train_label_one = train_labels[0]
    np.delete(test_labels, [0])

    history = model.fit(train_images, train_labels, epochs=10,
                        validation_data=(test_images, test_labels))

    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
    model.save('fashion-mnist_model.h5')
else:
    model = load_model('fashion-mnist_model.h5')
    test_image_one = test_images[0]
    np.delete(test_images, [0])
    np.delete(test_labels, [0])
plt.rcParams['figure.figsize'] = [10, 7]

# get first image to test
test_image = keras_image.img_to_array(test_image_one)

# convert to array
test_image = np.expand_dims(test_image, axis=0)

p_test = model.predict(test_image).argmax(axis=1)
print('Predicted image is ' + class_names[int(p_test)])
# cm = confusion_matrix(test_labels, p_test)
# plot_confusion_matrix(cm, list(range(10)), normalize=True)
