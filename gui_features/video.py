'''If there are errors with running this file, check ffmpeg is
correctly installed'''

import cv2


def preview_webcam():
    ''' Function to demo video capture object'''

    cap = cv2.VideoCapture(0)  # device index 0 is first webcam connected

    while True:
        # frame by frame capture
        ret, frame = cap.read()  # ret-bool returned when a frame is read correctly

        # convert to greyscale
        gs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # show frame and quit when q is pressed
        cv2.imshow('frame', gs)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # release capture when done
    cap.release()
    cv2.destroyAllWindows()


def play_video():
    ''' Function to demo playing a video from a file'''

    vid_path = "../media/drop.avi"
    vid = cv2.VideoCapture(vid_path)

    while(vid.isOpened()):
        ret, frame = vid.read()
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    play_video()