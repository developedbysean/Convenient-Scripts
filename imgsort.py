import os
import datetime

#Paths, change these to your folder paths
DIRS = [r"C:\Users\gopac\Downloads",  r"C:\Users\gopac\Pictures",r"C:\Users\gopac\Documents", r"C:\Users\gopac\Videos", r"C:\Users\gopac\Music" ]

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
