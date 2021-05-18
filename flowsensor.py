#Created by Vincent Munyalo
# Connection: Input -> 4.7k resistor -> RPi pin 13 + 10k resistor -> Gnd
import RPi.GPIO as GPIO
import time, sys

GPIO.setmode(GPIO.BOARD)
inpt = 13
GPIO.setup(inpt, GPIO.IN)
rate_count = 0
total_count = 0
minutes = 0
constant = 0.10
time_new = 0.0

print("Displaying average fluid flow ")
print("Control C to exit")

while True:
	time_new = time.time() + 60
	rate_count = 0
	while time.time() <= time_new:
		if GPIO.input(inpt) != 0:
			rate_count += 1
			total_count += 1
		try:
			print(GPIO.input(inpt), end = '')
		except KeyboardInterrupt:
			print('\nExiting nicely!')
			GPIO.cleanup()
			sys.exit()

	minutes += 1
	print('\nLiters / min ', round(rate_count * constant, 4))
	print('Time (min & clock)', minutes, '\t', time.asctime(time))

GPIO.cleanup()
print('Done Mothafuka!!')
