# remove white space and tab on left or right and both side
string1 = " thin iphone will be developed in the future  "
lstrip = string1.lstrip()
print("remove left:",lstrip)

rstrip = string1.rstrip()
print("remove right:",rstrip)

both = string1.strip()
print("remove both side:",both)