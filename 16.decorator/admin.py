user={"username":"jose","access_level":"admin"}
def get_admin_password():
    return "1234"
def make_function(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
    return secure_function

get_admin_password = make_function(get_admin_password)
print(get_admin_password())