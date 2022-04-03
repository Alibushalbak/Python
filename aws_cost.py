dict1= {
  "name": "eu-central-1",
  "location": "Frankfurt",
  "zones": 3,
  "t3.micro": 0.012
}

dict2= {
  "name": "eu-west-1",
  "location": "Ireland",
  "zones": 3,
  "t3.micro": 0.0114
}

dict3= {
  "name": "eu-west-2",
  "location": "London",
  "zones": 3,
  "t3.micro": 0.0118
}

dict4= {
  "name": "eu-south-1",
  "location": "Milan",
  "zones": 3,
  "t3.micro": 0.012
}

dict5= {
  "name": "eu-west-3",
  "location": "Paris",
  "zones": 3,
  "t3.micro": 0.0118
}

dict6= {
  "name": "eu-west-3",
  "location": "Stockholm",
  "zones": 3,
  "t3.micro": 0.0108
}



num_reg = input("Please choose the number of the area you want to server in :\n 1.Frankfurt\n 2.Ireland\n 3.London\n 4.Milan\n 5.Paris\n 6.Stockholm\n==============================\n your choice:  ")
num_reg = int(num_reg)
if num_reg > 6 :
  print("Your choice was wrong please try again")
  exit()
elif num_reg <1 :
  print("Your choice was wrong please try again")  
  exit()    
print("====================================================================")

hour = input("How many hours do you need to use the server:")
hour = int(hour)


if num_reg == 1:
    cost =float(dict1["t3.micro"]) * hour
    print("====================================================================")
    print("===================================================================\n")
    print("Your cost from ",dict1["location"],"server will be  ",cost,"$")
    print("====================================================================")
    print("====================================================================")
    print("Knowing that these server will be cheaper, as the price will be")
    print(dict2["location"],"It will be against",float(dict2["t3.micro"]) * hour,"$")
    print(dict3["location"],"It will be against",float(dict3["t3.micro"]) * hour,"$")
    print(dict5["location"],"It will be against",float(dict5["t3.micro"]) * hour,"$")
    print(dict6["location"],"It will be against",float(dict6["t3.micro"]) * hour,"$")

elif num_reg == 2:
    cost =float(dict2["t3.micro"]) * hour
    print("====================================================================")
    print("====================================================================\n")
    print("Your cost from ",dict2["location"],"server will be  ",cost,"$")
    print("Knowing that these server will be cheaper, as the price will be")
    print("====================================================================")
    print("IN",dict6["location"],"It will be against",float(dict6["t3.micro"]) * hour,"$")

elif num_reg == 3:
    cost =float(dict3["t3.micro"]) * hour
    print("====================================================================")
    print("====================================================================\n")
    print("Your cost from ",dict3["location"],"server will be  ",cost,"$")
    print("====================================================================")
    print("Knowing that these server will be cheaper, as the price will be")
    print("IN",dict2["location"],"It will be against",float(dict2["t3.micro"]) * hour,"$")
    print("IN",dict6["location"],"It will be against",float(dict6["t3.micro"]) * hour,"$")

elif num_reg == 4:
    cost =float(dict4["t3.micro"]) * hour
    print("====================================================================")
    print("====================================================================\n")
    print("Your cost from ",dict4["location"],"server will be  ",cost,"$")
    print("====================================================================")
    print("Knowing that these server will be cheaper, as the price will be")
    print("IN",dict2["location"],"It will be against",float(dict2["t3.micro"]) * hour,"$")
    print("IN",dict3["location"],"It will be against",float(dict3["t3.micro"]) * hour,"$")
    print("IN",dict5["location"],"It will be against",float(dict5["t3.micro"]) * hour,"$")
    print("IN",dict6["location"],"It will be against",float(dict6["t3.micro"]) * hour,"$")

elif num_reg == 5:
    cost =float(dict5["t3.micro"]) * hour
    print("====================================================================")
    print("====================================================================\n")
    print("Your cost from ",dict5["location"],"server will be  ",cost,"$")
    print("====================================================================")
    print("Knowing that these server will be cheaper, as the price will be")
    print("IN",dict2["location"],"It will be against",float(dict2["t3.micro"]) * hour,"$")
    print("IN",dict6["location"],"It will be against",float(dict6["t3.micro"]) * hour,"$")

elif num_reg == 6:
    cost =float(dict6["t3.micro"]) * hour
    print("====================================================================")
    print("====================================================================\n")
    print("Your cost from ",dict6["location"],"server will be  ",cost,"$") 

   
