import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
greenpins = 8
GPIO.setup(greenpins, GPIO.OUT)
print("LED on")
GPIO.output(greenpins, GPIO.HIGH)
sleep(5)#LED will be off after 5seconds
print("LED off")
GPIO.output(greenpins, GPIO.LOW)