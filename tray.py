from cProfile import label
from tkinter import *
import pystray
from PIL import Image, ImageTk
from pynotifier import Notification
import os
import threading
from time import sleep

#function to call sensors and check temperature
cores = []
def checkTemp():
    stream = os.popen('sensors')
    output = stream.read()
    out = output.splitlines()
    for i in out:
        if i[:4] == "Core":
            cores.append(i)

#sends notification
def Notify(temp):
    Notification(
        title='High Temperature',
        description=temp,
        icon_path='ff.ico',
        urgency='normal'
    ).send()

#defines functions for button clicks on tray
def on_clicked(icon, item):
    if str(item) == "Open":
        icon.stop()
        win.after(0,win.deiconify())
    elif str(item) == "Quit":
        icon.stop()
        win.destroy()

#function to hide window and create icon in system tray
def hide_window():
    win.withdraw()

def loopTray():
    icon = pystray.Icon("CoreTemp", image, "CoreTemp", menu=pystray.Menu(pystray.MenuItem('Open', on_clicked,default=True,visible=False),
        pystray.MenuItem("Open", on_clicked),
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
label1 = Label(win, text="Cores:")
label1.place(x=10,y=10)

label2 = Label(win, text="Interval per minutes:")
label2.place(x=10,y=300)

Lb1 = Listbox(win)
Lb1.pack(ipady=10)

txt1 = Text(win, height=1,width=10)
txt1.place(x=122,y=300)

#Checks the temperature on the cores and inserts the values
def updateValues():
    checkTemp()
    ind1 = 0
    for i in cores:
            Lb1.insert(ind1, i[14:21])
            ind1 = ind1+1
    while True:
        checkTemp()
        if int(cores[0][14:21]) > 80:
            Notify(cores[0][14:21])
        sleepInt = txt1.get("1.0","end-1c")
        try:
            sleepInt = int(sleepInt)
        except:
            sleepInt = 300
        sleep(sleepInt)
        ind2 = 0
        for i in cores:
            Lb1.delete(ind2)
            Lb1.insert(ind2, i[14:21])
            ind2 = ind2+1

#calls function to hide window on clicking close button
win.protocol('WM_DELETE_WINDOW', hide_window)

thValues = threading.Thread(target=updateValues,daemon=True).start()
thTray = threading.Thread(target=loopTray,daemon=True).start()
#runs the window
win.mainloop()