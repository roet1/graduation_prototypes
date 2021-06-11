#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Prototype_2-a

This prototype provides a barcode reader and decoder. After reading the code the barcod the consumer provides 
the packaging name through the app interface. 

The barcode and packaging name are combined for packaging valiation.

"""

#--------------------------------IMPORT_FUNCTIONS--------------------------------

import cv2
import numpy as np
from pyzbar.pyzbar import decode 

#--------------------------------LOAD+READ_IMAGE--------------------------------

input_mask = "/Users/ruthstam/ruth-stam_GR/prototypes/barcode_test.jpg"

image = cv2.imread(input_mask)

#--------------------------------READ+DECODE_BARCODE--------------------------------

for barcode in decode(image):
    
    # decode barcode number
    myData = barcode.data.decode('utf-8')
    
    # convert RIO to arrat
    pts = np.array([barcode.polygon],np.int32)
    
    # reshape array
    pts = pts.reshape((-1,1,2))
    
    # draw bounding box on mage
    cv2.polylines(image,[pts],True,(200,200,0),5)
    
    # retrieve second point for barcode text placement
    pts2 = barcode.rect
    
#--------------------------------SHOW_RESULT--------------------------------    
    
    cv2.putText(image,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX, 0.9,(200,200,0),2)
    
    cv2.imshow('Result', image)
    
    cv2.waitKey(1)

