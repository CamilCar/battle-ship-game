from random import randint

class Game:
    """
    Game class. Keeps track of game scores, 
    game progress, ships.
    """
    def __init__(self, player_name):
        self.player_name = player_name

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

        for ship in self.player_ship_placement:
            self.player_board[ship[0]][ship[1]] = "&"
    
    def display_boards(self):
        print("Computer's Board:")
        for row in self.computer_board:
            print(" ".join(row))

        print(f"{self.player_name}'s Board:")
        for row in self.player_board:
            print(" ".join(row))

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

main()
