print("wellcome to python pizza deliveries !")

bill = 0

size = input("what size do you want? S , M or L : ")
if size == "S":
    bill += 15

elif size == "M":
    bill += 20
else :
    bill += 25
    
pepperoni = input("do you want the pepperoni on your pizza? Y or N : ")
if pepperoni == "Y":
    bill += 2
else:
    bill += 3
    
extra_cheese = input("do you want the extra cheese on your pizza? Y or N : ")
if extra_cheese == "Y":
    bill += 1

print("final bill : $",bill)
    
    