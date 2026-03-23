# hallo square pattern

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*", end='')
#         else:
#             print(" ",end='')
#     print()


# hallo right angle triangle

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#        if j == 1 or j == i or i == n:
#             print("*",end=" ")
#        else:
#             print(" ",end=" ")
#     print()


#hallo pyramid pattern

# n = 5
# for i in range(1, n + 1):
    
#     for space in range(n - i):
#         print(" ", end="")

    
#     for j in range(1, 2 * i):
#         if j == 1 or j == (2 * i - 1) or i == n:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()  


# number pyramid

# n=int(input("enter a number : "))
# for i in range(1,n+1):
#     for space in range(n-i):
#         print(" ",end="")
    
#     for j in range(1, i + 1):
#         print(j, end=" ")

#     print()  


#diamond pattern

# n = int(input("Enter a number: "))

# # Upper half of the diamond
# for i in range(1, n + 1):
#     # print spaces
#     for space in range(n - i):
#         print(" ", end="")
#     # print numbers
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# # Lower half of the diamond
# for i in range(n - 1, 0, -1):
#     # print spaces
#     for space in range(n - i):
#         print(" ", end="")
#     # print numbers
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

    


        
        


# s = input("Enter a string: ").lower()  # convert to lowercase
# vowel_count = 0
# consonant_count = 0
# vowels = "aeiou"

# for ch in s:
#     if ch.isalpha():  # check if character is a letter
#         if ch in vowels:
#             vowel_count += 1
#         else:
#             consonant_count += 1

# print("Vowels:", vowel_count)
# print("Consonants:", consonant_count)


    
    
# s = input("Enter a string: ")
# total = 0

# for ch in s:
#     if ch.isdigit():
#         total += int(ch)

# print("Sum of digits =", total)


s=str(input("enter a string : "))
total=0
temp=""
for ch in s:
    if ch is int:
        temp=ch
    else:
        if temp!=0:
            total+=1
print(total)
        