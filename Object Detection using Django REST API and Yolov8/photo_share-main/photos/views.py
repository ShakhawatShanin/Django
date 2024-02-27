from django.shortcuts import render
from .models import Photo
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2
import tensorflow as tf
import json
import pandas as pd


# Create your views here.
def index(request):
    if request.method == 'POST':
        new_photo = Photo(
            file = request.FILES['img']
        )
        new_photo.save()
        img = Image.open(request.FILES['img'])
        
        model = YOLO("best.pt")
        results = model.predict(img)
        data = json.loads(results[0].tojson())

        a = pd.DataFrame(data)
        print(a)



        # Calculate value counts for the specified column
        value_counts = a['name'].value_counts()
        # Convert the value counts series to a dictionary
        column_dict = value_counts.to_dict()

        return render(request, 'index.html', {'new_url': column_dict})
    else:
        return render(request, 'index.html')