from djitellopy import tello
import cv2
myTello = tello.Tello()
myTello.connect()
print(myTello.get_battery())

myTello.streamon()

while True:
    img = myTello.get_frame_read().frame
    cv2.imshow("telloVideo", img)
    cv2.waitKey(1)
