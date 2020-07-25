import os
import time
from extensions import * 
#Function that takes downloads path, the final path 
#and the name of file being moved and then moves the file to the new path
def moveFile(path, dest, filenames):
    old_path = path + "\\" + filenames
    new_path = dest + "\\" + filenames
    os.rename(old_path, new_path)

#Paths, change these to your folder paths
DIRS = [r"C:\Users\\Downloads",  r"C:\Users\\Pictures",r"C:\Users\\Documents", r"C:\Users\\Videos", r"C:\Users\\Music" ]

for filenames in os.listdir(DIRS[0]):
    name,extension = os.path.splitext(filenames)
    if extension in img_extensions:
        moveFile(DIRS[0], DIRS[1], filenames)
    elif extension in doc_extensions:
        moveFile(DIRS[0], DIRS[2], filenames)
    elif extension in vid_extensions:
        moveFile(DIRS[0], DIRS[3], filenames)
    elif extension in aud_extensions:
        moveFile(DIRS[0], DIRS[4], filenames)
    else:
        break
