# implement a test function for every function in project.py
# every test should be named test_"name of function"
from unittest.mock import patch
from io import StringIO
import sys
import pytest
from fontTools.misc.cython import returns
from more_itertools.more import side_effect
from project import rock_paper_scissor, guess_the_number, hangman
import messages


# using patch to mock user_input, bot_choice and printed output
def test_rock_paper_scissor():
    with patch("builtins.input", side_effect=['Rock', 'x']), \
            patch("random.choice", return_value='Scissors'), \
            patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        # catch SystemExit to prevent test from failing
        with pytest.raises(SystemExit):
            rock_paper_scissor()
            output = mock_stdout.getvalue()
            # Verification that the game proceeds with correct printed messages
            assert "You won" in output


def test_guess_the_number():
    with patch("builtins.input", side_effect=["1", "1", "5", "7", "x"]), \
            patch("random.randint", return_value=7), \
            patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        # catch SystemExit to prevent test from failing
        with pytest.raises(SystemExit):
            guess_the_number()
            # Verification that the game proceeds with correct printed messages
            assert "Beeboop" in mock_stdout
            assert "You won!" in mock_stdout
            assert "You lost" not in mock_stdout


def test_hangman():
    with patch("builtins.input", side_effect=["A", "K", "I", "T", "E", "N", "x"]), \
            patch("random.choice", return_value="KITTEN"), \
            patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        # catch SystemExit to prevent test from failing
        with pytest.raises(SystemExit):
            hangman()
            assert "A is not" in mock_stdout
            assert "You won" in mock_stdout
            assert "You lost" not in mock_stdout


if __name__ == '__main__':
    test_rock_paper_scissor()
    test_guess_the_number()
    test_hangman()
