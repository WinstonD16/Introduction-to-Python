
lst = []
n = int(input("How long is the array elements?"))


for i in range(0, n):

    x= str(input("-->"))
    #Add an item to the list
    lst.append(x)

#Sort the list elements alphabetically or numerically (Depends on the input type)
lst.sort()

#Print with default format 
print(lst)
print('\n')
print('--------------------------')


#Print all array elements & separate each elements with newline
print(*lst,sep='\n')
print('\n')
print('--------------------------')
#Print all array elements & separate each elements with single space
print(*lst,sep=' ')
print('\n')
print('--------------------------')
#Print all array elements & separate each elements with commas
print(*lst,sep=', ')
print('\n')

#Print array by its index number
print(lst[0])

#Print array from the 1st index to 4th index
print(lst[1:5])

#Changing array element value
x= int(input("Which array elements you want to modify?"))
n= str(input("->"))
lst[x]=n

#Add an item to the index number 
#And also can push the current existing element to next one
lst.insert(1,"Pork")


#Method to copy a list 
list2 = lst.copy()
print(list2)

#Checking if "String" is present in the list
if "Jong Un" in lst:
    print("He's the supreme leader")
else:
    print("The president doesn't exist")

    #Method to clear whole list
    #lst.clear()