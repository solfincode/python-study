user = {"username": "jose", "access_level": "guest"}


def get_admin_password():
    return "1234"


def make_function(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permission for {user['username']}"
    return secure_function


get_admin_password = make_function(get_admin_password)
print(get_admin_password())
