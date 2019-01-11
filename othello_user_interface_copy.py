#Leon Luong 69139013 Lab section 9



import othello_logic_copy

    
def start_game(new_game: 'Othello'):
    "Takes in all of the parameters and starts the game."
    """NUM_OF_ROWS = int(input())
    NUM_OF_COL = int(input())
    PLAYER_ONE = input()
    TOP_LEFT_PLAYER = input()
    RULE = input()"""
    #new_game.start(NUM_OF_ROWS, NUM_OF_COL, PLAYER_ONE, TOP_LEFT_PLAYER, RULE)
    new_game.start()
    
if __name__ == '__main__':
    print('FULL')
    game = othello_logic_copy.Othello()
    start_game(game)
    game.gameplay()
