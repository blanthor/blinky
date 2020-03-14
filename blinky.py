#coding: utf-8
import RPi.GPIO as GPIO
import time

LedPin = 11 #GPIO pin number 11 on the Pi

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.output(LedPin, GPIO.HIGH)

def loop():
    while True:
        print ('´...led on´')
        GPIO.output(LedPin, GPIO.LOW)
        time.sleep(1.5)
        print ('´...led off´')
        GPIO.output(LedPin, GPIO.HIGH)
        time.sleep(0.5)

def destroy():
        GPIO.output(LedPin, GPIO.HIGH)
        GPIO.cleanup()

if __name__ == '__main__':
        setup()
        try:
            loop()
        except KeyboardInterrupt:
            destroy()
