# n = int(input("enter the number:"))
# sum=0
# temp=n
# digits=len(str(n))
# while temp>0:
    
#     digit=temp%10
#     temp//=10
#     sum+=digit**digits
# if sum==n:
#     print("amstrong",sum)
# else:
#     print("not armstrong",sum)

    
start=int(input("enter start:"))
end=int(input("enter end:"))
print("Armstrong numbers between start and end is :" )
count=0
for num in range(start,end+1):
    sum=0
    temp=num
    digits=len(str(num))
    while temp>0:
        digit=temp%10
        temp//=10
        sum+=digit**digits
    if sum==num:
        print(num)
        count+=1
print(count)
    
        
  