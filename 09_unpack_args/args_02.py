#use the * operator to unpack a list and pass arguments to a function

list1=[1,2,3,4]
list2=[4,5]
list3=[67,7,6]

def my_sum(*args):
    total=0
    for val in args:
        total+=val
    return total

print(my_sum(*list1,*list2,*list3))