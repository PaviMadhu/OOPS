class House(): #######Class creation
    housetype='Appartment'
    def __init__(self, bhk, color): #######Constructor
         self.color = color
         self.bhk = bhk
    def cost(self,INR):   ###Methodcreation
        self.a=100
        self.INR=INR
        print(self.color,"House cost is",self.INR,self.a)
        self.housetype='Lol' #Classvariable accessing through method
    def costmodified(self,INR):   ###Methodcreation
        self.INR=INR
        print(self.housetype)

bluehouse = House(4, "blue") ########Object creation
redhouse = House(2, "red")
print ("House colour: ",bluehouse.color) #########Printing Instance variable 
print ("House colour: ",redhouse.color)
print("************************")
print("Blue house type is ",bluehouse.housetype) #########Printing Class variable
print("Red house type is ", redhouse.housetype) ##########Printing Class variable
print("************************")
bluehouse.costmodified("00000000")
bluehouse.cost("2 Lakhs")
redhouse.cost("1 Lakh")
bluehouse.costmodified("11111111")
print("************************")
print("Blue house type is ",bluehouse.housetype) #########Printing Class variable after reassigning
print("Red house type is ", redhouse.housetype) ##########Printing Class variable after reassigning
