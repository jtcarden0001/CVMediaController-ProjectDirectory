from CVModule import FaceDetector, GestureDetector
from GUIModule import VideoFrame
import tkinter as tk

root = tk.Tk()
frame = VideoFrame(root)
state = 0
face_detector = FaceDetector()
gesture_detector = GestureDetector()

while True:
    root.update()
    if frame.current_mode() == 1:
        state = face_detector.detect(frame, root, state)
    else:
        state = gesture_detector.detect(frame, root, state)
