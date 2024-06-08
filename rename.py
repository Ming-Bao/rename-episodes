import os

name = input("Enter name of file:")
offset = int(input("What episode to start at:"))
fileExtention = input("What is the file Extention:")
currentFilename = os.path.basename(__file__)

files = [f for f in os.listdir() if os.path.isfile(f) and f != currentFilename and f.split('.')[1] !="exe"]
files.sort
numPad = len(str(len(files)))

for i in range(0, len(files)):
    os.rename(files[i], f"{name} E{str(i+offset).zfill(numPad)}.{fileExtention}")