import cv2                          # importing openCV module
import matplotlib.pyplot as plt     # importing matplotlib
import time

                                                                            #letting the program know how each object looks
play_cascade=cv2.CascadeClassifier('cascade_play_sandeep_github.xml')               #loading trained classifier for closed fist
pause_cascade=cv2.CascadeClassifier('cascade_pause.xml')                    #loading trained classifier for open palm
vol_up_cascade=cv2.CascadeClassifier('v7_thumbsup.xml')
vol_down_cascade=cv2.CascadeClassifier('v13_thumbsdown.xml')
forward_cascade=cv2.CascadeClassifier('v2_forward.xml')
backward_cascade=cv2.CascadeClassifier('v10_backward.xml')

#reads from the web cam
#creating variable name "cap"
#inside cv2, we create an object of the class "VideoCapture" and pass the argument '0' which is the default camera
cap=cv2.VideoCapture(0)


cap.set(3,1028)             # sets the output window resolution to 1028. code for the height is 3
cap.set(4,720)              # sets the output window resolution to 720. code for the  width is 4



while True:    #While loop to capture the frame continuosly

    time.sleep(0.2)


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

    #faces = face_cascade.detectMultiScale(gray, 1.3, 5) # detecting faces in each frame and saving into variable=faces
    play = play_cascade.detectMultiScale(gray, 1.4, 5)  # detecting play in frame and  saving into variable=play
    pause=pause_cascade.detectMultiScale(gray,1.3,4)
    vol_up=vol_up_cascade.detectMultiScale(gray,1.4,5)
    vol_down=vol_down_cascade.detectMultiScale(gray,1.3,4)
    forward=forward_cascade.detectMultiScale(gray,1.4,5)
    backward=backward_cascade.detectMultiScale(gray,1.4,5)



    for (px, py, pw, ph) in play:

        cv2.rectangle(frame, (px, py), (px + pw, py + ph), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_TRIPLEX
        text = cv2.putText(frame, '    PLAY    ', (-80, 150), font, 1.5, (0, 255, 0), 2, cv2.LINE_4)
        plt.imshow(text)


    for (psx, psy, psw, psh) in pause:
        cv2.rectangle(frame, (psx, psy), (psx + psw, psy + psh), (18, 255, 255), 2)
        font = cv2.FONT_HERSHEY_TRIPLEX
        text = cv2.putText(frame, '     PAUSE    ', (-110, 250), font, 1.5, (18, 255, 255), 2, cv2.LINE_4)
        plt.imshow(text)


    for (vux, vuy, vuw, vuh) in vol_up:
        cv2.rectangle(frame, (vux, vuy), (vux + vuw, vuy + vuh), (18, 255, 255), 2)
        font = cv2.FONT_HERSHEY_TRIPLEX
        text = cv2.putText(frame, '     Volume up   ', (-110, 150), font, 1.5, (18, 255, 255), 2, cv2.LINE_4)
        plt.imshow(text)


    for (vdx, vdy, vdw, vdh) in vol_down:
        cv2.rectangle(frame, (vdx, vdy), (vdx + vdw, vdy + vdh), (255, 255, 255), 2)
        font = cv2.FONT_HERSHEY_TRIPLEX
        text = cv2.putText(frame, '     Volume down   ', (-110, 300), font, 1.5, (255, 255, 255), 2, cv2.LINE_4)
        plt.imshow(text)


    for (fx, fy, fw, fh) in forward:
        cv2.rectangle(frame, (fx, fy), (fx + fw, fy + fh), (255, 153, 255), 2)
        font = cv2.FONT_HERSHEY_TRIPLEX
        text = cv2.putText(frame, '     forward  ', (-120, 200), font, 1.5, (255, 153, 255), 2, cv2.LINE_4)
        plt.imshow(text)

    for (bx, by, bw, bh) in backward:
        cv2.rectangle(frame, (bx, by), (bx + bw, by + bh), (255, 153, 255), 2)
        font = cv2.FONT_HERSHEY_TRIPLEX
        text = cv2.putText(frame, '     backward  ', (-120, 200), font, 1.5, (255, 153, 255), 2, cv2.LINE_4)
        plt.imshow(text)




    cv2.imshow('video',frame)           # to show the frame captured by the camera.
                                        #imshow(any name for output window, variable 'frame')

    if cv2.waitKey(1) & 0xFF == ord('q'):   #using waitkey() to wait for user to enter 'q' to quit the output window
                                            # we have to provide mask for 64 bit machines; 0xFF
        break                               #if 'q' is pressed, then come out of the While loop


cap.release()                       #releasing capture variable 'cap' and all the resources
cv2.destroyAllWindows()             #destroy the output window

