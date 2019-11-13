import tkinter as tk
from unittest import TestCase
from unittest.mock import MagicMock
from CVModule import FaceDetector
from GUIModule import VideoFrame


class TestFaceDetector(TestCase):
    def setUp(self):
        self.face_detector = FaceDetector()
        self.root = tk.Tk()
        self.frame = VideoFrame(self.root)

    def test_initial_values(self):
        assert (self.face_detector.state == 0)
        assert (self.face_detector.state_detection_streak == 0)

    def test_process_detected_state_threshold(self):
        #  assume the threshold is 2 for testing purposes
        self.face_detector.repeated_detections_required = 2

        #  process a "play" state. since the state streak is now 1 (less than threshold of 2), there should not
        #  be a media control executed
        self.face_detector.process_detected_state(self.frame, 0)
        assert(self.face_detector.state_detection_streak == 1)
        self.frame.player.play = MagicMock()
        self.frame.player.play.assert_not_called()

        #  process a second "play" state. since the state streak is now 2 (greater than or equal to the threshold
        #  value of 2), there should be a call to the "play" media control
        self.face_detector.process_detected_state(self.frame, 0)
        assert (self.face_detector.state_detection_streak == 2)
        self.frame.player.play.assert_called_once()

        #  process a "pause" state. since the state breaks the previous "play" streak, the state and streak
        #  should be reset
        self.face_detector.process_detected_state(self.frame, 1)
        assert (self.face_detector.state == 1)
        assert (self.face_detector.state_detection_streak == 1)

    def test_process_detected_state_media_controls(self):
        #  assume the threshold is 1 for testing purposes
        self.face_detector.repeated_detections_required = 1

        #  initialize mocks
        self.frame.player.play = MagicMock()
        self.frame.player.pause = MagicMock()

        #  test play
        self.face_detector.process_detected_state(self.frame, 0)
        self.frame.player.play.assert_called_once()

        #  test pause
        self.face_detector.process_detected_state(self.frame, 1)
        self.frame.player.pause.assert_called_once()
