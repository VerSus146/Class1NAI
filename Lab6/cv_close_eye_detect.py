from __future__ import print_function
import cv2 as cv
import argparse
from video_player import VideoCommercialPlayer
import os

def detectAndDisplay(frame, noEyesCounter):
    frame_gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray, minNeighbors=2)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame_gray, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h,x:x+w]

        #-- In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)
        eyes_detected = bool(len(eyes) > 0)

        #if no eyes detected - stop the video
        if eyes_detected is False:
            noEyesCounter += 1
            if noEyesCounter > 20:
                commercial.pauseVideo()
                #play warning message
                os.system("afplay alarm.mp3")
        print ('noEyesCounter' + str(noEyesCounter))

        for (x2,y2,w2,h2) in eyes:
            print('eyes_detected in for:' + str(eyes_detected))
            # eyes detected - play the commercial and reset no eyes counter
            noEyesCounter = 0

            commercial.playVideo()

            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.125))
            frame = cv.circle(frame_gray, eye_center, radius, (255, 0, 0 ), 4)
    cv.imshow('Capture - Face detection', frame)
    return noEyesCounter


parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
parser.add_argument('--face_cascade', help='Path to face cascade.', default='haarcascade_frontalface_alt.xml')
parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='haarcascade_eye_tree_eyeglasses.xml')
parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
args = parser.parse_args()
face_cascade_name = args.face_cascade
eyes_cascade_name = args.eyes_cascade
face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()

#-- 1. Load the cascades
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(cv.samples.findFile(eyes_cascade_name)):
    print('--(!)Error loading eyes cascade')
    exit(0)
camera_device = args.camera

#-- 2. Read the video stream
cap = cv.VideoCapture(camera_device)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)

commercial = VideoCommercialPlayer()
no_eyes_counter = 0

while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break

    commercial.displayVideo()
    print('No eyes counter before:' + str(no_eyes_counter))
    no_eyes_counter = detectAndDisplay(frame, no_eyes_counter)
    print('No eyes counter after:' + str(no_eyes_counter))

    if cv.waitKey(10) == 27:
        break