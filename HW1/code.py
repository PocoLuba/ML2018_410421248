import random
import numpy as ny
from PIL import Image


img_k1 = Image.open('key1.png')
img_k2 = Image.open('key2.png')
img_E = Image.open('E.png')
img_i = Image.open('I.png')
img_Eprime = Image.open('Eprime.png')

img_I = Image.new("L", (400,300), 0)
Limit = 13
Learningrate = 1e-6
Epoch = 1
#w = [1,1,1]
w=[random.random(),random.random(),random.random()] 
while Epoch == 1 or  Epoch < Limit:   #Learning process begin (below are all derived from pdf)
    for i in range(400):
        for j in range(300):
            a = w[0] * img_k1.getpixel((i,j)) + w[1] * img_k2.getpixel((i,j)) + w[2] * img_i.getpixel((i,j))
            e = img_E.getpixel((i,j)) - a
            w[0]+= Learningrate * e * img_k1.getpixel((i,j))
            w[1]+= Learningrate * e * img_k2.getpixel((i,j))
            w[2]+= Learningrate * e * img_i.getpixel((i,j))
            #print(w[0],w[1],w[2])
    Epoch+=1

for i in range(400): #output is the decryption from the teacher face used by the w we learned
    for j in range(300):
        img_I.putpixel((i,j),int((img_Eprime.getpixel((i,j)) - w[0] * img_k1.getpixel((i,j)) - w[1] * img_k2.getpixel((i,j))) / w[2]
))
img_I.save("output.png")
