#  Hexpawn
#  Autorzy: Krystian Dąbrowski s18550, Krzysztof Windorpski s18562

from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax


class GameOfBones(TwoPlayerGame):
    #  Players have to play against eachother.
    #  To win the game you have to defeat your enemy by:
    #  Stepping on his start point
    #  Defeating all of his pawns
    #  Blocking him from doing any legal moves

    #  Positions of the board:
    #  7 8 9
    #  4 5 6
    #  1 2 3

    def __init__(self, players=None):
        self.players = players
        self.board = [0 for i in range(9)]
        self.current_player = 1  # Start with player 1

    def possible_moves(self): return ['1', '2', '3']  # get possible moves
    def make_move(self, move): self.pile -= int(move)  # remove bones from pile
    def win(self): return self.pile <= 0  # opponent took the last bone ?
    def is_over(self): return self.win()  # game stops when someone wins
    def show(self): print("%d bones left in this pile" % self.pile)  # print how many bones are left
    def scoring(self): return 100 if game.win() else 0  # Scoring for the AI


# Setup AI and start match
ai = Negamax(13)  # AI will think 13 moves in advance
game = GameOfBones([Human_Player(), AI_Player(ai)])
history = game.play()
