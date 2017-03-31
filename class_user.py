#/usr/bin/python3
class User():
    def __init__(self, first_name, last_name, user_message="he is a user"):
        self.first_name = first_name
        self.last_name = last_name
        self.user_message = user_message

    def describe_user(self):
        print("Your name is "+ self.first_name +' '+ self.last_name)
        print( self.user_message )

    def greet_user(self):
        print("Holle , "+ self.first_name + ' ' + self.last_name +' !')

while True:
    f_n="\nWhat's your first name? "
    f_n += "\n(Enter q to exit!!)"
    f_name=input(f_n)
    if f_name == 'q':
        break

    l_n = "\nWhat's your last name? "
    l_n += "\n(Enter q to exit!!)"
    l_name=input(l_n)
    if l_name == 'q':
        break

    mg = "\nPlease geive me your describe: "
    mg += "\n(Enter q to exit!!)\n"
    message=input(mg)
    if message == 'q':
        break
    elif message == " ":
        message="he is a user!"

    Hello = User(f_name,l_name,message)
    Hello.describe_user()
    Hello.greet_user()
