# Battleship Game! 

This is a game versus the computer. Your task is to locate all ships on the opponents board before the computer found yours!

![Responsive image]()

## Features
---------------------
### Existing Features
- Header 
    - At the top of the page, you find the game name: Battle Ship Game
- The instructions
    - At the start of the game the game symbols are displayed and explained.   

- The player score
    - Players score is visually shown as the game progresses and the board updates its symbols.

![Paragraphs top]() 

- The game: options
    - Player is first asked to choose a letter between A-E and next to choose a number between 1-5.  

![Paragraph bottom]()

- The game: results
    - When either the player or the computer finds all ships on the board, the result is displayed and game is done.   

- Features left to implement
    - Have ships of different sizes
    - Have player position their ships themselves 
    - Multiplayer mode
    - Increase board size as player progresses from winning rounds

    ## Testing 
    ------------
- I have tested my code in PEP8 linter without any significant issues

- I have confirmed that the game results will always be correct. That invalid inputs such as multiple letters, numbers outside of board size, and already checked ship position sends user back to the question input. 

- I have tested this game in both local terminal and on Heroku terminal

### Bugs

- Solved bugs: 
    - When creating the random ship locations, it was clear that there would be a bug if the computer randomized the same position twice for a ship. This was solved with a tuple and a if statement. 
    - When creating validation rules for the input of letter and number, it stored the first faulty input, so that when a valid answer for number was added, the program crashed. This was solved by creating a loop that asks for input as long as the input is not valid. 
    - When running the program, a bug caused the computer to recognize a hit where there should not have been one. Solved eventually by swapping places of the 0 and 1 indexing where the ship placement is defined. 
- Remaining bugs: 
    - No known remaining bugs. 

### Validator Testing
- PEP8, no significant errors were returned. 

## Deployment
---------------
- The site was deployed with Code Institute's terminal on Heroku by:
    - 
    - 
    - 
- Link to the game is found here - 
## Credits
--------------
### Content
- The code to build the game class were taken from Code Institute's Love Sandwiches project. 
- Senior developer Joris Bomert, assisting with sollution for every bug, randomizing of board, player and computer guesses functions and the function to set the quit game option.
- 
- 
- 