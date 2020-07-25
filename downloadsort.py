import os
import time

#Function that takes downloads path, the final path 
#and the name of file being moved and then moves the file to the new path
def moveFile(path, dest, filenames):
    old_path = path + "\\" + filenames
    new_path = dest + "\\" + filenames
    os.rename(old_path, new_path)

#Paths, change these to your folder paths
path = r"C:\Users\user\Downloads"      #Default Downloads Folder
doc_path = r"C:\Users\user\Documents"  #Documents Folder
img_path = r"C:\Users\user\Pictures"   #Pictures Folder
vid_path = r"C:\Users\user\Video"      #Video Folder

img_extensions = ['.jpg', '.png', '.gif', '.jpeg']  #List of img extensions
doc_extensions = ['.txt', '.docx','.pdf']           #list of doc extensions
vid_extensions = ['.mp4', '.mov']                   #list of vid extensions

for filenames in os.listdir(path):
    #Handles Documents and moves them to documents folder
    for doc_extension in doc_extensions:
        if(filenames.endswith(doc_extension)):
            moveFile(path, doc_path, filenames)
    #Handles Pictures and moves them to pictures folder
    for img_extension in img_extensions:
        if(filenames.endswith(img_extension)):
            moveFile(path, img_path, filenames)
    #handles videos and mvoes them to videos folder
    for vid_extension in vid_extensions:
        if(filenames.endswith(vid_extension)):
             moveFile(path, vid_path, filenames)

