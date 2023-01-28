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
        
    def _rand_placements(self, amount):
        return [[randint(0, self.size - 1), randint(0, self.size - 1)] for x in range(amount)]

    def _random_ship_placements(self):
        rand_placements = self._rand_placements(4)
        uniq_ships = set(tuple(ship) for ship in rand_placements)

        if len(rand_placements) != len(uniq_ships):
            return self._random_ship_placements()
        else:
            return rand_placements

    def create_boards(self, size):
        self.size = size

        def generateboard():
            return [["." for x in range(size)] for y in range(size)]
       
        self.player_board = generateboard()
        self.computer_board = generateboard()

        self.player_ship_placement = self._random_ship_placements()
        self.computer_ship_placement = self._random_ship_placements()

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

        def correct_x_axis(ship, index): 
            return ship[0] == index

        def correct_y_axis(ship, index): 
            return ship[1] == index

        player_correct_guess = False

        x_axis_index = self.x_axis_dict[player_guessing_letter]
        y_axis_index = self.y_axis_dict[player_guessing_number]

        for ship in self.computer_ship_placement:
            if correct_x_axis(ship, x_axis_index) and correct_y_axis(ship, y_axis_index):
                player_correct_guess = True

        if player_correct_guess:
            print("Hit")
            self.computer_board[y_axis_index][x_axis_index] = "&"

        else:
            print("Miss")
            self.computer_board[y_axis_index][x_axis_index] = "*"

        ##### BörjR GÖRA SAKERHTHTUGUTUTUT 
        computer_correct_guess = False
        comp_guess = self._rand_placements(1)[0]

        comp_x_axis_index = comp_guess[0]
        comp_y_axis_index = comp_guess[1]

        for ship in self.player_ship_placement:
            if correct_x_axis(ship, comp_x_axis_index) and correct_y_axis(ship, comp_y_axis_index):
                computer_correct_guess = True

        if computer_correct_guess:
            self.player_board[comp_y_axis_index][comp_x_axis_index] = "x"
            print("Computer Hit")

        else:
            self.player_board[comp_y_axis_index][comp_x_axis_index] = "*"
            print("Computer Missed")

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
