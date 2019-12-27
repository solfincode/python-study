numbers = [1,2,3,4,5,6,7,8,9,10]

# --- using for loop ---
doubled=[]
for num in numbers:
    doubled.append(num*2)



#---list comprehension---
doubled = [num * 2 for num in numbers]
print(doubled)