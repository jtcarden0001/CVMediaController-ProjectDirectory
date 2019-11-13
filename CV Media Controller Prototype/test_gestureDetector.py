import tkinter as tk
from unittest import TestCase
from unittest.mock import MagicMock
from CVModule import GestureDetector
from GUIModule import VideoFrame


class TestGestureDetector(TestCase):
    def setUp(self):
        self.gesture_detector = GestureDetector()
        self.root = tk.Tk()
        self.frame = VideoFrame(self.root)

    def test_initial_values(self):
        assert (self.gesture_detector.state == 0)
        assert (self.gesture_detector.gesture_detection_streak == 0)

    def test_process_detected_gesture_threshold(self):
        #  assume the threshold is 2 for testing purposes
        self.gesture_detector.repeated_detections_required = 2

        #  process a "play" gesture. since the gesture streak is now 1 (less than threshold of 2), there should not
        #  be a media control executed
        self.gesture_detector.process_detected_gesture(self.frame, 0)
        assert(self.gesture_detector.gesture_detection_streak == 1)
        self.frame.player.play = MagicMock()
        self.frame.player.play.assert_not_called()

        #  process a second "play" gesture. since the gesture streak is now 2 (greater than or equal to the threshold
        #  value of 2), there should be a call to the "play" media control
        self.gesture_detector.process_detected_gesture(self.frame, 0)
        assert (self.gesture_detector.gesture_detection_streak == 2)
        self.frame.player.play.assert_called_once()

        #  process a "pause" gesture. since the gesture breaks the previous "play" streak, the state and streak
        #  should be reset
        self.gesture_detector.process_detected_gesture(self.frame, 1)
        assert (self.gesture_detector.state == 1)
        assert (self.gesture_detector.gesture_detection_streak == 1)

    def test_process_detected_gesture_media_controls(self):
        #  assume the threshold is 1 for testing purposes
        self.gesture_detector.repeated_detections_required = 1

        #  initialize mocks
        self.frame.player.play = MagicMock()
        self.frame.player.pause = MagicMock()
        self.frame.player.increase_volume = MagicMock()
        self.frame.player.decrease_volume = MagicMock()
        self.frame.player.jump_forward = MagicMock()
        self.frame.player.jump_back = MagicMock()

        #  test play
        self.gesture_detector.process_detected_gesture(self.frame, 0)
        self.frame.player.play.assert_called_once()

        #  test pause
        self.gesture_detector.process_detected_gesture(self.frame, 1)
        self.frame.player.pause.assert_called_once()

        #  test volume up
        self.gesture_detector.process_detected_gesture(self.frame, 2)
        self.frame.player.increase_volume.assert_called_once()

        #  test volume down
        self.gesture_detector.process_detected_gesture(self.frame, 3)
        self.frame.player.decrease_volume.assert_called_once()

        #  test jump forward
        self.gesture_detector.process_detected_gesture(self.frame, 4)
        self.frame.player.jump_forward.assert_called_once()

        #  test jump back
        self.gesture_detector.process_detected_gesture(self.frame, 5)
        self.frame.player.jump_back.assert_called_once()
