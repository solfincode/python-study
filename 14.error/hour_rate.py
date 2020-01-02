try:
    hours = float(input("hours"))
    rate = float(input("rate"))

    if hours > 40:
        pay = hours * rate * 1.5
    else:
        pay = hours * rate

    print(pay)
except:
    print("not a number")