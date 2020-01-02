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


class Phone(Device):
    def __init__(self,name,connected,storage):
        super().__init__(name,connected)
        self.storage = storage 
        self.remaining_messages = storage
    def __str__(self):
        return f"{super().__str__()} ({self.remaining_messages} message remaining)"
    def call(self,messages):
        if not self.connected:
            print("Your phone is not connected")

iphone = Phone("iphone","USB",500)
print(iphone)
iphone.disconnected()

    