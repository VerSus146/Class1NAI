#  Hexpawn
#  Autorzy: Krystian Dąbrowski s18550, Krzysztof Windorpski s18562

from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax
from Pawn import *


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
        self.board = []
        self.create_board()
        self.current_player = 2  # Start with player 1

    def create_board(self):
        pawn_1_1 = Pawn(1, [0, 0])
        pawn_1_2 = Pawn(1, [1, 0])
        pawn_1_3 = Pawn(1, [2, 0])
        pawn_2_1 = Pawn(2, [0, 2])
        pawn_2_2 = Pawn(2, [1, 2])
        pawn_2_3 = Pawn(2, [2, 2])
        self.board = [
            [pawn_1_1, pawn_1_2, pawn_1_3],
            [0, 0, 0],
            [pawn_2_1, pawn_2_2, pawn_2_3]
        ]

    def possible_moves(self):
        all_available_moves = []
        i_y = 0
        for y in self.board:
            i_x = 0
            for x in y:
                position = self.board[i_x][i_y]
                if type(position) is Pawn:
                    all_available_moves.append([position, position.check_moves(self.board)])
                i_x = i_x + 1
            i_y = i_y + 1

        return all_available_moves  # get possible moves

    def make_move(self, move):
        pawn = move[0]
        position = pawn.get_position()
        action = move[1][0]
        self.board[position[0]][position[1]] = 0
        self.board[action[0]][action[1]] = pawn

    def is_over(self):
        return self.win()  # game stops when someone wins

    def win(self):
        opponent_alive = False

        for y in self.board:
            for x in y:
                if type(x) is Pawn:
                    player = x.get_player()

                    if player == self.current_plater:
                        if player.get_position()[1] is not 2:
                            player1_alive = True
                            return False
                    else:
                        if player.get_position()[1] is not 0:
                            player2_alive = True
                            return False
        if not opponent_alive:
            return True

    def show(self):
        for i in self.board:
            print('\t'.join(map(str, i)))

    def scoring(self):
        return 100 if game.win() else 0  # Scoring for the AI


# Setup AI and start match
ai = Negamax(13)  # AI will think 13 moves in advance
game = GameOfBones([Human_Player(), AI_Player(ai)])
history = game.play()

