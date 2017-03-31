class Dog():
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def describe(self):
        print("There is a "+ self.color + " dog!\n\nIt's name " + self.name +" It's "+ self.age +" years old!\n")

    def action(self):
        print("It's very cute!!")

mydog = Dog("guodong", "white", str(2))
mydog.describe()
