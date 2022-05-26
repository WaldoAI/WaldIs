from turtle import back
import PIL
import random
import os
import glob
from PIL import Image

directory_path = os.path.dirname(__file__)
backgrounds_path = directory_path + "/backgrounds"
#background = Image.open("C:\\Users\\Waldo\Desktop\\waldo maker\\background.jpeg")
imagearray = []
print(directory_path)
for backgrounds in glob.iglob(backgrounds_path + '/*.png', recursive=True):
    imagearray.append(Image.open(backgrounds))
def generate():
    background = imagearray[random.randrange(0,len(imagearray))]
    background = background.resize((2000,2000))
    waldo = Image.open(directory_path + '/waldo.png')
    width, height = background.size
    smalldo = waldo.resize((150,150))
    #smalldo = waldo
    coordinates = (random.randrange(100,width-100),random.randrange(100,height-100))
    print(coordinates)
    #coordinates = (0,299) 
    background.paste(smalldo,coordinates,smalldo.convert('RGBA')
    )
    background.save(directory_path.replace('/generate','') + "/static/output.png")
    return coordinates