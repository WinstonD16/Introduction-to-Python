class Main:

    ra = 1.05
    def __init__(self,name,email,ids,tuition):
        self.name=name
        self.email=email
        self.ids=ids
        self.tuition=tuition

    #There's bug from calcRaise method, I'll fix it tomorrow
    #Basically the calculate method doesnt work
    #def calcRaise(self):
         #return self.tuition*self.ra
      
        

    def print(self):
        print("My name is:"+self.name)
        print("Email addr:"+self.email)
        print("ID:"+self.ids)
        print("Tuition fee:")
        print(self.tuition)

x=str(input("-->"))  
y=str(input("-->")) 
z=str(input("-->")) 
z1=int(input("-->")) 

main_1=Main(x,y,z,z1)
main_1.print()
main_1.calcRaise()
main_1.print()
print("-------------------------")