from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from collections import Counter

#Populates a text file with the array versions of each image
def createExamples():
	numberArrayExamples = open('numArEx.txt', 'a')
	numbersWeHave = range(0,10)
	versionsWeHave = range(1,10)

	for eachNum in numbersWeHave:
		for eachVer in versionsWeHave:
			#cycle through each file
			imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(eachVer)+'.png'
			#open the image			
			ei = Image.open(imgFilePath)
			#convert the image to an array and a list
			eiar = np.array(ei)
			eiar1 = str(eiar.tolist())

			#format file input, print to file
			lineToWrite = str(eachNum)+'::'+eiar1+'\n'
			numberArrayExamples.write(lineToWrite)

#a method to convert image to black and white
def threshold(imageArray):
	#array to average later
	balanceAr = []
	newAr = imageArray

	for eachRow in imageArray:
		for eachPix in eachRow:
			avgNum = reduce(lambda x, y: x + y, eachPix[:3])/len(eachPix[:3])
			balanceAr.append(avgNum)
	balance = reduce(lambda x, y: x + y, balanceAr)/len(balanceAr)
	for eachRow in newAr: 
		for eachPix in eachRow:
			if reduce(lambda x, y: x + y, eachPix[:3])/len(eachPix[:3]) > balance:
				eachPix[0] = 255;
				eachPix[1] = 255;
				eachPix[2] = 255;
				eachPix[3] = 255;
			else:
				eachPix[0] = 0;
				eachPix[1] = 0;
				eachPix[2] = 0;
				eachPix[3] = 255;
	return newAr

#image recognition!
def whatNumIsThis(filePath):
	matchedAr = []
	loadExamps = open('numArEx.txt', 'r').read()
	loadExamps = loadExamps.split('\n')
	
	i = Image.open(filePath)
	iar = np.array(i)
	iarl = iar.tolist()

	inQuestion = str(iarl)
	
	for eachExample in loadExamps:
		if len(eachExample) > 3:
			
			#split the file into arrays for each number			
			splitEx = eachExample.split('::')
			currentNum = splitEx[0]
			currentAr = splitEx[1]
	
			eachPixEx = currentAr.split('],')
			
			eachPixInQ = inQuestion.split('],')

			x=0
			
			while x < len(eachPixEx):
				if eachPixEx[x] == eachPixInQ[x]:
					matchedAr.append(int(currentNum))
								
				x += 1

	print matchedAr	
	#counts frequency of elements, returns dictionary	
	x = Counter(matchedAr)
	print x
	#from the frequency of elements in the array, we can make an educated guess as to which number matches the picture
	
whatNumIsThis('images/testNew.png')
	




