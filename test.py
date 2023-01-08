from tkinter import *
from tkinter import ttk
import psutil
import threading
import os
from tkinter import messagebox
from batteryCheck import battery_level

window = Tk()
window.title("My Power Management")
window.geometry("300x200")

ticking = False
threadRunning = True


def getBatteryInfo():
    global percentBar
    global plugStateVar
    global chargePercentVar
    global threadRunning

    if (threadRunning):
        t = threading.Timer(1.0, lambda: getBatteryInfo())
        t.start()
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = battery_level

        if plugged == True:
            plugStateVar.set("plugged")
        else:
            plugStateVar.set("Unplugged")

        percentBar["value"] = percent
        chargePercentVar.set(percent)

def on_closing():
    global window
    global threadRunning

    if messagebox.askokcancel("Quite", "Do you want to quit?"):
        threadRunning = False
        window.destroy()


plugStateVar = StringVar()
plugStateVar.set("Unplugged")
chargePercentVar = StringVar()
chargePercentVar.set(0)
titleLabel = Label(window, text="Battery Info")
titleLabel.pack()

percentBar = ttk.Progressbar(window, length=200, orient="horizontal", mode="determinate")
percentBar.pack()
percentBar["maximum"] = 100
percentBar["value"] = 0

plugStateLabel = Label(window, textvariable=plugStateVar)
plugStateLabel.pack()

chargePercentLabel = Label(window, textvariable=chargePercentVar)
chargePercentLabel.pack()

getBatteryInfo()
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()