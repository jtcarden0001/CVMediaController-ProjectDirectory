# Computer Vision Media Controller

### Download
An executable of the Computer Vision Media Controller is available [here](https://www.dropbox.com/s/4iuygu5w156nnc0/CV%20Media%20Controller.exe?dl=0).

### About
The Computer Vision Media Controller is a program that can send media player controls to a YouTube video using either facial recognition or gesture recognition.

### Using the Program
Upon launching the program, enter the URL of a YouTube video into the provided text input field and click `Start`. Playback will begin.

### Program Modes
There are two modes that the program can operate in: Facial Recognition Mode and Gesture Recognition Mode. This can be selected using a radio button toggle in main UI.

In Facial Recognition Mode, the video will play as long as a face is detected by your webcam. When no face is detected, the video will pause.

In Gesture Recognition Mode, the video will be controlled by hand gestures detected by your webcam. The supported gestures are:

| Play | Pause | Vol Up | Vol Down | Fast Forward | Rewind |
| ---- | ----- | ------ | -------- | ------------ | ------ |
| <img src="https://github.com/jtcarden0001/CVMediaController-ProjectDirectory/blob/master/Hand%20Gestures/play.jpg?raw=true" height = "100" width = "100"> | <img src="https://github.com/jtcarden0001/CVMediaController-ProjectDirectory/blob/master/Hand%20Gestures/pause.jpg?raw=true" height = "100" width = "100"> | <img src="https://github.com/jtcarden0001/CVMediaController-ProjectDirectory/blob/master/Hand%20Gestures/volume%20up.jpg?raw=true" height = "100" width = "100"> | <img src="https://github.com/jtcarden0001/CVMediaController-ProjectDirectory/blob/master/Hand%20Gestures/volume%20down.jpg?raw=true" height = "100" width = "100"> | <img src="https://github.com/jtcarden0001/CVMediaController-ProjectDirectory/blob/master/Hand%20Gestures/fast%20forward.jpg?raw=true" height = "100" width = "100"> | <img src="https://github.com/jtcarden0001/CVMediaController-ProjectDirectory/blob/master/Hand%20Gestures/rewind.jpg?raw=true" height = "100" width = "100"> |

### Repo Organization
The various components of the program have been developed independently from each other and reside in the appropriately named folders. The complete program is in the folder titled `CV Media Controller Prototype`.
