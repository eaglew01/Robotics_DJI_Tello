import tkinter as tk
import ttkbootstrap as ttk
from batteryCheck import battery_level
from batteryCheck import hoogte

#variabele scherm batterij
root = tk.Tk()
style = ttk.Style("superhero")
root.geometry("450x250+0+0")

#batterijmeter
ttk.Meter(
    metersize=180,
    padding=20,
    stripethickness=2,
    amountused=battery_level,
    subtext='battery level',
    textright='%',
    bootstyle='success',
    interactive=True
).grid(row=0, column=0)

#hoogtemeter
ttk.Meter(
    metersize=180,
    padding=20,
    stripethickness=2,
    amountused=hoogte,
    subtext='hoogte drone',
    textright='m',
    bootstyle='success',
    interactive=True
).grid(row=0, column=1)
root.mainloop()
