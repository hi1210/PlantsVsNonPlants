import sys
from game import Game

if __name__ == '__main__':
    if len(sys.argv) == 2:
        #try:
        game = Game(sys.argv[1]);
        game.place_wave()
        game.draw()
        game.get_input()
        while game.gameOver == False:
            game.run_turn()
            game.draw()
            game.get_input()
        print("Game Over");
        #except ValueError as e:
            #print("Invalid gamefile")
    else:
        print("Please enter a game file to run")
