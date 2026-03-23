arr = [1, 23, 2, 2]
seen = set()

for num in arr:
    if num in seen:
        print("Duplicate number =", num)
        break
    seen.add(num)
