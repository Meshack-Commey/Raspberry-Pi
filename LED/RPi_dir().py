#Raspberry Pi Directories Readings

import RPi as R
import RPi.GPIO as G

d = dir()

r = dir(R)
g = dir(R.GPIO)
#RPi.GPIO modes
gbcm = dir(G.BCM)
gboard = dir(G.BOARD)

print(r)
print("\n \n {}".format("General Pins Input Output (GPIO) \n "))
print(g)
print("\n \n GPIO.BCM \n \n")
print(gbcm)
print("\n \n GPIO.BOARD \n \n")
print(gboard)

