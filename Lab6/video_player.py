import cv2

class VideoCommercialPlayer:
    """ Simple Video Player with Start/Stop functionality """
    # States of video player
    is_paused = True
    is_video_opened = False
    video_stream = None

    def __init__(self):
        self.is_video_opened = self.__openVideoFile()
        self.is_paused = True

    def __openVideoFile(self):
        self.video_stream = cv2.VideoCapture('commercials.mp4')

        # check if the video capture is open
        if not self.video_stream.isOpened():
            print("Error Opening Video Stream Or File")
            return False
        else:
            return True

    def displayVideo(self):
        print('is_opened: ' + str(self.is_video_opened) + ' is_paused:' + str(self.is_paused))
        if self.is_video_opened and not self.is_paused:
            ret, frame = self.video_stream.read()

            if ret == True:
                cv2.resizeWindow('frame', 600, 600)
                cv2.imshow('frame', frame)

    def pauseVideo(self):
        self.is_paused = True

    def playVideo(self):
        self.is_paused = False
