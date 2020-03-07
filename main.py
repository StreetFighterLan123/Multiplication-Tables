import time
import sys
import os
import random

#Might change this to seperate tables or automate this idk...
tables = {

#1 table.
"1x1" : str(1*1)
"1x2" : str(1*2)
"1x3" : str(1*3)
"1x4" : str(1*4)
"1x5" : str(1*5)
"1x6" : str(1*6)
"1x7" : str(1*7)
"1x8" : str(1*8)
"1x9" : str(1*9)
"1x10" : str(1*10)
"1x11" : str(1*11)
"1x12" : str(1*12)

#2 table.
"2x1" : str(2*1)
"2x2" : str(2*2)
"2x3" : str(2*3)
"2x4" : str(2*4)
"2x5" : str(2*5)
"2x6" : str(2*6)
"2x7" : str(2*7)
"2x8" : str(2*8)
"2x9" : str(2*9)
"2x10" : str(2*10)
"2x11" : str(2*11)
"2x12" : str(2*12)

#3 table.
"3x1" : str(3*1)
"3x2" : str(3*2)
"3x3" : str(3*3)
"3x4" : str(3*4)
"3x5" : str(3*5)
"3x6" : str(3*6)
"3x7" : str(3*7)
"3x8" : str(3*8)
"3x9" : str(3*9)
"3x10" : str(3*10)
"3x11" : str(3*11)
"3x12" : str(3*12)

#4 table.
"4x1" : str(4*1)
"4x2" : str(4*2)
"4x3" : str(4*3)
"4x4" : str(4*4)
"4x5" : str(4*5)
"4x6" : str(4*6)
"4x7" : str(4*7)
"4x8" : str(4*8)
"4x9" : str(4*9)
"4x10" : str(4*10)
"4x11" : str(4*11)
"4x12" : str(4*12)

#5 table.
"5x1" : str(5*1)
"5x2" : str(5*2)
"5x3" : str(5*3)
"5x4" : str(5*4)
"5x5" : str(5*5)
"5x6" : str(5*6)
"5x7" : str(5*7)
"5x8" : str(5*8)
"5x9" : str(5*9)
"5x10" : str(5*10)
"5x11" : str(5*11)
"5x12" : str(5*12)

#6 table.
"6x1" : str(6*1)
"6x2" : str(6*2)
"6x3" : str(6*3)
"6x4" : str(6*4)
"6x5" : str(6*5)
"6x6" : str(6*6)
"6x7" : str(6*7)
"6x8" : str(6*8)
"6x9" : str(6*9)
"6x10" : str(6*10)
"6x11" : str(6*11)
"6x12" : str(6*12)

#7 table.
"7x1" : str(7*1)
"7x2" : str(7*2)
"7x3" : str(7*3)
"7x4" : str(7*4)
"7x5" : str(7*5)
"7x6" : str(7*6)
"7x7" : str(7*7)
"7x8" : str(7*8)
"7x9" : str(7*9)
"7x10" : str(7*10)
"7x11" : str(7*11)
"7x12" : str(7*12)

#8 table.
"8x1" : str(8*1)
"8x2" : str(8*2)
"8x3" : str(8*3)
"8x4" : str(8*4)
"8x5" : str(8*5)
"8x6" : str(8*6)
"8x7" : str(8*7)
"8x8" : str(8*8)
"8x9" : str(8*9)
"8x10" : str(8*10)
"8x11" : str(8*11)
"8x12" : str(8*12)

#9 table.
"9x1" : str(9*1)
"9x2" : str(9*2)
"9x3" : str(9*3)
"9x4" : str(9*4)
"9x5" : str(9*5)
"9x6" : str(9*6)
"9x7" : str(9*7)
"9x8" : str(9*8)
"9x9" : str(9*9)
"9x10" : str(9*10)
"9x11" : str(9*11)
"9x12" : str(9*12)

#10 table.
"10x1" : str(10*1)
"10x2" : str(10*2)
"10x3" : str(10*3)
"10x4" : str(10*4)
"10x5" : str(10*5)
"10x6" : str(10*6)
"10x7" : str(10*7)
"10x8" : str(10*8)
"10x9" : str(10*9)
"10x10" : str(10*10)
"10x11" : str(10*11)
"10x12" : str(10*12)

#11 table.
"11x1" : str(11*1)
"11x2" : str(11*2)
"11x3" : str(11*3)
"11x4" : str(11*4)
"11x5" : str(11*5)
"11x6" : str(11*6)
"11x7" : str(11*7)
"11x8" : str(11*8)
"11x9" : str(11*9)
"11x10" : str(11*10)
"11x11" : str(11*11)
"11x12" : str(11*12)

#12 table.
"12x1" : str(12*1)
"12x2" : str(12*2)
"12x3" : str(12*3)
"12x4" : str(12*4)
"12x5" : str(12*5)
"12x6" : str(12*6)
"12x7" : str(12*7)
"12x8" : str(12*8)
"12x9" : str(12*9)
"12x10" : str(12*10)
"12x11" : str(12*11)
"12x12" : str(12*12)

}
# ^^I could've done a "for x in range (blah blah blah)" and append 
#it to a dictionary but I have a lot of time to waste right now.

def main():
	print "This project is still in development"
