#!/usr/bin/env python
# coding: utf-8

# In[2]:


from PIL import Image
from PIL import ImageFilter

img=Image.open("dog.jpg");
img.show();

for i in range(0,img.size[0]-1):
    for j in range(0,img.size[1]-1):
        pixelColorVals=img.getpixel((i,j));
        redPixel=255-pixelColorVals[0];
        greenPixel=255-pixelColorVals[0];
        bluePixel=255-pixelColorVals[0];
        img.putpixel((i,j),(redPixel,greenPixel,bluePixel));
img.show();
        


# In[ ]:




