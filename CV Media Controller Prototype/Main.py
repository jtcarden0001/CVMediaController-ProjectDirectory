from CVModule import FaceDetector, GestureDetector
from GUIModule import VideoFrame
import tkinter as tk

root = tk.Tk()
root.title("CV Media Controller")
frame = VideoFrame(root)
face_detector = FaceDetector()
gesture_detector = GestureDetector()

while True:
    root.update()
    if frame.current_mode() == 1:
        face_detector.detect(frame, root)
    else:
        gesture_detector.detect(frame, root)
