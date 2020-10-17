import random

#  method to take user input, choice is the input provided from unit tests
def human_user(choice):
    if choice != False:
        user_input = choice
    else:
        user_input = input(
            "Whats your choice? Rock, Paper or Scissor?").upper()
    if user_input not in ("ROCK", "PAPER", "SCISSORS"):
        return False
    return user_input


def computer_user():
    machine_input = random.choice(("ROCK", "PAPER", "SCISSORS"))
    return machine_input


def game(user_input, machine_input, start):
    continue_game = True
    if start != "YES":
        continue_game = False
        return False
    while continue_game:
        # user_input, machine_input = human_user(), computer_user()
        if user_input == machine_input:
            print("Tie!")
            return "Tie!"
        elif user_input == "ROCK" and machine_input == "PAPER":
            print("You Lose!", machine_input, " beats ", user_input)
            return False
        elif user_input == "ROCK" and machine_input == "SCISSORS":
            print("You Win!", user_input, " beats ", machine_input)
            return True
        elif user_input == "PAPER" and machine_input == "SCISSORS":
            print("You Lose!", machine_input, " beats ", user_input)
            return False
        elif user_input == "PAPER" and machine_input == "ROCK":
            print("You Win!", user_input, " beats ", machine_input)
            return True
        elif user_input == "SCISSORS" and machine_input == "ROCK":
            print("You Lose!", machine_input, " beats ", user_input)
            return False
        elif user_input == "SCISSORS" and machine_input == "PAPER":
            print("You Win!", user_input, " beats ", machine_input)
            return True
        continue_game = False

# # decis is variable passed from unit tests to avoid input from keyboard # #
def start_game(decis):
    start = ""
    # print(decis)
    while True:
        if decis != False:
            start = decis
            # print(start)
        else:
            start = input(
                "Would you like to play Rock, Paper, Scissor? (Yes/No)").upper()
        while(start == "YES"):
            user_input = human_user(False)
            machine_input = computer_user()
            start = game(user_input, machine_input, start)
            start = "NO"
        if start == "NO":  # if a user says no
            return ("Game Over")
        # if a user selects something other than yes or no
        return("Please try again")
# #
# class get():
#     start_game(False)
