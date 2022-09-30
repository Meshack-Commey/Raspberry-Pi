import RPi.GPIO as g
import time
g.setwarnings(False)

print("Welcome to Morse Code \n")
print("Aim: To blink SOS with LED continuosly \n")

g.setmode(g.BOARD)#BOARD mode
greenpins = 8 #number of datapins to give output
g.setup(8, g.OUT)#setup state: to give OUT data to the BOARD

def sayS():
 for i in range(3):
  print("S on")
  g.output(greenpins, g.HIGH)#set LED on
  time.sleep(0.2)#at 0.2sec
  print("S off")
  g.output(greenpins, g.LOW)
  time.sleep(0.2)#at 0.2seconds

def sayO():
 for i in range(3):
  print("O on")
  g.output(greenpins, g.HIGH)
  time.sleep(0.6)
  print("O off")
  g.output(greenpins, g.LOW)
  time.sleep(0.2)


def sayS():
 for i in range(3):
  print("S on")
  g.output(greenpins, g.HIGH)#set LED on
  time.sleep(0.2)#
  print("S off")
  g.output(greenpins, g.LOW)#set LED off
  time.sleep(0.2)#at 0.2seconds

while True:
 sayS()
 time.sleep(0.3)
 sayO()
 time.sleep(0.3)
 sayS()
 time.sleep(0.5)