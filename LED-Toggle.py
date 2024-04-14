##imports 
from tkinter import * 
import tkinter.font 
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

##Hardware definition  

ledRed = LED(18) ## board pin 11
ledBlue = LED(12) ## board pin 13
ledGreen = LED(13) ## board pin 15

##GUI Definitions 
win = Tk()
win.title("Multi LED Toggler")
myfont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")
myFontTitle = tkinter.font.Font(family = 'Helvetica', size = 22, weight = "bold")


## Refactoring potentials:
## can create a general function that handles the toggling of any given LED
## can do Dictionary Mapping for LEDs and Buttons

##Event Functions
def redToggle():
    if ledRed.is_lit:
        ledRed.off()
        ledRedButton["text"] = "Turn Red LED On"
        ledRedButton["bg"] = "bisque2"  # Neutral color when off
    else:
        ledRed.on()
        ledBlue.off()
        ledGreen.off()
        ledRedButton["text"] = "Turn Red LED Off"
        ledRedButton["bg"] = "red"  # Red when LED is on
        ledBlueButton["text"] = "Turn Blue LED On"
        ledBlueButton["bg"] = "bisque2"
        ledGreenButton["text"] = "Turn Green LED On"
        ledGreenButton["bg"] = "bisque2"

def blueToggle():
    if ledBlue.is_lit:
        ledBlue.off()
        ledBlueButton["text"] = "Turn Blue LED On"
        ledBlueButton["bg"] = "bisque2"
    else:
        ledBlue.on()
        ledRed.off()
        ledGreen.off()
        ledBlueButton["text"] = "Turn Blue LED Off"
        ledBlueButton["bg"] = "blue"  # Blue when LED is on
        ledRedButton["text"] = "Turn Red LED On"
        ledRedButton["bg"] = "bisque2"
        ledGreenButton["text"] = "Turn Green LED On"
        ledGreenButton["bg"] = "bisque2"

def greenToggle():
    if ledGreen.is_lit:
        ledGreen.off()
        ledGreenButton["text"] = "Turn Green LED On"
        ledGreenButton["bg"] = "bisque2"
    else:
        ledGreen.on()
        ledBlue.off()
        ledRed.off()
        ledGreenButton["text"] = "Turn Green LED Off"
        ledGreenButton["bg"] = "green"  # Green when LED is on
        ledRedButton["text"] = "Turn Red LED On"
        ledRedButton["bg"] = "bisque2"
        ledBlueButton["text"] = "Turn Blue LED On"
        ledBlueButton["bg"] = "bisque2"


def close():
  RPi.GPIO.cleanup()
  win.destroy()


##Widgets 

titleText = Label(win, text = "Multi-Color LED Toggler", font = myFontTitle)
titleText.grid(row=0, column=2, pady=10)

ledRedButton = Button(win, text = 'Turn Red LED On', font = myfont, command = redToggle, bg = 'bisque2', height = 1, width = 24)
ledRedButton.grid(row=2, column=1)

ledBlueButton = Button(win, text = 'Turn Blue LED On', font = myfont, command = blueToggle, bg = 'bisque2', height = 1, width = 24)
ledBlueButton.grid(row=2, column=2)

ledGreenButton = Button(win, text = 'Turn Green LED On', font = myfont, command = greenToggle, bg = 'bisque2', height = 1, width = 24)
ledGreenButton.grid(row=2, column=3)
  

##Exit button
exitButton = Button(win, text = 'Exit', font = myfont, command = close, bg = 'red', height = 1, width = 6)
exitButton.grid(row= 4, column=3, pady=20)

win.protocol("WM_DELETE_WINDOW", close) 

win.mainloop()
