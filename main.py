import time
import sys
import os
import random


#1_tables =





	
		



def main():
	victim_list = []
	victim_counter = 0
	print "This project is still in development"
	#Work on the main loop here.
	first_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
	for i in range (1,13):
		victim_list.append(first_digits[victim_counter])
		victim_list[victim_counter] = first_digits[victim_counter]
		victim_counter += 1
	#Victim list is also 1 through 12
	#TIME TO MULLTIPLY
	answer_list = []
	#for x in first_digits:
		
		
	
	

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
	
