import os
import cv2
import numpy

def read_images(path,image_size):
    names=[]
    training_images, training_labels = [],[]
    label_count = 0
    for dirname,filenames in os.walk(path):
        names.append(names.append(subdirname))
        for filename in os.listdir(dirname):
            image=cv2.imread(os.path.join(dir, filename),cv2.IMREAD_GRAYSCALE)
            if img is None:
                #the file cannot be loaded as an image
                continue
            image-cv2.resize(image,image_size)
            training_images.append(image)
            training_labels.append(label)
         label_count+=1

