#Created by: WinstonD16//Indonesia

class Employee:
    #method to init
    numOfEmps = 0
    tax = 0.10
    amount_tax=0

    #constructor for inits variables
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.numOfEmps +=1

    #method to returning whole vars
    def fullname(self):
        return '{} {} {} {}'.format(self.first,self.last, self.tax,self.amount_tax)
    #method to calculate salary*tax
    def calculateTax(self):
        self.amount_tax = self.pay*self.tax

    #classmethod
    #we use class method because it has connection to the class
    # it means when you change a certain values
    #it will be changed on the class instead on the instances
    #running the class method from the newly called objects also can change the value on the class
    @classmethod
    def setTax(cls,amount):
        cls.tax = amount

    #staticmethod
    # we use this when the method doesnt need a connection to the class/obj
    #for instances when you not use cls parameter (class method first parameter), and in object self parameter(object method first parameter)
    @staticmethod
    def isWorkday(day):
        #monday =0
        #sunday =6
        if day.weekday()==5 or day.weekday==6:
            return 'Today is weekend'
        return 'You have to work'

    #method for init variables with special format
    @classmethod
    def inputs(cls,emp_str):
        #splitting the value by '-'
        first, last, pay = emp_str.split('-')
        #convert pay to int
        pay = int(pay)
        #return the parsed data into constructor
        return cls(first,last,pay)

#default object constructors
#emp1 = Employee('Corey','Johnson', 50000)
emp_1 = Employee('James', 'May', 50000)
emp_2 = Employee('Richard', 'Hammond', 600000)

#call the specific methods
emp_1.calculateTax()
print (emp_1.fullname())
emp_1.setTax(0.25)
emp_1.calculateTax()
print (emp_1.fullname())

emp_2.calculateTax()
print (emp_2.fullname())
emp_2.calculateTax()
print (emp_2.fullname())




#Inputting data in special format
emp1 = 'Corey-Johnson-50000'
emp2='Dwayne-Johnson-605000'

#init the data into the inputs method
new_emp1 = Employee.inputs(emp1)

new_emp2 = Employee.inputs(emp2)

#call the specific methods
new_emp1.calculateTax()
print (new_emp1.fullname())
new_emp1.setTax(0.25)
new_emp1.calculateTax()
print (new_emp1.fullname())

new_emp2.calculateTax()
print (new_emp2.fullname())
new_emp2.calculateTax()
print (new_emp2.fullname())

#method for import current date from system
from datetime import date
#my_date = datetime.date(2020,9,5)
my_date = date.today()
print(Employee.isWorkday(my_date))
