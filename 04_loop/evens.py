numbers = [1,2,34,546,45,76,8,6,100]

# define even number empty list
evens=[]

# extract number and check whether it is even or not
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
        
# print out evens list
print(evens)
