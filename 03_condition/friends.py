friends =["bob","Jane","Eliot"]

guess_friends = input("which your friend is in the room?")
if guess_friends in friends:
    print(guess_friends + " is in the room")
else:
    print(guess_friends + " is not in the room")