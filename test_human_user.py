import pytest

from game import human_user

# A valid choice will return same choice back for eg: ROCK - ROCK
@pytest.mark.parametrize("choice, expected",[
     ("", False),
    ("ROCK", "ROCK"),
    ("Paper", False) # only passes if upper( is used)
])
def test_unit_test(choice, expected):
    result = human_user(choice)
    # print(result)
    assert result == expected

# class test_human_user():
#     test_unit_test("ROCK")