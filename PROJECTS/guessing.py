from random import randint
print("Welcome to number guessing game".title())
print("i'm thinking of a number betweeen 1 and 100.".title())
level = input("Choose Difficulty: Type 'easy' or 'hard': ").lower()
# guess_num = [num for num in range(1,101)]
random_num = randint(1, 100)

def start_game(level):
    if level == 'easy':
        attempt = 10
    elif level == 'hard':
        attempt = 5
    else:
        print("enter a valid level")
        
    while True:
        print(f"You have {attempt} remaining to guess the number")
        guess_number = int(input("Make a Guess: "))
        if guess_number == random_num:
            print("You won")
            break
        elif guess_number > random_num:
            print("Too High")
            attempt -= 1
        else:
            print("Too low")
            attempt -= 1   
        if attempt == 0:
            decision = input('Do you want to continue the game: y or n')
            if decision == 'y':
                level = input("Choose Difficulty: Type 'easy' or 'hard': ").lower()
                start_game(level)
            return
            

start_game(level)


# def easy():
#     attempt = 10
#     global guess_number
#     while attempt:
#         print(f"You have {attempt} remaining to guess the number")
#         guess_number = int(input("Make a Guess: "))
#         if guess_number == random_num:
#             print("You won")
#             break
#         elif guess_number > random_num:
#             print("Too High")
#             attempt -= 1
#         else:
#             print("Too low")
#             attempt -= 1