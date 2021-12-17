from keras.models import load_model
from keras.preprocessing import image
import numpy as np

# Load the model
model = load_model('cifar10_model.h5')

# Load the images
bird = image.load_img('animals_images/bird.png')
dog1 = image.load_img('animals_images/dog.jpg')
dog2 = image.load_img('animals_images/dog2.png')
deer = image.load_img('animals_images/deer.png')

counter = 0
# Predict the given images
for image_item in [bird, dog1, dog2, deer]:

    # Get first image to test
    test_image = image.img_to_array(image_item)

    # Convert to array
    test_image = np.expand_dims(test_image, axis=0)

    # Predict what is this image
    result = model.predict(test_image)

    # Fetch highest possible value out of 10 types - most probable label
    result = np.argmax(result[0])

    animal_type = 'None'
    counter += 1

    if result == 0:
        animal_type = "Aeroplane"
    elif result == 1:
        animal_type = 'Automobile'
    elif result == 2:
        animal_type = 'Bird'
    elif result == 3:
        animal_type = 'Cat'
    elif result == 4:
        animal_type = 'Deer'
    elif result == 5:
        animal_type = 'Dog'
    elif result == 6:
        animal_type = 'Frog'
    elif result == 7:
        animal_type = 'Horse'
    elif result == 8:
        animal_type = 'Ship'
    elif result == 9:
        animal_type = 'Truck'
    else:
        animal_type = 'Error'

    print('Image: ' + str(counter) + ' is a ' + animal_type)
