#loading the saved model
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

model = load_model('cifar10_model.h5')
test_image1 = image.load_img('dog2.png')

test_image =image.img_to_array(test_image1)
test_image = np.expand_dims(test_image, axis =0)
result = model.predict(test_image)
print(result)
if result[0][0]==1:
    print("Aeroplane")
elif result[0][1]==1:
    print('Automobile')
elif result[0][2]==1:
    print('Bird')
elif result[0][3]==1:
    print('Cat')
elif result[0][4]==1:
    print('Deer')
elif result[0][5]==1:
    print('Dog')
elif result[0][6]==1:
    print('Frog')
elif result[0][7]==1:
    print('Horse')
elif result[0][8]==1:
    print('Ship')
elif result[0][9]==1:
    print('Truck')
else:
    print(result)
    print('Error')