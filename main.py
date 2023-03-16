#importing required libraries
import cv2
import os
import string
import textwrap
import time
#Changing the directory to the project folder
ImageDict = {}
directory = __file__.removesuffix('main.py')
os.chdir(directory)
width = 75
#function to add image
def addImage(letter,symbolName=None):
    try:
        if letter.islower() or letter.isdigit():
            path = "Fonts\\"+ letter + ".jpg" 
            image = cv2.imread(os.path.join(directory,path))

        elif letter.isupper():
            path = "Fonts\\"+ letter + "c.jpg" 
            image = cv2.imread(os.path.join(directory,path))

        else:
            path = "Fonts\\"+ symbolName + ".jpg" 
            image = cv2.imread(os.path.join(directory,path))

        image = cv2.resize(image,(17,30), interpolation=cv2.INTER_LINEAR)
    
    except:
            path = "Fonts\\spaceline.jpg" 
            image = cv2.imread(os.path.join(directory,path))
            image = cv2.resize(image,(17,30), interpolation=cv2.INTER_LINEAR)

        


    ImageDict.update({letter: image})
    return ImageDict


#Importing all the image files
letters = string.ascii_letters
for letter in letters:
    addImage(letter)

for number in ['0','1','2','3','4','5','6','7','8','9']:
    addImage(number)

ImageDict = addImage(" ")
addImage('?', 'questionmark')
addImage('\'' , 'apostrophe')
addImage('\"' , 'apostrophe')
addImage('.' , 'Fullstop')
addImage(',' , 'Fullstop')

for symbols in ['€','¦',';','â','=','_','-','[',']','(',')']:
    addImage(symbols)



def lineToImage(line,ImageDict=ImageDict):
    for txt in line:
        try:
                
            hlist.append(ImageDict[txt])

        except:
            time.sleep(0.1)
            hlist.append(ImageDict['space'])
    

    length = len(hlist)
    while length < width:
        path = "Fonts\\spaceline.jpg" 
        spacePhoto = cv2.imread(os.path.join(directory,path))
        spacePhoto = cv2.resize(spacePhoto,(17,30), interpolation=cv2.INTER_LINEAR)

        hlist.append(spacePhoto)
        length+=1

    imageh  = cv2.hconcat(hlist)

    hlist.clear()
    return imageh

hlist = []
vlist = []


with open(os.path.join(directory,'textfile.txt')) as f:
    linesOfDoc=f.read().splitlines()
    for text in linesOfDoc: 
        if len(text) !=0:
            wrapper = textwrap.TextWrapper(width = width)
            wordlist = wrapper.wrap(text)
            for lines in wordlist:
                h_img = lineToImage(lines)
                vlist.append(h_img)
                print(text)

        else:
            
            h_img = lineToImage(' ')
            vlist.append(h_img)

    imagef = cv2.vconcat(vlist)

cv2.imshow('Handwritten File',imagef)
cv2.waitKey(0)
cv2.imwrite('Output.png', imagef)