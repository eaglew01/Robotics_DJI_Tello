from djitellopy import tello
from time import sleep

myTello = tello.Tello()
myTello.connect()

print(myTello.get_battery())

myTello.takeoff()

myTello.send_rc_control(0, -50, 0, 0)
sleep(2)
myTello.send_rc_control(0, 0, 0, 0)
myTello.land()