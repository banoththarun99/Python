arr=[-2,1,-3,4,-1,2,1,-5,4]
max_current=arr[0]
max_global=arr[0]
for i in range (1,len(arr)):
    max_current=max(arr[i],max_current+arr[i])
    if max_current>max_global:
        max_global=max_current
print("max subarr sum :",max_global)