#Created by: WinstonD16//Indonesia

class Main:


    ra = 1.05
    #Constructor
    #This is a must when using OOP code
    def __init__(self,name,email,ids,tuition):
        self.name=name
        self.email=email
        self.ids=ids
        self.tuition=tuition

    #The method to calculate tuition vars times ra vars
    #This method will replace tuition value
    def calcRaise(self):
         self.tuition = self.tuition*self.ra
      
        
    #Method to print whole variable
    def print(self):
        print("My name is:"+self.name)
        print("Email addr:"+self.email)
        print("ID:"+self.ids)
        print("Tuition fee:")
        print(self.tuition)

#Input to take the name,email,student id, and tuition fee
x=str(input("Please enter your name: "))  
y=str(input("Please enter your email address: ")) 
z=str(input("Please enter your student ID: ")) 

z1=int(input("Please enter your tuition fee: ")) 

#Use the inputted variable into a constructor
#A method in OOP run only when its have been called in the class to object method

#This is a class to object method
#Basically its initializing a class into a new object

main_1=Main(x,y,z,z1)
main_1.print()
main_1.calcRaise()
print("\n")
print("This is the output after price raise")
main_1.print()
print("-------------------------")
