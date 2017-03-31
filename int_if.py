#!/usr/bin/python3
age=input("How old are you? ")
age=int(age)

if age > 18:
	print("You not a kids")
else:
	print("\nYou are a kids")

number=input("\nPlease enter a number? ")
number=int(number)

if number%2 == 0:
	print("\n"+str(number) +" is a even!")
else:
	print("\n"+str(number) +" is a odd!")
