from djitellopy import tello
from time import sleep

myTello = tello.Tello()
myTello.connect()

print(myTello.get_battery())

myTello.takeoff()
myTello.send_rc_control(0, 0, 0, 0)
sleep(2)
#forward
myTello.send_rc_control(0, 50, 0, 0)
sleep(2)

#right
myTello.send_rc_control(50, 0, 0, 0)
sleep(2)

#flip
#myTello.flip("r")
#myTello.send_rc_control(0, 0, 0, 0)
#sleep(1)

#back
myTello.send_rc_control(0, -50, 0, 0)
sleep(2)

#left
myTello.send_rc_control(-50, 0, 0, 0)
sleep(2)

#land
myTello.send_rc_control(0, 0, 0, 0)
myTello.land()
