class MediaModule:

    def __init__(self):
        self.state = 0  # may change these states into an enum
        self.placeholder = 0

    def ValidateURL(self):
        self.placeholder = 0

    def Initialize(self):
        self.placeholder = 0

    def Play(self):
        self.state = 0

    def Pause(self):
        self.state = 1

    def IncreaseVolume(self):
        self.placeholder = 0

    def DecreaseVolume(self):
        self.placeholder = 0

    def JumpForward(self):
        self.placeholder = 0

    def JumpBack(self):
        self.placeholder = 0

    def GetState(self):
        self.placeholder = 0
