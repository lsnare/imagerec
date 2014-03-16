from PIL import Image
import os
import numpy as np

def scale(image, max_size, method=Image.ANTIALIAS):
    """
    resize 'image' to 'max_size' keeping the aspect ratio 
    and place it in center of white 'max_size' image 
    """
    im_aspect = float(image.size[0])/float(image.size[1])
    out_aspect = float(max_size[0])/float(max_size[1])
    if im_aspect >= out_aspect:
        scaled = image.resize((max_size[0], int((float(max_size[0])/im_aspect) + 0.5)), method)
    else:
        scaled = image.resize((int((float(max_size[1])*im_aspect) + 0.5), max_size[1]), method)
 
    offset = (((max_size[0] - scaled.size[0]) / 2), ((max_size[1] - scaled.size[1]) / 2))
    back = Image.new("RGB", max_size, "white")
    back.paste(scaled, offset)
    return back

def resizeToLargest():
    largest = Image.open('newimages/cq-10.gif')
    #cycle through all images to find the largest
    for dirpath, dirnames, filenames in os.walk('newimages/'):
        for curFile in filenames:
            imgFilePath = 'newimages/'+curFile
            nextIm = Image.open(imgFilePath)
            if nextIm.size > largest.size:
                largest = nextIm
    for dirpath, dirnames, filenames in os.walk('newimages/'):
       for curFile in filenames:
            imgFilePath = 'newimages/'+curFile
            nextIm = Image.open(imgFilePath)
            nextIm = scale(nextIm, largest.size, Image.ANTIALIAS) 
            nextIm = nextIm.convert('1')
            nextIm.save(imgFilePath)

#Populates a text file with the array versions of each image
def createExamples():
    if(os.path.isfile('noteArEx.txt')):
        os.remove('noteArEx.txt')
    numberArrayExamples = open('noteArEx.txt', 'a')

    for dirpath, dirnames, filenames in os.walk('newimages/'):
        for curFile in filenames:
            imgFilePath = 'newimages/'+curFile
            ei = Image.open(imgFilePath)
            #convert the image to an array and a list
            eiar = np.array(ei)
            eiar1 = str(eiar.tolist())
            name = list(curFile)
            
            #format file input, print to file
            if len(name)>8:
                lineToWrite = "".join(name[:4]) +'::'+eiar1+'\n'
            else:
                lineToWrite = "".join(name[:3]) +'::'+eiar1+'\n'

            numberArrayExamples.write(lineToWrite)

resizeToLargest()
createExamples()
