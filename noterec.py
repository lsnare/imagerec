from PIL import Image
import numpy as np
from collections import Counter

#image recognition!
def whatNoteIsThis(filePath):
    matchedAr = []

    #load the examples database
    loadExamps = open('noteArEx.txt', 'r').read()
    loadExamps = loadExamps.split('\n')

    #convert the image to array
    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()

    inQuestion = str(iarl)
    #cycle through examples
    for eachExample in loadExamps:
        if len(eachExample) > 3:
            
            #split the file into arrays for each number         
            splitEx = eachExample.split('::')
            currentNote = splitEx[0]
            currentAr = splitEx[1]
    
            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')
            x=0
            #fill up an array of matched pixels
            while x < len(eachPixInQ):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(currentNote)    
                x += 1

        
    #counts frequency of elements, returns dictionary entry of the most frequent    
    x = Counter(matchedAr)
    print x
    #from the frequency of elements in the array, we can make an educated guess as to which number matches the picture
