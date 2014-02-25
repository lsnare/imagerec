from PIL import Image
'''
This is the modified version for our project
'''
import numpy as np
import matplotlib.pyplot as plt
import time
from collections import Counter

#Populates a text file with the array versions of each image
def createExamples():
	numberArrayExamples = open('noteArEx.txt', 'a')
	notesWeHave = range(0,9)
	versionsWeHave = range(1,1)

	for eachNum in notesWeHave:
		
		#cycle through each file
		imgFilePath = 'images/'+str(eachNum)+'.'+'1.png'
		#open the image			
		ei = Image.open(imgFilePath)
		#convert the image to an array and a list
		eiar = np.array(ei)
		eiar1 = str(eiar.tolist())

		#format file input, print to file
		lineToWrite = str(eachNum)+'::'+eiar1+'\n'
		numberArrayExamples.write(lineToWrite)
		print eachNum

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
	note_dict = {0: 'E', 1: 'F', 2: 'G', 3: 'A', 4: 'B', 5: 'C', 6: 'D', 7: 'E'} 
	loadExamps = open('noteArEx.txt', 'r').read()
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

		
	#counts frequency of elements, returns dictionary entry of the most frequent	
	x = Counter(matchedAr).most_common(1)[0][0]
	print "The note you showed me is an " + note_dict[x]
	#from the frequency of elements in the array, we can make an educated guess as to which number matches the picture

	'''graphX = []
	graphY = []

	for eachThing in x:
		print eachThing
		graphX.append(eachThing)
		print x[eachThing]
		graphY.append(x[eachThing])

	fig = plt.figure()
	ax1 = plt.subplot2grid((4,4),(0,0),rowspan=1, colspan=4)
	ax2 = plt.subplot2grid((4,4),(1,0),rowspan=3, colspan=4)

	ax1.imshow(iar)

	ax2.bar(graphX, graphY, align='center')

	plt.ylim(400)
	xloc = plt.MaxNLocator(12)
	ax2.xaxis.set_major_locator(xloc)
	plt.show()'''



whatNumIsThis('tester.png')
#createExamples()	



	




