#/usr/bin/python3
class Restau():
    """docstring for ."""
    def __init__(self, restau_name, restau_type):
        self.restau_name = restau_name
        self.restau_type = restau_type

    def desc_restau(self):
        print("\nThe name is "+ self.restau_name )
        print("\nThe type is "+ self.restau_type )

    def open_restau(self):
        print("\nThe store is running!")


while True:
    store_name=input("Please input your store name,input 'q' to exit: ")
    if store_name == 'q':
        break
    store_type=input("Pleasr input your store type,input 'q' to exit: ")
    if store_type == 'q':
        break
    my_store = Restau( store_name.title(), store_type.title() )
    print(my_store.desc_restau())
    print(my_store.open_restau())
