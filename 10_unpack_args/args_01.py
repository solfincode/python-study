# about *args and **kwargs
# *args allow you to pass multiple arguments to a function.


def my_multi(*args):
    result = 1
    for x in args:
        result*=x
    return result
# get 1,2,3 argument into my_multi function
print(my_multi(1,2,3))

