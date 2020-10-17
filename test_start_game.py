import pytest

from game import start_game

@pytest.mark.parametrize("decision, expected", [
    # ("YES","Game Over" ),
     ("NO", "Game Over"),
    ("Paper", "Please try again"),  # only passes if upper( is used)
    ("","Please try again")
])
def test_start_game(decision, expected):
    result = start_game(decision)
    # print(result)
    assert expected == result

# class test_human_user():
#     test_start_game("YES", "Game Over")