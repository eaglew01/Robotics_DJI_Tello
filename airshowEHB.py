from djitellopy import tello
from time import sleep

myTello = tello.Tello()
myTello.connect()

print(myTello.get_battery())

#takeoff-auto
myTello.takeoff()

#create letter E
myTello.send_rc_control(0, 0, 60, 0)
sleep(2)

myTello.send_rc_control(-20, 0, 0, 0)
sleep(2)
myTello.send_rc_control(20, 0, 0, 0)
sleep(2)

myTello.send_rc_control(0, 0, -30, 0)
sleep(2)

myTello.send_rc_control(-20, 0, 0, 0)
sleep(2)
myTello.send_rc_control(20, 0, 0, 0)
sleep(2)

myTello.send_rc_control(0, 0, -30, 0)
sleep(2)

myTello.send_rc_control(-20, 0, 0, 0)
sleep(2)
myTello.send_rc_control(20, 0, 0, 0)
sleep(2)

#create letter H
myTello.send_rc_control(-20, 0, 0, 0)
sleep(2)
myTello.send_rc_control(0, 0, 50, 0)
sleep(2)
myTello.send_rc_control(0, 0, -30, 0)
sleep(2)
myTello.send_rc_control(-20, 0, 0, 0)
sleep(2)
myTello.send_rc_control(0, 0, 30, 0)
sleep(2)
myTello.send_rc_control(0, 0, -60, 0)
sleep(2)


#create letter B
myTello.send_rc_control(0, 0, 60, 0)
sleep(2)
myTello.send_rc_control(-20, 0, -20, 0)
sleep(2)
myTello.send_rc_control(20, 0, -20, 0)
sleep(2)
myTello.send_rc_control(-20, 0, -20, 0)
sleep(2)
myTello.send_rc_control(20, 0, -20, 0)
sleep(2)

#land-auto
myTello.send_rc_control(0, 0, 0, 0)
myTello.land()
