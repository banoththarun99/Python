n=int(input("enter the digit to sum : "))

sum=0

temp=n
while temp>0:
    digit = temp%10    #get last digit
    sum += digit       #add the digit
    temp //=10         #remove last digit
print(sum)