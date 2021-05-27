import requests
import RPi.GPIO as GPIO
import time
import tinytuya

sensorPin = 11 # define sensorPin

livroom = tinytuya.OutletDevice('eb0e2c8010a4d16a9cs5xt', '192.168.2.242', '1fbc6ff66d77f13d')
livroom.set_version(3.3)



def setup():
	GPIO.setmode(GPIO.BOARD)
	#GPIO.setup(ledPin, GPIO.OUT)
	GPIO.setup(sensorPin, GPIO.IN) # set sensorPin to INPUT mode
	#h = lgpio.gpiochip_open(0)
	#lg.gpio_claim_input(h, sensorPin)

def loop():	
	while True:
		if GPIO.input(sensorPin) == GPIO.HIGH: 
			#GPIO.output(ledPin,GPIO.HIGH) # turn on led 
			print ('led turned on >>>')
			livroom.turn_on()
			time.sleep(10)
		else :
			#GPIO.output(ledPin,GPIO.LOW) # turn off led 
			print ('led turned off <<<')
			livroom.turn_off()

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