attendance = {"David":98,"Kory":30,"Anney":20}

#using items() to unpack key and value from dictionary
for name,age in attendance.items():
    print(f"{name} is {age}")