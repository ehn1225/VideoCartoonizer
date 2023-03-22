#2023-03-22
#Video To Cartoon Style
import cv2
import numpy as np

#Load the video(sample : "bird.mp4", "recorder.mp4"")
video = cv2.VideoCapture("bird.mp4")

if video.isOpened():
    # Get FPS and calculate the waiting time in millisecond
    fps = video.get(cv2.CAP_PROP_FPS)
    wait_msec = int(1 / fps * 1000)

    while True:
        # Read an image from 'video'
        valid, img = video.read()
        if not valid:
            break

        #Get Image Size and resize
        h, w, *_ = img.shape
        original = cv2.resize(img, dsize=(w//2, h//2), interpolation=cv2.INTER_LINEAR)

        #convert to cartoon style
        gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(original, 9, 300, 300)
        cartoon = cv2.bitwise_and(color, color, mask=edges)

        #Concat Images Vertically
        result = cv2.vconcat([original, cartoon])

        #Show the image
        cv2.imshow('Video Player', result)

        # Terminate if the given key is ESC
        key = cv2.waitKey(wait_msec)
        if key == 27: # ESC
            break

cv2.destroyAllWindows()
