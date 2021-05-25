import requests
import RPi.GPIO as GPIO

ledPin = 12 # define ledPin
sensorPin = 11 # define sensorPin

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(ledPin, GPIO.OUT)
	GPIO.setup(sensorPin, GPIO.IN) # set sensorPin to INPUT mode

def loop():	
	while True:
		if GPIO.input(sensorPin)==GPIO.HIGH: 
			#GPIO.output(ledPin,GPIO.HIGH) # turn on led 
			print ('led turned on >>>')
		else :
			#GPIO.output(ledPin,GPIO.LOW) # turn off led 
			print ('led turned off <<<')

def destroy():
	GPIO.cleanup() # Release GPIO resource
# use PHYSICAL GPIO Numbering # set ledPin to OUTPUT mode

if __name__ == '__main__': # Program entrance 
print('Program is starting...')
setup()
try:
	loop()
except KeyboardInterrupt: # Press ctrl-c to end the program.
	destroy()