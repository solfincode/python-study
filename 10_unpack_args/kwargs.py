# **kwargs works just like *args, but instead of accepting positional arguments it accepts keyword (or named) arguments.

def print_letter(**kwargs):
    result=""
    for arg in kwargs.values():
        result +=arg
    print(result)
print_letter(a="I ",b="Love ",c="iphone")