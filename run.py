from random import randint
import sys

class Game:
    """
    Game class. Keeps track of game scores, 
    game progress, ships.
    """
    def __init__(self, player_name):
        self.player_name = player_name
        self.game_over = False
        self.player_score = 0
        self.computer_score = 0
        self.x_axis_dict = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4
        }

        self.y_axis_dict = {
            "1": 0,
            "2": 1,
            "3": 2,
            "4": 3,
            "5": 4
        }
        
    def _rand_placements(self, amount):
        return [[randint(0, self.size - 1), randint(0, self.size - 1)] for x in range(amount)]

    def _random_ship_placements(self):
        rand_placements = self._rand_placements(self.amount_of_boats)
        uniq_ships = set(tuple(ship) for ship in rand_placements)

        if len(rand_placements) != len(uniq_ships):
            return self._random_ship_placements()
        else:
            return rand_placements

    def _validate_letter(self, letter):
        valid_letters = list(self.x_axis_dict.keys())
        valid = True

        if not letter or not isinstance(letter, str):
            print("Please enter a letter")
            valid = False
        elif len(letter) > 1:
            print("Please enter one letter")
            valid = False
        elif letter not in valid_letters:
            print(f"Please enter one of the following letters: {valid_letters}")
            valid = False

        return valid

    def _validate_number(self, number):
        valid_numbers = list(self.y_axis_dict.keys())
        valid = True

        try:
            int(number)
            if number not in valid_numbers:
                print(f"Please enter one of the following numbers: {valid_numbers}")
                valid = False
        except ValueError:
            print("Please enter a number")
            valid = False

        return valid

    def _ask_letter(self):
        valid_letter = False
        player_guessing_letter = ""

        while not valid_letter:
            player_guessing_letter = input("Choose a letter \n").lower()
            valid_letter = self._validate_letter(player_guessing_letter)

        return player_guessing_letter
    
    def _ask_number(self):
        valid_number = False
        player_guessing_number = ""

        while not valid_number:
            player_guessing_number = input("Choose a number \n")
            valid_number = self._validate_number(player_guessing_number)

        return player_guessing_number

    def _correct_x_axis(self, ship, index): 
        return ship[0] == index

    def _correct_y_axis(self, ship, index): 
        return ship[1] == index

    def _check_if_game_over(self, guesser, correct_guess):
        if correct_guess:
            if guesser == "player":
                self.player_score += 1
                if self.player_score >= self.amount_of_boats:
                    print(f"The winner is: {self.player_name}!")
                    self.game_over = True
                    return True
            else:
                self.computer_score += 1
                if self.computer_score >= self.amount_of_boats:
                    print("Computer won!")
                    self.game_over = True
                    return True

    def _next_round(self):
        player_input = input("Press any key to continue, or Q to quit \n")
        if (player_input.lower() == "q"):
            sys.exit(0)

    def create_boards(self, size):
        self.size = size
        self.amount_of_boats = 4

        def generateboard():
            return [["." for _ in range(size)] for _ in range(size)]
       
        self.player_board = generateboard()
        self.computer_board = generateboard()

        self.player_ship_placement = self._random_ship_placements()
        self.computer_ship_placement = self._random_ship_placements()

        for ship in self.player_ship_placement:
            self.player_board[ship[1]][ship[0]] = "&"
    
    def display_boards(self):
        print("Computer's Board:")
        for row in self.computer_board:
            print(" ".join(row))

        print(f"{self.player_name}'s Board:")
        for row in self.player_board:
            print(" ".join(row))

    def player_guess(self):
        print("-" * 20)

        unique_guess = False
        x_axis_index = ""
        y_axis_index = ""

        while not unique_guess:
            player_guessing_letter = self._ask_letter()
            player_guessing_number = self._ask_number()
            x_axis_index = self.x_axis_dict[player_guessing_letter]
            y_axis_index = self.y_axis_dict[player_guessing_number]
            unique_guess = self.computer_board[y_axis_index][x_axis_index] == "."
            if not unique_guess:
                print("You have already guessed this position")

        player_correct_guess = False
        for ship in self.computer_ship_placement:
            if self._correct_x_axis(ship, x_axis_index) and self._correct_y_axis(ship, y_axis_index):
                player_correct_guess = True

        if player_correct_guess:
            print("Hit")
            self.computer_board[y_axis_index][x_axis_index] = "&"
            return True
        else:
            print("Miss")
            self.computer_board[y_axis_index][x_axis_index] = "*"
            return False

    def computer_input(self):
        computer_correct_guess = False
        
        unique_guess = False

        comp_x_axis_index = ""
        comp_y_axis_index = ""

        while not unique_guess:
            comp_guess = self._rand_placements(1)[0]
            comp_x_axis_index = comp_guess[0]
            comp_y_axis_index = comp_guess[1]
            result = self.player_board[comp_y_axis_index][comp_x_axis_index]
            unique_guess = result == "." or result == "&"

        for ship in self.player_ship_placement:
            correct_x_axis = self._correct_x_axis(ship, comp_x_axis_index)
            correct_y_axis = self._correct_y_axis(ship, comp_y_axis_index)

            if correct_x_axis and correct_y_axis:
                computer_correct_guess = True

        if computer_correct_guess:
            self.player_board[comp_y_axis_index][comp_x_axis_index] = "x"
            print("Computer Hit")
            return True
        else:
            self.player_board[comp_y_axis_index][comp_x_axis_index] = "*"
            print("Computer Missed")
            return False

    def run(self):
        while not self.game_over:
            player_guessed_correctly = self.player_guess()
            if self._check_if_game_over("player", player_guessed_correctly):
                return
            computer_guessed_correctly = self.computer_input()
            self._check_if_game_over("computer", computer_guessed_correctly)
            self.display_boards()
            self._next_round()

def game_rules():
    print("goes here")
    print("-" * 20)

def ask_player_name():
    print("Battle Ship Game!")
    player_name = input("Enter player name \n")
    print(f"{player_name}, your game is starting...")
    print("-" * 20)
    return player_name
    
def main():
    game_rules()
    player_name = ask_player_name()
    game = Game(player_name)
    size = 5
    game.create_boards(size)
    game.display_boards()
    game.run()

main()
