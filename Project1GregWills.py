#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 17:15:08 2018

@author: gjwills
"""

# Greg Wills
# Assignment 1
# Computer Science 010 - Intro to IT
# Professor Amy Gates

import sys

def main():
	print("\nWelcome to the Advanced Baseball Offensive Statistic caculator.")
	menu()

def menu():

	ops = 0
	babip = 0
	iso = 0
	rc = 0

	while True:
		test = False
		print("---------------------------------------------------------------")
		print("Here are your options...")
		print("OPS   - On-base Plus Slugging Percentage")
		print("BABIP - Batting Average on Balls in Play")
		print("ISO   - Isolated Power")
		print("RC    - Runs Created")
		print("Sum   - For Summmary of Statistics Calculated")
		print("quit  - if you want to quit the program")
		print("----------------------------------------")

		userInput = input("Please enter your choice from the menu above: ")

		if userInput.lower() == "ops":
			ops = OPS()
		elif userInput.lower() == "babip":
			babip = BABIP()
		elif userInput.lower() == "iso":
			iso = ISO()
		elif userInput.lower() == "rc":
			rc = RC()
		elif userInput.lower() == "sum":
			summary(ops,babip,iso,rc)
		elif userInput == "quit":
			print("Thank you for using my program. Goodbye!")
			sys.exit()
		else:
			print("Please enter a valid statistic abbreviation or type quit to exit...")
			test = True 
		# nested if statements
		if test == False:
			while True:
				cont = input("Do you want to calculate another statistic? (Y/N) ")
				if cont.lower() == 'n':
					print("Thank you for using my program. Goodbye!")
					sys.exit()
				elif cont.lower() == 'y':
					break
				else:
					print("Please enter a Y for yes or a N for no...")


def OPS():
	ops = 0.0

	hits = int(input("How many hits? "))
	walks = int(input("How many walks? "))
	hbp = int(input("How many hit by pitches? "))
	atbats = int(input("How many at-bats? "))
	sacflies = int(input("How many sacrafice flies? "))
	totalBases = int(input("How many total bases? "))

	numerator = (atbats * (hits+walks+hbp) + totalBases * (atbats+walks+sacflies+hbp))
	denominator = (atbats * (atbats+walks+sacflies+hbp))
	if denominator == 0:
		print("Make sure your denominator is not 0")
	ops = numerator/denominator

	print("The OPS of your player is: ")
	print(round(ops,3)) 

	if ops >= 1:
		print("This is great!")
	elif ops <1 and ops >= .9:
		print("This is pretty good.")
	elif ops <.9 and ops >=.8:
		print("This is above average")
	elif ops <.8 and ops >=.71:
		print("This is average")
	elif ops <.71 and ops >= .67:
		print("This is below average")
	elif ops <.67 and ops >= .6:
		print("This is poor")
	elif ops <.6 and ops >= .57:
		print("This is awful")
	else:
		print("This is a terrible ops, think about sending this player down. ")


	return ops 

def BABIP():
	babip = 0.0
	hits = int(input("How many hits? "))
	hrs = int(input("How many homeruns? "))
	atbats = int(input("How many at-bats? "))
	ks = int(input("How many strikeouts? "))
	sacflies = int(input("How many sac flies? "))

	numerator = hits -hrs
	denominator = atbats - ks - hrs +sacflies
	if denominator == 0:
		print("Make sure your denominator is not 0")

	babip = numerator/denominator

	print("The BABIP of your player is: ")
	print(round(babip,3))

	return babip

def ISO():
	iso = 0.0

	doubles = int(input("How many doubles? "))
	triples = int(input("How many triples? "))
	hrs = int(input("How many homeruns? "))
	atbats = int(input("How many at-bats? "))

	numerator = doubles + 2*triples + 3*hrs

	iso = numerator/atbats

	print("The ISO of your player is: ")
	print(round(iso,3))

	if iso >= 0.25:
		print("This is great!")
	elif iso >= 0.2:
		print("This is good.")
	elif iso >= 0.17:
		print("This is above average.")
	elif iso >= 0.14:
		print("This is average")
	elif iso <= 0.12:
		print("This is below average")
	elif iso <= 0.08:
		print("Get this player of of your team!")
	else:
		print("Check to make sure you entered you statistics correctly.")

	return iso 

def RC():
	rc = 0.0

	hits = int(input("How many hits? "))
	walks = int(input("How many walks? "))
	totalBases = int(input("How many total bases? "))
	atbats = int(input("How many at-bats? "))

	numerator = (hits + walks) * totalBases
	denominator = atbats + walks

	rc = numerator/denominator

	print("The RC of your player is: ")
	print(round(rc,3))

	return rc 

def summary(ops,babip,iso,rc):

	# For/in loop implementation

	list = [ops,babip,iso,rc]

	# print(" OPS       BABIP      ISO     RC ")
	print("%6s" % "OPS", end=" ")
	print("%6s" % "BABIP", end=" ")
	print("%6s" % "ISO", end=" ")
	print("%6s" % "RC")
	print("---------------------------")

	for item in list:
		# print("  ", round(item,3), end="     ")
		print("%6s" % round(item,3), end= " ")
		#	print("Error in summary function")
	print(" ")

main()
