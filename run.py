class Game:
    """
    Game class. Keeps track of game scores, 
    game progress, ships.
    """
    def __init__(self,player_name):
        self.player_name = player_name

def ask_player_name():
    print("Welcome to Battle Ship")
    player_name = input("Enter player name \n")
    print(f"Welcome {player_name}, your game is starting...")
    
    game = Game(player_name)
    print(game.player_name)


ask_player_name()
