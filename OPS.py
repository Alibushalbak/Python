num_1,op,num_2= input("Enter an Expression: ").split()

num_1 = float(num_1)
num_2 = float(num_2)

if op == "+" :
    res= num_1 + num_2
    print(res)

elif op == "-"  :

    res= num_1 - num_2
    print(res)

elif op == "*" :

    res= num_1 * num_2
    print(res)
elif op == "/" :
    
    res= num_1 / num_2
    print(res)

else:
    print("Invalid input ")



