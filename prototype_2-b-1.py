#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Prototype_2-b-1

This prototype part reads the color mask image and converts it to a binary mask. 
Also, it assigns attribute names and material names to the packaging attributes. 

You might have to change the path names 

References

[1] Programmer Sought. (2021). Python uses the mask to cut out (using PIL.image and cv2) to output a 
transparent background image. https://www.programmersought.com/article/54555439083/

"""

#--------------------------------REPLACE_USERPATH--------------------------------

"""

Replace the user path with the path of your computer

Example:
    
"/Users/ruthstam/ruth-stam_GR/prototypes/"

"""

user_path = "/Users/ruthstam/ruth-stam_GR/prototypes/"

#--------------------------------IMPORT_FUNCTIONS--------------------------------

import cv2
from PIL import Image
import numpy as np
import os

#--------------------------------USER_INPUT_IMAGE--------------------------------

"""

The input_name connects with the barcode scan of the app interface.

"""

# input name = barcode scan
input_name = "alpro_cooking"

#--------------------------------LOADING--------------------------------

"""

The input_image connects with the packaging caputering part of the app interface.

The input_mask connects with the packaging attribute coloring part of the app interface.

"""

input_image = user_path + "/" + input_name +".jpg"
input_mask = user_path + "/"  + input_name + "_mask.jpg"

#--------------------------------LISTS_DIC_START--------------------------------

masks = []

#--------------------------------CREATE_MASK_[1]--------------------------------

class UnsupportedFormat(Exception):
    def __init__(self, input_type):
        self.t = input_type

    def __str__(self):
        return "The conversion of'{}' mode is not supported, please use the image address (path), PIL.Image (pil) or OpenCV (cv2) mode".format(self.t)


class MatteMatting():
    def __init__(self, original_graph, mask_graph, input_type='path'):
        """
                 Convert the input image into a transparent image constructor through a mask
                 :param original_graph: input image address, PIL format, CV2 format
                 :param mask_graph: The picture address of the mask, PIL format, CV2 format
                 :param input_type: input type, path: picture address, pil: pil type, cv2 type
        """
        if input_type == 'path':
            self.img1 = cv2.imread(original_graph)
            self.img2 = cv2.imread(mask_graph)
        elif input_type == 'pil':
            self.img1 = self.__image_to_opencv(original_graph)
            self.img2 = self.__image_to_opencv(mask_graph)
        elif input_type == 'cv2':
            self.img1 = original_graph
            self.img2 = mask_graph
        else:
            raise UnsupportedFormat(input_type)

    @staticmethod
    def __transparent_back(img):
        """
                 :param img: incoming picture address
                 :return: returns the transparent image after replacing the white
        """
        img = img.convert('RGBA')
        L, H = img.size
        color_0 = (255, 255, 255, 255)  # The color to be replaced
        for h in range(H):
            for l in range(L):
                dot = (l, h)
                color_1 = img.getpixel(dot)
                if color_1 == color_0:
                    color_1 = color_1[:-1] + (0,)
                    img.putpixel(dot, color_1)
        return img

    def save_image(self, path, mask_flip=False):
        """
                 Used to save transparent images
                 :param path: save location
                 :param mask_flip: Mask flip, flip the black and white color of the mask; True flip; False does not use flip
        """
        if mask_flip:
            img2 = cv2.bitwise_not(self.img2)  # Black and white flip
        image = cv2.add(self.img1, img2)
        image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # OpenCV converted to PIL.Image format
        img = self.__transparent_back(image)
        img.save(path)

    @staticmethod
    def __image_to_opencv(image):
        """
                 Convert PIL.Image to OpenCV format
        """
        img = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
        return img
    
#--------------------------------CHANGE_COLOR_PROFILE--------------------------------

image = cv2.imread(input_mask)

# convert image to RGB
packaging = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# convert image to HSV
hsv_packaging = cv2.cvtColor(packaging, cv2.COLOR_RGB2HSV)

#--------------------------------CHECK_IF_COLOR_IS_PRESENT--------------------------------

# orange mask 
orange_mask = cv2.inRange(hsv_packaging, (10,100,20), (24,255,255))
if cv2.countNonZero(orange_mask) > 0:
    orange_mask = Image.fromarray(orange_mask)
    orange_mask.save("orange_mask.jpg", mask_flip=True)
    masks.append("orange_mask.jpg")
else:
    print("Color orange is not in mask")

# blue mask 
blue_mask = cv2.inRange(hsv_packaging, (91,50,50), (105,255,255))
if cv2.countNonZero(blue_mask) > 0:
    blue_mask = Image.fromarray(blue_mask)
    blue_mask.save("blue_mask.jpg", mask_flip=True)
    masks.append("blue_mask.jpg")
else:
    print("Color blue is not in mask")

# yellow mask 
yellow_mask = cv2.inRange(hsv_packaging, (26,93,80), (35,255,255))
if cv2.countNonZero(yellow_mask) > 0:
    yellow_mask = Image.fromarray(yellow_mask)
    yellow_mask.save("yellow_mask.jpg", mask_flip=True)
    masks.append("yellow_mask.jpg")
else:
    print("Color yellow is not in mask")
 
# green mask
green_mask = cv2.inRange(hsv_packaging, (63,80,40), (73,255,255))
if cv2.countNonZero(green_mask) > 0:
    green_mask = Image.fromarray(green_mask)
    green_mask.save("green_mask.jpg", mask_flip=True)
    masks.append("green_mask.jpg")
else:
    print("Color green is not in mask")
    
# pink mask
pink_mask = cv2.inRange(hsv_packaging, (170,0,50), (180,255,255))
if cv2.countNonZero(pink_mask) > 0:
    pink_mask = Image.fromarray(pink_mask)
    pink_mask.save("pink_mask.jpg", mask_flip=True)
    masks.append("pink_mask.jpg")
else:
    print("Color pink is not in mask")

#--------------------------------ASSIGN_NAMES+CUT_PACKAGING_ATTRIBUTE--------------------------------

"""

This part of the prototype iterates through the masks list 
and asks to assign attribute names and attribute material names.

After assigning names, the image attribute is saved within th dataset folder.

"""

# iterate through masks 
for mask in masks:
    if mask == "orange_mask.jpg":
        
        color = "orange"
    
    if mask == "blue_mask.jpg":
        
        color = "blue"
        
    if mask == "yellow_mask.jpg":
        
        color = "yellow"
        
    if mask == "green_mask.jpg":
        
        color = "green"
        
    if mask == "pink_mask.jpg":
        
        color = "pink"
        
    #this will be an navigation menu in the dashboard
    
    print("orange attribute = Dop blue attribute = Drankenkarton")
    
    name_attribute = input("Which packaging attribute is "+ color +"? ")
    
    print("orange material = Plastic, blue material = Gecombineerd")
    
    name_material = input("Which material is "+ color +"? ")
        
    mm = MatteMatting(input_image, mask)
            
    mm.save_image(input_name + "_" + name_attribute + "_" + name_material + ".png", mask_flip=True)
        
    img = cv2.imread(input_name + "_" + name_attribute + "_" + name_material + ".png", 1)
    
    path = user_path + "dataset_images/"
        
    cv2.imwrite(os.path.join(path + name_attribute +  "/" + name_material + "/" + ((str.lower(name_attribute)) +  "_" + (str.lower(name_material)) + "_" + input_name) + ".png"), img)
    
print("The packaging attributes are stored in the dataset_images folder. Please return to the app interface.")