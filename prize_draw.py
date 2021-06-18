import csv
import random 
import os
from survey_config import *

print "The current working directory is", os.getcwd()

CSV_DIR = os.path.join(os.getcwd(), CSV_FILE)
OUTPUT_DIR = os.path.join(os.getcwd(), OUTPUT_FILE)

while True:
	print("Welcome to Albert's Prize Drawing Programme.\n")

	# Input the number of winners or prizes for this draw
	N = raw_input("How many prizes do you want to offer? \n")

	# Reads the .csv file from Qualtrics
	ERfile = open(CSV_DIR, 'rb')

	# Converting the .csv file into a readable format
	# It should be readable like a matrix, should be able to call entries based on row and columns
	ERdata = csv.reader(ERfile, delimiter=',')
	ERtable = [row for row in ERdata]

	# Removing the header from the .csv file
	ERtable = ERtable[INDEX_HEADER:]

	# Randomly select the people to get the prize
	Winners = random.sample(ERtable, int(N))

	# Designates winner places 1 - N (number the user input)
	Places = range(1, int(N)+1)
	
	# Results are printed onto an output file
	Results = open(OUTPUT_DIR, 'w')

	for x in Places: 
		print 'Winner %d is...%s' %(x, Winners[x-1][INDEX_HEADER_NAME])
		print >>Results, 'Winner %d is...%s' %(x, Winners[x-1])

	Results.close()

	Answer = raw_input("Run again? (y/n): ")
	if Answer == 'n':
		print("Goodbye")
		False
		break
	else:
		continue