# store string into variable
letters = "I want to study python"

# number
count = 1000

# boolean
is_contained = True

# list
camera_list = ['nikon','leica','canon']
print(camera_list[0]) # print first element in camera_list
camera_list[0] = "super camera" # assign value in first position

# tuple - immutable on value
camera_tuple = ('nikon','leica','canon')

# set
camera_set={'nikon','leica','canon'}

# dictionary - key:value pair
camera_dict ={'nikon':'black','leica':'red','canon':'blue'}

# add value in dictionary of camera_dict
camera_dict["iphone"] = "space gray"

# iteration
for camera in camera_dict:
    print(("{camera}: {camera_dict}").format(camera=camera,camera_dict=camera_dict[camera]))

# /below is output from iteration/
# nikon: black
# leica: red
# canon: blue
# iphone: space gray

# list of dictionary
iphones =[
    {"name":"iphone 8","size":20},
    {"name":"iphone 10","size":120},
    {"name":"iphone 11","size":420},
    {"name":"iphone 12","size":520},
]