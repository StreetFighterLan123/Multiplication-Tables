import time
import sys
import os
import random

tables = {}


def main():
	print "This project is still in development"
	#Work on the main loop here.
	
	

answer_choice = raw_input("Launch Multiplication Tables?")
if answer_choice.lower() == "yes" or answer_choice.lower() == "y":
	print "Starting up Multiplication Tables..."
	time.sleep(1)
	main()
elif answer_choice.lower() == "no" or answer_choice.lower() == "n":
	print "Okay"
	time.sleep(0.5)
	sys.exit()
else:
	print "That is not a valid answer. Goodbye!"
	time.sleep(1)
	sys.exit()
	
