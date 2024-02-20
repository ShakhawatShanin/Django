from django.shortcuts import render
from .models import Photo

from PIL import Image
import numpy as np
import cv2
import tensorflow as tf


# Create your views here.
def index(request):
    if request.method == 'POST':
        new_photo = Photo(
            file = request.FILES['img']
        )
        new_photo.save()
        img = Image.open(request.FILES['img'])
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        dimensions = (299, 299)

        # Interpolation - a method of constructing new data points within the range
        # of a discrete set of known data points.
        resized_image = cv2.resize(img_array, dimensions, interpolation=cv2.INTER_AREA)
        ready_image = np.expand_dims(resized_image, axis=0)
        ready_image = tf.keras.applications.inception_resnet_v2.preprocess_input(ready_image)

        model = tf.keras.applications.InceptionResNetV2(weights='imagenet')
        prediction = model.predict(ready_image)
        decoded = tf.keras.applications.inception_resnet_v2.decode_predictions(prediction)[0][0][1]

        return render(request, 'index.html', {'new_url': str(decoded)})
    else:
        return render(request, 'index.html')