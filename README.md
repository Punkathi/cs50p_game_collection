 # Game Collection
    #### Video Demo:  https://youtu.be/4-eI9U-EbtQ
    #### Description: My final project for CS50 Python is a collection of three classic games.
    #### It allows users to play "Rock, Paper, Scissors", "Guess the Number" and "Hangman".
    #### The project provides a fun and text-based interactive experience, integrating a game loop,
    #### that allows users to choose which game they want to play or exit the program.
    #### After each game session, users are given the option to restart or exit.
    #### This project demonstrates a range of Python programming concepts I learned while taking part in CS50
    #### Python. It includes concepts like control structures, functions and randomization. 
    #### I tried implementing a modular design by handling messages externally in a seperate file for easier maintainance.
    #### The project is organized around a central menu system that guides users through the different games.
    #### Each game operates independently, but they all share a similar structure of user input, game logic and feedback.
# Project structure
    #### main(): This is the starting point of the program. 
    #### It functions as a menu where users can choose one of the implemented games to play or exit the program.
    #### Depending on the input, it directs the users to the respective game.
    ####
    #### rock_paper_scissor(): This is the first implemented game, the classic "Rock, Paper, Scissors".
    #### The function generates a random choice for the computer by utilizing the random module and compares it to the user's choice.
    #### Based on the game logic, the user either wins, loses or ties with the computer.
    #### If the player wins, the game ends and prompts the user to restart or exit the program.
    ####
    #### guess_the_number(): This is the second implemented game.
    #### The users guesses a randomly selected number based on the difficulty they choose.
    #### Difficulty ranges between n1-10, n1-50 and n1-100.
    #### Users are given 5 attempts to guess correctly. After each incorrect guess, the program informs the player how many tries are left.
    #### If the player guesses the number within the given attempts, they win. If not, the program reveals the correct number.
    #### Just like with rock_paper_scissor() the users can restart or exit the program afterwards.

    #### hangman(): This is the final implemented game. It's a textbased version of the classic Hangman.
    #### The function selects a random word from a list of possible words and the users guess letters within a set number of attempts.
    #### Users have 11 attempts. The program displays the correct guesses so far and tracks the letters the player has guesses incorrectly.
    #### The game ends when the users either correctly guessed the word or if they run out of tries.
    #### Just like the other two games users can choose to restart or exit the program afterwards.

    #### restart(): This function hanesl the user's decision after finishing a game.
    #### It provides the options to either restart (and thus return to the game choices) or exit the program.
    #### If the users input invalid commands, the program terminates with an error message asking the user to restart manually.
# External Files and Modules
    #### messages.py: This is my external module used to manage and print the different messages and game instructions.
    #### It helps improve modularity by separating the game logic from most of the interface text, allowing the game to be modified or localized easier.

    #### requirements.txt: External dependencies are listed here. 
    #### I used mostly core libraries that are standard to Python, so this file is not heavily utizlied until additional functionally is added in the future.
# Design Choices
    #### The key design choice in this project was the separation of the game logic from some of the messages, achieved by creating a separate file(messages.py)
    #### and using the import function. This provides cleaner code, better readability and easier maintenance,
    #### since modifying instructions and output does not require diving into the core game logic.

    #### Another design decision was to handle game chpice and restart logic in a centralized manner, 
    #### ensuring that users can easily navigate between different games without relaunching the pogram every time. 
    #### The use of loops and conditionals in each game ensures that users receive real-time feedback 
    #### and can make multiple guesses or attempts withput restarting the entire program.

    # I also added simple ascii art of cats, because It makes the program look a bit more grafical (and because I love cats).
# Limitations and Future Improvements
    #### The games currently rely on text input only and are played in the terminal.
    #### Adding a graphical user interface using a library like tkinter or pygame would significantly enhance user experience.

    #### More games could be added to the collection to expand the project's scope.
    #### Currently, the program does not validate non-integer input when setting difficulty levels or making guesses in the number-guessing-game.
    #### Adding input validation would make the project more robust, so I'll probably keep working on it from time to time.

# Conclusion
    #### This project deonstrates the implementation of three classic games in Python,  
    #### with modularity and user interaction in mind. By splitting the messaging and game logic, the program remains easy to modify and extend.
    #### Additionally, each game is structured to provide clear feedback and allows users to restart without needing to manully restart the application,
    #### except for when their input is invalid.



