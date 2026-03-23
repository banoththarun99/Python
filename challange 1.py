# #multiple of 5 and 3.

# n=int(input("enter a number : "))
# if n%3==0:
#     print("number divisible by 3 only ")
# elif n%5==0:
#     print("number divisible by 5 only ")
# elif n%3 and n%5==0:
#     print("number divisible by both 3 and 5 ")
# else:
#     print("number is not divisible both 3 and 5 ")
    
    
    
# #prime or not

# n = int(input("Enter a number: "))

# if n <= 1:
#     print("Not a prime number")
# else:
#     is_prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = False
#             break  # no need to check further
#     if is_prime:
#         print("Prime number")
#     else:
#         print("Not a prime number")


# # armstrong number
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
    
    
    
# # armstrong with function    

# def is_armstrong(num):
#     sum=0
#     temp=num
#     digits=len(str(num))
#     sum=0
    
#     while temp>0:
#         digit=temp%10
#         temp//=10
#         sum+=digit**digits
#     return sum==num
# num=int(input("enter a number : "))
    
# if is_armstrong(num):
#     print("armstrong number")
# else:
#     print("not armstrong number")


# # perfect number

# def is_perfect(num):
#     sum=0
#     i=1
#     while i < num:
#         if num%i==0:
#             sum+=i
#         i+=1
#     return sum==num
# num=int(input("enter a number : "))
# if is_perfect(num):
#     print(num,"perfectt number ")
# else:
#     print(num,"not perfect number ")

# # Function 1: Check if a single number is perfect
# def is_perfect(num):
#     sum = 0
#     for i in range(1, num):
#         if num % i == 0:
#             sum += i
#     return sum == num


# # Function 2: Find all perfect numbers in a given range
# def find_perfect_in_range(start, end):
#     print(f"Perfect numbers between {start} and {end} are:")
#     for n in range(start, end + 1):
#         if is_perfect(n):   # Call the first function
#             print(n)


# # Main program
# start = int(input("Enter start: "))
# end = int(input("Enter end: "))

# find_perfect_in_range(start, end)

# #strong number
# def factorial(digit):
#     fact=1
#     for i in range(1,digit+1):
#         fact*=i
#     return fact
    

# def is_strong(num):
#     sum=0
#     temp=num
#     while temp>0:
#       digit=temp%10
#       temp//=10
#       sum+=factorial(digit)
#     return sum==num
# num=int(input("enter a nmber")) 
# if is_strong(num):
#     print("strong number")
# else:
#     print("not strong number")
    
        

        
# n=int(input("enterr a number : "))
# if n%2==0 and n%5==0:
#     print("smallest number is multiple of both 2 and 5")
# else:
#     print ("not smallest ")

list = [1,1,2,2,2,3,3,3,4,4,5,]
set=set(list)
print(set)