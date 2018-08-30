# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 14:07:02 2018

this python script is to test single handedly one photo.
make sure to download the hdf5 weights file and putting it in the right directory.
you have two datasets to choose from:
    
    change the file_name to:
    
    normal brains:
    file_name = 'dataset/test_set/normal/normal.'+str(i)'+.jpg'
    you have 18 samples just change i to 1-18
    
    tumor brain:
    file_name = 'dataset/test_set/tumor/tumor.'+str(i)+'.jpg'
    you have 12 samples just change i to 1-12
    
    
    mri_model_weights.h5
    

@author: Amit
"""


#from keras.models import Sequential
import numpy as np
from keras.models import load_model
from keras.preprocessing import image


# returns a compiled model
# identical to the previous one
classifier1 = load_model('mri_model_weights.h5')

#Image index i
i = 6

#Predicting the Dogs dataset
image_name = 'tumor.'+str(i)+'.jpg'
file_name = 'dataset/test_set/tumor/tumor.'+str(i)+'.jpg'
test_image = image.load_img(file_name, target_size = (128, 128))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier1.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
     print('Model prediction for image '+image_name+':  TUMOR')
else:
     print('Model prediction for image '+image_name+':   NORMAL')
