import cv2


class VideoCapture:

    def __init__(self):
        self.VIDEO = "resources/video.mp4"
        self.vid = None
        self.width = None
        self.height = None
        self.restart()

    def __del__(self):
        if self.vid is not None and self.vid.isOpened():
            self.vid.release()

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        return False, None

    def restart(self):
        self.vid = cv2.VideoCapture(self.VIDEO)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", self.VIDEO)
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
