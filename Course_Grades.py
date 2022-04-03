
from audioop import avg


x= float(input("Please Enter the grade of Networking : "))
y= float(input("Please Enter the grade of Linux : "))
z= float(input("Please Enter the grade of Python : "))


print("=============================================== ")
print("The Gradess after rounding is ")
print("The Networking grade is : ")
x=round(x)
print(x)

print("The Linux grade is :")
y=round(y)
print(y)

print("The Python grade is :")
z=round(z)
print(z)

print("=============================================== ")

print("The Average of  grades is : ")

my_list = [x,y,z]
average = sum(my_list)/len(my_list)
print(average)

print("=============================================== ")

print("The Highest Grade is : ")

max_num = max(my_list)
print(max_num)








