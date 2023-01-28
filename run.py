from random import randint

class Game:
    """
    Game class. Keeps track of game scores, 
    game progress, ships.
    """
    def __init__(self, player_name):
        self.player_name = player_name
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

    def _random_ship_placements(self, size):
        rand_placements = [[randint(0, size - 1), randint(0, size - 1)] for x in range(4)]
        uniq_ships = set(tuple(ship) for ship in rand_placements)

        if len(rand_placements) != len(uniq_ships):
            return self._random_ship_placements(size)
        else:
            return rand_placements

    def create_boards(self, size):
        def generateboard():
            return [["." for x in range(size)] for y in range(size)]
       
        self.player_board = generateboard()
        self.computer_board = generateboard()

        self.player_ship_placement = self._random_ship_placements(size)
        self.computer_ship_placement = self._random_ship_placements(size)

        print(self.computer_ship_placement)

        for ship in self.player_ship_placement:
            self.player_board[ship[0]][ship[1]] = "&"
    
    def display_boards(self):
        print("Computer's Board:")
        for row in self.computer_board:
            print(" ".join(row))

        print(f"{self.player_name}'s Board:")
        for row in self.player_board:
            print(" ".join(row))

    def player_guess(self):
        print("-" * 20)
        player_guessing_letter = input("Choose a letter \n")
        player_guessing_number = input("Choose a number \n")

        x_axis_index = self.x_axis_dict[player_guessing_letter]
        y_axis_index = self.y_axis_dict[player_guessing_number]

        def correct_x_axis(ship): 
            return ship[0] == x_axis_index

        def correct_y_axis(ship): 
            return ship[1] == y_axis_index

        correct_guess = False

        for ship in self.computer_ship_placement:
            if correct_x_axis(ship) and correct_y_axis(ship):
                correct_guess = True

        if correct_guess:
            print("Hit")
            self.computer_board[y_axis_index][x_axis_index] = "&"

        else:
            print("Miss")
            self.computer_board[y_axis_index][x_axis_index] = "*"

        self.display_boards()

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
    game.player_guess()

main()
