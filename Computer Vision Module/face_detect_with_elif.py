import cv2                          # importing openCV module
import matplotlib.pyplot as plt     # importing matplotlib
import numpy as np                  #importing numpy

                                                                            #letting the program know how each object looks
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')   #loading trained classifier for face detection
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')                    #loading trained classifier for eye
play_cascade=cv2.CascadeClassifier('fist_sandeep_github.xml')               #loading trained classifier for closed fist
pause_cascade=cv2.CascadeClassifier('cascade_pause.xml')                    #loading trained classifier for open palm
vol_up_cascade=cv2.CascadeClassifier('v5_thumbsup.xml')
vol_down_cascade=cv2.CascadeClassifier('v11_thumbsdown.xml')
right_sideways=cv2.CascadeClassifier('right sideways_sandeep_github.xml')
left_sideways=cv2.CascadeClassifier('v6_backward.xml')

#reads from the web cam
#creating variable name "cap"
#inside cv2, we create an object of the class "VideoCapture" and pass the argument '0' which is the default camera
cap=cv2.VideoCapture(0)


cap.set(3,1028)             # sets the output window resolution to 1028. code for the height is 3
cap.set(4,720)              # sets the output window resolution to 720. code for the  width is 4



while True:    #While loop to capture the frame continuosly

    ret, frame= cap.read()   # defining variables 'ret' and 'frame'. With 'cap' instance, calling method read()
                             #read() will return True if frame is available and save it to variable 'frame'
                             #'ret' variable will save True or False


    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)       #converting the frame into grayscale

    #objects= cv.CascadeClassifier.detectMultiScale( image, scaleFactor, minNeighbors) where
    #image= Matrix of the type CV_8U containing an image where objects are detected
    #objects= Vectors of rectangles where each rectangle contains the detected object
    #scaleFactor= Parameter specifying how much the image size is reduced at each image scale
    #minNeighbors= Parameters specifying how many neighbors each candidate rectangle should have to retain it
    #changing scaleFactor and minNeighbors to different values changes the sensitivity of the detection.

    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # detecting faces in each frame and saving into variable=faces
    play = play_cascade.detectMultiScale(gray, 1.1, 5)  # detecting play in frame and  saving into variable=play
    pause=pause_cascade.detectMultiScale(gray,1.1,4)
    vol_up=vol_up_cascade.detectMultiScale(gray,1.3,5)
    vol_down=vol_down_cascade.detectMultiScale(gray,1.1,1)
    forward=right_sideways.detectMultiScale(gray,1.1,4)
    backward = left_sideways.detectMultiScale(gray, 1.1, 4)




    if (np.sum(faces)>0):                   #if x+y+w+h>0, draw a rectangle. np.sum() basically sums up the numpy array
        print('face detected')
        for (x, y, w, h) in faces:          # iterate over faces object. Parameters:x,y,width and height of the rectangle

            # cv2.rectangle(image,starting point, ending point, color, thickness)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255),2)  # draws rectangle around the face. starts from x and y to x+w and y+h
            roi_gray = gray[y:y + h,x:x + w]  # setting a boundry around face.Starts from y to y+h...... Will be used for eye detection.
            roi_color = frame[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)  # detecting eye inside the facial region

            for (ex, ey, ew, eh) in eyes:  # for loop inside faces to make sure eyes are never detected outside of the face
                font = cv2.FONT_HERSHEY_TRIPLEX  # setting the font

                # cv2.putText(image where text will be,text,cordinates of text, font, fontScale, color, thickness, line type )
                text = cv2.putText(frame, 'face', (1135, 100), font, 1.5, (0, 0, 255), 2, cv2.LINE_AA)
                plt.imshow(text)

                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0),2)  # drawing rectangle around the eyes

    elif (np.sum(play)> 0):
        print('play detected')
        for (px, py, pw, ph) in play:

            cv2.rectangle(frame, (px, py), (px + pw, py + ph), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_TRIPLEX
            text = cv2.putText(frame, '    PLAY    ', (-80, 150), font, 1.5, (0, 255, 0), 2, cv2.LINE_4)
            plt.imshow(text)

    elif (np.sum(pause)> 0):
        print('pause detected')
        for (psx, psy, psw, psh) in pause:
            cv2.rectangle(frame, (psx, psy), (psx + psw, psy + psh), (18, 255, 255), 2)
            font = cv2.FONT_HERSHEY_TRIPLEX
            text = cv2.putText(frame, '     PAUSE    ', (-110, 250), font, 1.5, (18, 255, 255), 2, cv2.LINE_4)
            plt.imshow(text)

    elif (np.sum(vol_up)> 0):
        print('volume up detected')
        for (vux, vuy, vuw, vuh) in vol_up:
            cv2.rectangle(frame, (vux, vuy), (vux + vuw, vuy + vuh), (18, 255, 255), 2)
            font = cv2.FONT_HERSHEY_TRIPLEX
            text = cv2.putText(frame, '     Volume up   ', (-110, 150), font, 1.5, (18, 255, 255), 2, cv2.LINE_4)
            plt.imshow(text)

    elif (np.sum(vol_down)> 0):
        print('volume down detected')
        for (vdx, vdy, vdw, vdh) in vol_down:
            cv2.rectangle(frame, (vdx, vdy), (vdx + vdw, vdy + vdh), (255, 255, 255), 2)
            font = cv2.FONT_HERSHEY_TRIPLEX
            text = cv2.putText(frame, '     Volume down   ', (-110, 300), font, 1.5, (255, 255, 255), 2, cv2.LINE_4)
            plt.imshow(text)

    elif (np.sum(forward)> 0):
        print('forward detected')
        for (bx, by, bw, bh) in forward:
            cv2.rectangle(frame, (bx, by), (bx + bw, by + bh), (255, 153, 255), 2)
            font = cv2.FONT_HERSHEY_TRIPLEX
            text = cv2.putText(frame, '     backward  ', (-120, 200), font, 1.5, (255, 153, 255), 2, cv2.LINE_4)
            plt.imshow(text)
    elif (np.sum(backward)>0):
        print('backward detected')
        for (bx, by, bw, bh) in backward:
            cv2.rectangle(frame, (bx, by), (bx + bw, by + bh), (255, 153, 255), 2)
            font = cv2.FONT_HERSHEY_TRIPLEX
            text = cv2.putText(frame, '     backward  ', (-120, 200), font, 1.5, (255, 153, 255), 2, cv2.LINE_4)
            plt.imshow(text)

    else:
        print("nothing detected")


    cv2.imshow('video',frame)           # to show the frame captured by the camera.
                                        #imshow(any name for output window, variable 'frame')

    if cv2.waitKey(1) & 0xFF == ord('q'):   #using waitkey() to wait for user to enter 'q' to quit the output window
                                            # we have to provide mask for 64 bit machines; 0xFF
        break                               #if 'q' is pressed, then come out of the While loop


cap.release()                       #releasing capture variable 'cap' and all the resources
cv2.destroyAllWindows()             #destroy the output window

