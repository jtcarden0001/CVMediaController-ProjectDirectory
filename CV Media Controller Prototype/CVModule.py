import cv2
import numpy as np
import time


# Function that regulates when a state shift should occur.  It requires that an image should be
# recognized at least 2 times in a row before a state shift is accomplished to prevent choppy performance
def state_shift(tolerance_arr, i):
    for j in range(len(tolerance_arr)):
        if j == i:
            tolerance_arr[j] += 1
        else:
            tolerance_arr[j] = 0

    if tolerance_arr[i] > 1:
        return True
    return False


class FaceDetector:

    # inside cv2, we create an object of the class "VideoCapture" and pass the argument
    # '0' which is the default camera
    # sets the output window resolution to 1028. code for the height is 3
    # sets the output window resolution to 720. code for the  width is 4
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('CV models/haarcascade_frontalface_default.xml')
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 1028)
        self.cap.set(4, 720)
        self.state = 0

    def detect(self, video_frame, root):
        # Each element in the tolerance array represents a possible state for the player to be in
        tolerance = [0, 0]
        # TODO: break this while loop into smaller testable functions
        while video_frame.current_mode() == 1:
            root.update()
            ret, frame = self.cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

            if np.sum(faces) > 0:
                if state_shift(tolerance, 0):
                    self.state = 0
            else:
                if state_shift(tolerance, 1):
                    self.state = 1

            if self.state == 0:
                video_frame.update_status("Face Mode: play")
                video_frame.player.play()
            else:
                video_frame.update_status("Face Mode: pause")
                video_frame.player.pause()

            time.sleep(.3)


class GestureDetector:

    # inside cv2, we create an object of the class "VideoCapture" and pass the argument
    # '0' which is the default camera
    # sets the output window resolution to 1028. code for the height is 3
    # sets the output window resolution to 720. code for the  width is 4
    def __init__(self):
        self.play_cascade = cv2.CascadeClassifier('CV models/fist_sandeep_github.xml')  # loading trained classifier for closed fist
        self.pause_cascade = cv2.CascadeClassifier('CV models/cascade_pause.xml')  # loading trained classifier for open palm
        self.vol_up_cascade = cv2.CascadeClassifier('CV models/v5_thumbsup.xml')
        self.vol_down_cascade = cv2.CascadeClassifier('CV models/v11_thumbsdown.xml')
        self.right_sideways = cv2.CascadeClassifier('CV models/right sideways_sandeep_github.xml')
        self.left_sideways = cv2.CascadeClassifier('CV models/v6_backward.xml')
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 1028)
        self.cap.set(4, 720)
        self.state = 0

    def detect(self, video_frame, root):
        # Each element in the tolerance array represents a possible state for the player to be in
        tolerance = [0, 0, 0, 0, 0, 0]
        # TODO: break this while loop into smaller testable functions
        while video_frame.current_mode() == 2:
            root.update()
            ret, frame = self.cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            play = self.play_cascade.detectMultiScale(gray, 1.1, 5)  # detecting play in frame and  saving into variable=play
            pause = self.pause_cascade.detectMultiScale(gray, 1.1, 4)
            vol_up = self.vol_up_cascade.detectMultiScale(gray, 1.3, 5)
            vol_down = self.vol_down_cascade.detectMultiScale(gray, 1.1, 1)
            forward = self.right_sideways.detectMultiScale(gray, 1.1, 4)
            backward = self.left_sideways.detectMultiScale(gray, 1.1, 4)

            # TODO: this tolerance method of control may need rework
            if np.sum(play) > 0:
                if state_shift(tolerance, 0):
                    self.state = 0
            elif np.sum(pause):
                if state_shift(tolerance, 1):
                    self.state = 1
            elif np.sum(vol_up):
                if state_shift(tolerance, 2):
                    self.state = 2
            elif np.sum(vol_down):
                if state_shift(tolerance, 3):
                    self.state = 3
            elif np.sum(forward):
                if state_shift(tolerance, 4):
                    self.state = 4
            elif np.sum(backward):
                if state_shift(tolerance, 5):
                    self.state = 5

            if self.state == 0:
                video_frame.player.play()
                video_frame.update_status("Gesture: play")
            elif self.state == 1:
                video_frame.player.pause()
                video_frame.update_status("Gesture: pause")
            elif self.state == 2:
                video_frame.player.increase_volume()
                video_frame.update_status("Gesture: volume up: ")
            elif self.state == 3:
                video_frame.player.decrease_volume()
                video_frame.update_status("Gesture: volume down: ")
            elif self.state == 4:
                video_frame.player.jump_forward()
                video_frame.update_status("Gesture: forward")
            elif self.state == 5:
                video_frame.player.jump_back()
                video_frame.update_status("Gesture: backward")

            time.sleep(.3)
