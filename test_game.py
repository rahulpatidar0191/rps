import pytest

from game import  game

# False is when choice1 looses or input is invalid 
# True is when choice1 wins 
# NOTE : All the input need to be in upper case for a vlaid o/p  
@pytest.mark.parametrize("choice1, choice2, start, expected", [
    ("YES","ROCK", "ROCK", "Tie!"),
    ("YES","ROCK", "PAPER", False),
    ("YES","ROCK", "SCISSORS", True),
    ("YES","PAPER", "SCISSORS", False),
    ("YES","PAPER", "ROCK", True),
    ("YES","PAPER", "PAPER", "Tie!"),
    ("YES","SCISSORS", "ROCK", False),
    ("YES","SCISSORS", "PAPER", True),
    ("YES","SCISSORS", "SCISSORS", "Tie!"),
    
    ("NO","SCISSORS", "xyz", False),
    ("YES","SCISSORS", "A", False),
     ("NO", "SCISSORS", "ROCK", False),
     ("qw", "SCISSORS", "SCISSORS", False),
     ("", "","", False),
     ("YES","scissor", "SCISSORS", "False"),
])

def test_game(start, choice1, choice2, expected):
    if start == "YES":
        if choice1 and choice1 not in ("ROCK", "PAPER", "SCISSORS"):
            print("Invalid choice")
            return False

        else:
            print(choice1, choice2)
            dec = game(choice1, choice2, start)
            assert dec == expected
            return True
        
    elif start == "NO":
        dec = game(choice1, choice2, start)
        assert dec == expected