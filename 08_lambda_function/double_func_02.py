seq = [1,2,3,4,5,6]


doubled_one =[(lambda x: x*2)(x) for x in seq]
print("first method is ", doubled_one)

doubled_two=map((lambda x:x*2),seq)
print("second method is ",list(doubled_two))