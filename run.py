import os

try:
    import cv2

except:
    os.system('cmd /c "pip install -r requirements.txt"')



directory = __file__.removesuffix('run.py')
os.chdir(directory)

file = open('textfile.txt','w')
file.write('This is an auto-generated line, Replace this with the text you want'+('\n'*20))
file.close()
os.system('textfile.txt')
os.system('main.py')
os.remove('textfile.txt')
