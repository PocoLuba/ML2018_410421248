import numpy as ny
from PIL import Image


img_k1 = Image.open('key1.png')
img_k2 = Image.open('key2.png')
img_E = Image.open('E.png')
img_i = Image.open('I.png')
img_Eprime = Image.open('Eprime.png')
Limit = 15
Learningrate = 1e-6
Epoch = 1
w = [1,1,1]

while Epoch == 1 or  Epoch < Limit:
    for i in range(400):
        for j in range(300):
            pass
            a = w[0] * img_k1.getpixel((i,j)) + w[1] * img_k2.getpixel((i,j)) + w[2] * img_i.getpixel((i,j))
            e = img_E.getpixel((i,j)) - a
            w[0]+=w[0] + Learningrate * e * img_k1.getpixel((i,j))
            w[1]+=w[1] + Learningrate * e * img_k2.getpixel((i,j))
            w[2]+=w[2] + Learningrate * e * img_i.getpixel((i,j))
    Epoch+=1