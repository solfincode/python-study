def print_pop(list,index):
    try:
        print(list.pop(index))
    except IndexError:
        print(('value of {} can not be accessed ').format(index))
        
print_pop([1,2,3],5)