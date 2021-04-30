from tkinter import *
import RPi.GPIO as GPIO
import time
from morse_code import letters

window = Tk()
window.geometry("800x200")
window.title("Morse Code LED")
   

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(13,GPIO.OUT)

def buttonclicked(E1):
    print("The Letters: ", E1)
    for letter in E1.upper():
        time.sleep(2)
        mcode= letters[letter]
        print(mcode)
        for i in mcode:
            if i == "-":
                led(0.5)
            elif i == ".":
                led(0.2)
            elif i == "/":
                time.sleep(1)

def led(timedelay):
    GPIO.output(13,GPIO.HIGH)
    time.sleep(timedelay)
    GPIO.output(13,GPIO.LOW)
    time.sleep(0.5)
    
E1 = Entry(window, width = 50, fg="black")
E1.place(x=160, y= 70)
B5 = Button(window, text="ENTER", width= 20, bg="yellow", fg="black", command=lambda:buttonclicked(E1.get()))
B5.place(x=250, y= 100)

window.mainloop()