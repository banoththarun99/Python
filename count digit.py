n=int(input("enter the numbers to count : "))
count = 0
while n>0:
    n//=10
    count+=1
print("count of numbers : ",count)
    