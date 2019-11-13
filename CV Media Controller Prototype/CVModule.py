import cv2
import numpy as np
import time


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
        self.state_detection_streak = 0  # number of times the same state has been detected in a row
        self.repeated_detections_required = 2  # number of repeated detections needed to trigger a media control

    def process_detected_state(self, video_frame, current_state):
        #  if the current face/no face state doesn't match the previous state, reset the streak and the set the
        #  state to the current face/no face state
        if self.state != current_state:
            self.state = current_state
            self.state_detection_streak = 0

        #  increment the streak
        self.state_detection_streak += 1

        #  if the streak exceeds the given tolerance, execute the appropriate media control
        if self.state_detection_streak >= self.repeated_detections_required:
            if self.state == 0:
                video_frame.update_status("Face Mode: play")
                video_frame.player.play()
            elif self.state == 1:
                video_frame.update_status("Face Mode: pause")
                video_frame.player.pause()

    def detect(self, video_frame, root):
        # TODO: break this while loop into smaller testable functions
        while video_frame.current_mode() == 1:
            root.update()
            ret, frame = self.cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if np.sum(self.face_cascade.detectMultiScale(gray, 1.3, 5)) > 0:  # face detected
                self.process_detected_state(video_frame, 0)
            else:  # no face detected
                self.process_detected_state(video_frame, 1)

            time.sleep(.3)


class GestureDetector:

    # inside cv2, we create an object of the class "VideoCapture" and pass the argument
    # '0' which is the default camera
    # sets the output window resolution to 1028. code for the height is 3
    # sets the output window resolution to 720. code for the  width is 4
    def __init__(self):
        self.play_cascade = cv2.CascadeClassifier('CV models/cascade_play_sandeep_github.xml')
        self.pause_cascade = cv2.CascadeClassifier('CV models/cascade_pause.xml')
        self.vol_up_cascade = cv2.CascadeClassifier('CV models/v7_thumbsup.xml')
        self.vol_down_cascade = cv2.CascadeClassifier('CV models/v13_thumbsdown.xml')
        self.right_sideways = cv2.CascadeClassifier('CV models/v2_forward.xml')
        self.left_sideways = cv2.CascadeClassifier('CV models/v10_backward.xml')
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 1028)
        self.cap.set(4, 720)
        self.state = 0
        self.gesture_detection_streak = 0  # number of times the same gesture has been detected in a row
        self.repeated_detections_required = 2  # number of repeated detections needed to trigger a media control

    def process_detected_gesture(self, video_frame, current_gesture):
        #  if the current gesture doesn't match the previous gesture, reset the streak and the set the state to
        #  the current gesture
        if self.state != current_gesture:
            self.state = current_gesture
            self.gesture_detection_streak = 0

        #  increment the streak
        self.gesture_detection_streak += 1

        #  if the streak exceeds the given tolerance, execute the appropriate media control
        if self.gesture_detection_streak >= self.repeated_detections_required:
            if self.state == 0:
                video_frame.player.play()
                video_frame.update_status("Gesture: play")
            elif self.state == 1:
                video_frame.player.pause()
                video_frame.update_status("Gesture: pause")
            elif self.state == 2:
                video_frame.player.increase_volume()
                video_frame.update_status("Gesture: volume up")
            elif self.state == 3:
                video_frame.player.decrease_volume()
                video_frame.update_status("Gesture: volume down")
            elif self.state == 4:
                video_frame.player.jump_forward()
                video_frame.update_status("Gesture: forward")
            elif self.state == 5:
                video_frame.player.jump_back()
                video_frame.update_status("Gesture: backward")

    def detect(self, video_frame, root):
        # TODO: break this while loop into smaller testable functions
        while video_frame.current_mode() == 2:
            root.update()
            ret, frame = self.cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            #  check for the presence of a detected gesture in the following order:
            #   [play -> pause -> vol up -> vol down -> jump forward -> jump back]
            #  if a gesture is detected, do not process any further gestures in the same iteration
            #  this is to prevent false positives on low-priority gestures (such as jump back) from interfering with
            #  high-priority gestures (such as play / pause)
            if np.sum(self.play_cascade.detectMultiScale(gray, 1.4, 5)) > 0:  # play gesture detected
                self.process_detected_gesture(video_frame, 0)
            elif np.sum(self.pause_cascade.detectMultiScale(gray, 1.3, 4)) > 0:  # pause gesture detected
                self.process_detected_gesture(video_frame, 1)
            elif np.sum(self.vol_up_cascade.detectMultiScale(gray, 1.4, 5)) > 0:  # vol up gesture detected
                self.process_detected_gesture(video_frame, 2)
            elif np.sum(self.vol_down_cascade.detectMultiScale(gray, 1.3, 5)) > 0:  # vol down gesture detected
                self.process_detected_gesture(video_frame, 3)
            elif np.sum(self.right_sideways.detectMultiScale(gray, 1.4, 5)) > 0:  # jump forward gesture detected
                self.process_detected_gesture(video_frame, 4)
            elif np.sum(self.left_sideways.detectMultiScale(gray, 1.4, 5)) > 0:  # jump back gesture detected
                self.process_detected_gesture(video_frame, 5)

            time.sleep(0.3)
