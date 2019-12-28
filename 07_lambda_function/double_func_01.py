def double(x):
    return x * 2

seq = [1,2,3,4,5,6]

# list comprehension
doubled_one=[double(x) for x in seq]
print("first method is ",doubled_one)

# using map function
doubled_two=map(double,seq)
print("second method is ",list(doubled_two))