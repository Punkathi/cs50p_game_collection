# import needed modules/libraries
# those that need to be installed via pip need to be listed in a file named "requirements.txt"
import sys
import random
import messages


# main-part of the program
# Here the user can choose which Game they want to play or if they want to exit the game
def main():
    messages.cat1()
    messages.welcome()
    game_choice = input("Which Game would you like to play? ( 1 | 2 | 3 ) \nInput \"x\" to exit. \n$")
    if game_choice == "1":
        rock_paper_scissor()
    elif game_choice == "2":
        guess_the_number()
    elif game_choice == "3":
        hangman()
    else:
        sys.exit("Something went wrong. Please restart the program manually.")


# first game - rock paper scissor
def rock_paper_scissor():
    messages.cat2()
    messages.game1()
    valid_signs = ["Rock", "Paper", "Scissors"]
    while True:
        bot_sign = random.choice(valid_signs)
        user_sign = input("Rock, Paper or Scissors? ").title().strip()
        if bot_sign == "Rock" and user_sign == "Scissors" or bot_sign == "Paper" and user_sign == "Rock" or bot_sign == "Scissors" and user_sign == "Paper":
            print(f"You lost! Mimi won by using {bot_sign}. Please try again!")
        elif bot_sign == user_sign:
            print(f"Draw! - You and Mimi used {user_sign}. Please try again!")
        elif user_sign == "Rock" and bot_sign == "Scissors" or user_sign == "Paper" and bot_sign == "Rock" or user_sign == "Scissors" and bot_sign == "Paper":
            print(f"You won! Mimi lost by using {bot_sign}.")
            restart()


# second game - guess the number
def guess_the_number():
    messages.cat3()
    messages.game2()
    set_difficulty = int(input("$"))
    tries = 5
    if set_difficulty == 1:
        number = random.randint(1, 10)
    elif set_difficulty == 2:
        number = random.randint(1, 50)
    elif set_difficulty == 3:
        number = random.randint(1, 100)
    while tries > 0:
        guess = int(input("Your guess: "))
        if guess != number:
            tries -= 1
            print(f"Beeboop, wrong number. You have {tries} tries left.")
        elif guess == number:
            print(f"You won! You had {tries} tries left.")
            restart()
        if tries == 0:
            print(f"You lost! {number} was the winning number.")
            restart()


# third game - hangman
def hangman():
    messages.cat3()
    messages.game3()
    possible_words = ["KITTEN", "LYNXES", "TIGERS", "SPHINX", "FELINE", "CALICO", "KITCAT"]
    word = random.choice(possible_words)
    tries = 11
    guess = "_" * len(word)
    wrong_letters = ""
    while tries > 0 or guess != word:
        print(f"You have {tries} tries.\n"
              f"{guess}\n"
              f"Wrong letters: {wrong_letters}")
        if tries == 0:
            print(f"You lost! \"{word}\" was the winning word.")
            restart()
        elif guess == word:
            print(f"You won! You had {tries} tries left.")
            restart()
        letter = input("\nLetter: ").upper().strip()
        if letter in word:
            tries -= 1
            temp = ""
            for i in range(len(word)):
                if letter == word[i]:
                    temp += letter
                elif guess[i] != "_":
                    temp += guess[i]
                else:
                    temp += "_"
            guess = temp
        else:
            print(f"{letter} is not n the word")
            wrong_letters += letter
            tries -= 1


# function for restarting or exiting the program, after one of the games is over
def restart():
    r = input("\nDo you want to restart or exit the program?"
              "\nRestart: r"
              "\nExit: x "
              "\n$").strip().lower()
    if r == "x":
        sys.exit("Good Bye!")
    elif r == "r":
        main()
    else:
        sys.exit("Something went wrong. Please restart the program manually.")


if __name__ == '__main__':
    main()
