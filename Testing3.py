import imageio
import cv2 # pip install opencv-python
import os
from os.path import isfile, join

def convert_pictures_to_video(pathIn, pathOut, fps, time):
    #this function converts images to video
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    for i in range (len(files)):
        filename = pathIn + files[i]
        #reading images
        img = cv2.imread(filename)
        # img=cv2.resize(img,(1400, 1000))
        height, width = img.shape
        size = (width, height)

        for k in range (time):
            frame_array.append(img)
    out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()

# example:
directory = 'C:/Users/teng448/Desktop/16505/V02/Fe'
pathIn = directory + '/'
pathOut = pathIn + 'video_example.avi'
fps = 1
time = 2 #the duration of each picture in the video

convert_pictures_to_video(pathIn, pathOut, fps, time)