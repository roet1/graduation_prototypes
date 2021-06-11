#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Prototype_2-b-2

This prototype part converts the packaging image and mask image of prototype_2-b-1 into COCO format.

The COCO format annotations are saved as a JSON element. the JSON element corosponds with the JSON prototype_2-dataset file.


References

[2] Kelly, A. (2020, April 30). Create COCO annotations from scratch. 
Immersive Limit. https://www.immersivelimit.com/tutorials/create-coco-annotations-from-scratch

"""

#--------------------------------REPLACE_USERPATH--------------------------------

"""

Replace the user path with the path of your computer

Example:
    
"/Users/ruthstam/ruth-stam_GR/prototypes/"

"""

user_path = "/Users/ruthstam/ruth-stam_GR/prototypes/"

#--------------------------------IMPORT_FUNCTIONS--------------------------------


from PIL import Image
import numpy as np
from shapely.geometry import MultiPolygon, Polygon
from skimage import measure
import json

#--------------------------------LOAD_IMAGES--------------------------------

"""

Load the paths of the image attribute and matching mask image retrieved from 
prototype_2-a-1

"""

#pink_mask_image = Image.open("/Users/ruthstam/Afstuderen/mask/pink_mask.jpg")
#path_pink = "/Users/ruthstam/Afstuderen/mask/dataset_images/Fles/Glas/fles_glas_heinz_ketchup_gwoon_olijfolie.png"

#yellow_mask_image = Image.open("/Users/ruthstam/Afstuderen/mask/pink_mask.jpg")
#path_yellow = "/Users/ruthstam/Afstuderen/mask/dataset_images/Dop/Metaal/dop_metaal_heinz_ketchup_gwoon_olijfolie.png"

blue_mask_image = Image.open(user_path + "blue_mask.jpg")
path_blue = user_path + "dataset_images/Drankenkarton/Gecombineerd/drankenkarton_gecombineerd_alpro_cooking.png"

#green_mask_image = Image.open("/Users/ruthstam/Afstuderen/mask/green_mask.jpg")
#mask_paths.append(" ")

orange_mask_image = Image.open("/Users/ruthstam/ruth-stam_GR/prototypes/orange_mask.jpg")
path_orange = "/Users/ruthstam/ruth-stam_GR/prototypes/dataset_images/Dop/Plastic/dop_plastic_alpro_cooking.png"


#--------------------------------CREATE_CATEGORY_ID--------------------------------

def get_category_id(path):
    
    # simulate category_id for prototype 
    
    if (("Fles" in path) and ("Plastic" in path)):
        
        category_id = 25
    
    if (("Fles" in path) and ("Glas" in path)):
        
        category_id = 24
    
    if (("Dop" in path) and ("Metaal" in path)):
        
        category_id = 19
    
    if (("Dop" in path) and ("Plastic" in path)):
        
        category_id = 19
    
    if (("Sachet" in path) and ("Gecombineerd" in path)):
        
        category_id = 43     
    
    if (("Drankenkarton" in path) and ("Gecombineerd" in path)):
        
        category_id = 21 
    
    return category_id

#--------------------------------CREATE_MASK_ANNOTATIONS[2]--------------------------------

def create_sub_mask_annotation(sub_mask, image_id, category_id, annotation_id, is_crowd):
    # Find contours (boundary lines) around each sub-mask
    # Note: there could be multiple contours if the object
    # is partially occluded. (E.g. an elephant behind a tree)
    contours = measure.find_contours(sub_mask, 0.5, positive_orientation="low")

    segmentations = []
    polygons = []
    for contour in contours:
        # Flip from (row, col) representation to (x, y)
        # and subtract the padding pixel
        for i in range(len(contour)):
            row, col = contour[i]
            contour[i] = (col - 1, row - 1)

        # Make a polygon and simplify it
        poly = Polygon(contour)
        poly = poly.simplify(1.0, preserve_topology=False)
        polygons.append(poly)
        segmentation = np.array(poly.exterior.coords).ravel().tolist()
        segmentations.append(segmentation)

    # Combine the polygons to calculate the bounding box and area
    multi_poly = MultiPolygon(polygons)
    x, y, max_x, max_y = multi_poly.bounds
    width = max_x - x
    height = max_y - y
    bbox = (x, y, width, height)
    area = multi_poly.area

    annotation = {
        "segmentation": segmentations,
        "iscrowd": is_crowd,
        "image_id": image_id,
        "category_id": category_id,
        "id": annotation_id,
        "bbox": bbox,
        "area": area
    }

    return annotation

#--------------------------------LOAD_MASKS+ANNOTATE--------------------------------

# create list for mask images
mask_images = [blue_mask_image, orange_mask_image]

# is_crowd will always be 0
is_crowd = 0
        
# this variables will attomatically increase
annotation_id = 1

# this variable refers to image in prototype_2-dataset JSON file 
image_id = 1
        
# create annotation list
annotations = []

for mask_image in mask_images:
    
    #if mask_image == pink_mask_image:
    #    path = path_pink
    #if mask_image == yellow_mask_image:
    #    path = path_yellow
    if mask_image == blue_mask_image:
        path = path_blue
    if mask_image == orange_mask_image:
        path = path_orange
    #if mask_image == green_mask_image:
     #   path = path_green
     
    # retrieve category_id
    category_id = get_category_id(path)
    
    # retrieve annotations
    annotation = create_sub_mask_annotation(mask_image, image_id, category_id, annotation_id, is_crowd)
    
    # add annotations to annotation list 
    annotations.append(annotation)
    
    # increa annotation_id 
    annotation_id += 1
    
    print(json.dumps(annotations))
    
print("The packaging attributes and annotations are stored in the database. Please return to the app interface.")