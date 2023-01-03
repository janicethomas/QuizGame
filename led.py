#ground(pin 9) - led(green) - resistor(330ohms) - GPIO17(pin 11)
#ground(pin 9) - led(red) - resistor(330ohms) - GPIO27(pin 13)
import RPi.GPIO as GPIO
import time

GREEN = 17
RED = 27

class ledBlink:
    def __init__(self):
        pass
       
    def blink_green(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GREEN, GPIO.OUT)
        GPIO.output(GREEN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(GREEN, GPIO.LOW)
        time.sleep(0.5)
        GPIO.cleanup()

    def blink_red(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RED, GPIO.OUT)
        GPIO.output(RED, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(RED, GPIO.LOW)
        time.sleep(0.5)
        GPIO.cleanup()

    def score_blink(self, n):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RED, GPIO.OUT)
        GPIO.setup(GREEN, GPIO.OUT)

        for i in range(n):
            GPIO.output(RED, GPIO.HIGH)
            GPIO.output(GREEN, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(RED, GPIO.LOW)
            GPIO.output(GREEN, GPIO.LOW)
            time.sleep(0.5)
            
        GPIO.cleanup()

# led = ledBlink()
# led.blink_green()
