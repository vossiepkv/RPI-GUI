##imports 
from tkinter import * 
import tkinter.font 
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

##Hardware definition 

led_red = led(17) ## board pin 11
led_blue = led(27) ## board pin 13
led_green = led(22) ## board pin 15

##