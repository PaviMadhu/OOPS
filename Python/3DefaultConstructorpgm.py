class MyShop:
 
    # default constructor
    def __init__(self):
        self.shopname = "Brownies and Bakes"
 
    # a method for printing data members
    def print_shopname(self):
        print(self.shopname)
 
 
# creating object of the class
obj = MyShop()
print(obj)
# calling the instance method using the object obj
obj.print_shopname()

#Quiz Time
obj.shopname="OOKOO Brownies and Bakes"
obj.print_shopname()