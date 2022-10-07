# Python3 program to
# demonstrate instantiating
# a class and creation of objects
#Quiz 1 - Whats the difference you can see here from previous program?
 
class Dog:
 
    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"
 
    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)
 
 
# Driver code
# Object instantiation
obj1 = Dog()
 
# Accessing class attributes
# and method through objects
print(obj1.attr1)
obj1.fun()