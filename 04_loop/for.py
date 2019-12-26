num_list = [2,3,456,4,7546,35,3452,100]

# extract list value using for statement
for num in num_list:
    if num > 100:
        print(str(num) + " is greater than 100")
    else:
        print(str(num)+ " is less than 100")