#!/usr/bin/python3
asks="Give me a message,I will replace print for you: "
asks +="\n(Enter q exit !)"
while True:
	message=input(asks)
	if message == 'q':
		break
	else:
		print("Thank you! You input "+message)
		

