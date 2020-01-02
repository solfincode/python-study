class Device:
    def __init__(self,name,connected):
        self.name=name
        self.connected = connected
        self.connected = True
    def __str__(self):
        return f"Device {self.name!r} connected is ({self.connected})"
    def disconnected(self):
        self.connected = False
        print("Disconnected")

phone = Device("iphone","ios")
print(phone)