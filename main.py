from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax

class GameOfBones( TwoPlayerGame ):

    def __init__(self, players=None):
        self.players = players
        self.pile = 20 # start with 20 bones on the pile
        self.current_player = 1 # Start with player 1

    def possible_moves(self): return ['1', '2', '3']  # get possible moves
    def make_move(self, move): self.pile -= int(move)  # remove bones from pile
    def win(self): return self.pile <= 0  # opponent took the last bone ?
    def is_over(self): return self.win()  # game stops when someone wins
    def show(self): print("%d bones left in this pile" % self.pile)  # print how many bones are left
    def scoring(self): return 100 if game.win() else 0  # Scoring for the AI


ai = Negamax(13)
game = GameOfBones([Human_Player(), AI_Player(ai)])
history = game.play()
