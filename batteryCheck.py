from djitellopy import tello
from time import sleep

#variabele DJI TELLO
myTello = tello.Tello()
myTello.connect()

#check batterij
battery_level = myTello.get_battery()
#(battery_level)

#check hoogte
hoogte = myTello.get_height()
#print(hoogte)

# while True:
#     # check batterij
#     battery_level = myTello.get_battery()
#     # (battery_level)
#
#     # check hoogte
#     hoogte = myTello.get_height()
#     # print(hoogte)
#     sleep(5)