#!/usr/bin/python3
users=[]
zhuce=input("Do you want sign up my web? if you want ,please input Y　else input N: ")

while zhuce == 'Y':
	name=input("Input your name: ")
	if name == 'exit':
		break
	else:
		users.append(name)
print(users)


