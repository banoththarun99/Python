start=int(input("enter start : "))
end=int(input("enter end : "))
for num in range (start,end+1):
    if num>1:
        for i in range(2,num):
            if num%2==0:
                break
        else:
         print(num)     
         
         
         

n = int(input("Enter a number: "))

if n <= 1:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")



n = int(input("Enter a number: "))

if n <= 1:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
