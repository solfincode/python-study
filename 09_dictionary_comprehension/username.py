users=[
    (0,"bob","password"),
    (1,"david","badpassword"),
    (2,"kori","longpassword"),
    (3,"paul","helloworld"),
]

# user[1] is extract second element in each users object
user_mapping ={user[1]:user for user in users}

username_input=input("what is your username?")
password_input=input("what is your password?")
_,username,password = user_mapping[username_input]

if password_input == password:
    print("You are logged in")
else:
    print("Incorrect information")