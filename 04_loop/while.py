
num_answer = 7
user_input=int(input("guess the number below 10? "))
while True:
    
    if user_input < num_answer:
        print("less than answer")
        user_input=int(input("guess the number below 10? "))
    elif user_input == num_answer:
        print("right answer!")
        break
    else:
        print("bigger than answer")
        user_input=int(input("guess the number below 10? "))