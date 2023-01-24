class Game:
    """
    Game class. Keeps track of game scores, 
    game progress, ships.
    """
    def __init__(self,player_name):
        self.player_name = player_name
        
    def create_boards(self, size):
        board = [["." for x in range(size)] for y in range(size)]
        self.player_board = board
        self.computer_board = board

    def display_boards(self):
        print("Computer's Board:")
        for row in self.computer_board:
            print(" ".join(row))

        print(f"{self.player_name}'s Board:")
        for row in self.player_board:
            print(" ".join(row))


def ask_player_name():
    print("Welcome to Battle Ship")
    player_name = input("Enter player name \n")
    print(f"Welcome {player_name}, your game is starting...")
    
    return player_name
    
def main():
    player_name = ask_player_name()
    game = Game(player_name)
    size = 5
    game.create_boards(size)
    game.display_boards()

main()
