import cv2
import time

video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None

while True:
    # Set the camera
    check, frame = video.read()
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey_frame_gau = cv2.GaussianBlur(grey_frame, (21, 21), 0)

    # Check if the first image captured by the camera so to store it
    if first_frame is None:
        first_frame = grey_frame_gau

    # Check if the current image is the same as the first image
    delta_frame = cv2.absdiff(first_frame, grey_frame)
    cv2.imshow("My video", delta_frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()
