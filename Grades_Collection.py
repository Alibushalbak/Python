import statistics
print("Please enter the present scores and at the end write stop  ")

try:
    presnt_list = []
    while True:
        presnt_list.append(int(input()))
        

        
except:  
    print("Your input scores is ",presnt_list) 

print("================================================================= ") 

print("Enter the number you want to compare with it  ")  
output = []
input_a = input()
input_a = int(input_a)
list1 = presnt_list
list1.sort(reverse = True)
le=len(list1)
print("================================================================= ") 
print('The Numbers greater than the entered number(',input_a,') is')
for i in list1:
    if i > input_a : print(i)

print("================================================================= ") 



sum_list = sum(list1)
avge = sum_list/le
print('The Numbers greater than average(',avge,') is')
for j in list1:
    if j > avge: print(j)


print("================================================================= ") 
list1.sort()
res = statistics.median(list1)
list1.sort(reverse = True)
print('The Numbers greater than median(',res,') is')
for l in list1:
    if l > res: print(l)


print("================================================================= ") 
print("THE END OF THE PROGRAM ") 
print("THANKS") 
print("================================================================= ") 








