##imports 
from tkinter import * 
import tkinter.font 
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

##Hardware definition  

ledRed = led(17) ## board pin 11
ledBlue = led(27) ## board pin 13
ledGreen = led(22) ## board pin 15

##GUI Definitions 
win = Tk()
win.title("Multi LED Toggler")
myfont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

##Event Functions
def redToggle():
  if ledRed.is_lit:
    ledRed.off()
    ledRedButton["text"] = "Turn  LED On"
  else:
    ledRed.on()
    ledRedButton["text"] = "Turn Red LED Off"

def blueToggle():
  if ledBlue.is_lit:
    ledBlue.off()
    ledBlueButton["text"] = "Turn Blue LED On"
  else:
    ledRed.on()
    ledBlueButton["text"] = "Turn Blue LED Off"

def greenToggle():
  if ledGreen.is_lit:
    ledGreen.off()
    ledGreenButton["text"] = "Turn Green LED On"
  else:
    ledGreen.on()
    ledGreenButton["text"] = "Turn Green LED Off"

def close():
  RPi.GPIO.cleanup()
  win.destroy()


##Widgets 

ledRedButton = Button(win, text = 'Turn Red LED On', font = myfont, command = redToggle, bg = 'bisque2', height = 1, width = 24)
ledRedButton.grid(row=0, column=1)

ledBlueButton = Button(win, text = 'Turn Blue LED On', font = myfont, command = blueToggle, bg = 'bisque2', height = 1, width = 24)
ledBlueButton.grid(row=0, column=2)

ledGreenButton = Button(win, text = 'Turn Green LED On', font = myfont, command = greenToggle, bg = 'bisque2', height = 1, width = 24)
ledGreenButton.grid(row=0, column=3)
  

##Exit button
exitButton = Button(win, text = 'Exit', font = myfont, command = close, bg = 'red', height = 1, width = 6)
exitButton.grid(row= 1, column=3)

win.protocol("WM_DELETE_WINDOW", close) 

win.mainloop()
