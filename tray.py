from cProfile import label
from tkinter import *
import pystray
from PIL import Image, ImageTk
from pynotifier import Notification
import os

stream = os.popen('sensors')
output = stream.read().splitlines()
cores = []
for i in output:
    x = 0
    if output[i][4:] == "Core":
        cores[x] = output[i]
        x = x+1

for i in cores:
    print(cores[i][14:21])


#sends notification
def Notify():
    Notification(
        title='Hello There',
        description='General Kenobi',
        icon_path='ff.ico',
        urgency='normal'
    ).send()

#defines functions for button clicks on tray
def on_clicked(icon, item):
    if str(item) == "Open":
        icon.stop()
        win.after(0,win.deiconify())
    elif str(item) == "mess":
        Notify()
    elif str(item) == "Quit":
        icon.stop()
        win.destroy()

#function to hide window and create icon in system tray
def hide_window():
    win.withdraw()
    icon = pystray.Icon("CoreTemp", image, "CoreTemp", menu=pystray.Menu(pystray.MenuItem('Open', on_clicked,default=True,visible=False),
        pystray.MenuItem("Open", on_clicked),
        pystray.MenuItem("mess", on_clicked),
        pystray.MenuItem("Quit", on_clicked)
        ))

    #runs the icon in the tray
    icon.run()

#creates window
win=Tk()

#Gets icon for program
image = Image.open("ff.ico")
tkImage = ImageTk.PhotoImage(image)

#changes window header
win.iconphoto(True, tkImage)
win.title("Core Temperatures")
win.geometry("400x500")

#content of window
label1 = Label(win, text="abc")
label1.place(x=10,y=10)

#calls function to hide window on clicking close button
win.protocol('WM_DELETE_WINDOW', hide_window)

#runs the window
win.mainloop()
# nohup mypythonprog &

