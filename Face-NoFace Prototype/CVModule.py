from MediaModule import MediaPlayer
import cv2
import numpy as np
import keyboard
import time


class FaceDetector:

    # inside cv2, we create an object of the class "VideoCapture" and pass the argument
    # '0' which is the default camera
    # sets the output window resolution to 1028. code for the height is 3
    # sets the output window resolution to 720. code for the  width is 4
    def __init__(self):
        # TODO: having inconsistencies detecting faces with given classifier
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 1028)
        self.cap.set(4, 720)
        self.player = MediaPlayer()
        self.state = True

    def detect(self, player):
        self.player = player
        # what tolerance does is makes a CV reading need to happen 3 times in a row in order to change the
        # player states (play/pause).  This prevents small pauses and plays if there is a wrong reading
        tolerance = [0, 0]
        # TODO: break this while loop into smaller testable functions
        while True:
            ret, frame = self.cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

            if np.sum(faces) > 0:
                tolerance[0] += 1
                tolerance[1] = 0
                if tolerance[0] > 1:
                    self.state = True
                print("face")
            else:
                tolerance[1] += 1
                tolerance[0] = 0
                if tolerance[1] > 1:
                    self.state = False
                print("no face")

            if self.state:
                player.play()
            else:
                player.pause()

            if keyboard.is_pressed('q'):
                print("quit")
                self.cap.release()
                # cv2.destroyAllWindows()
                break

            # cv2.imshow('video', frame)
            time.sleep(.3)
        return [True, True]
