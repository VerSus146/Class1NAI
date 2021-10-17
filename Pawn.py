
class Pawn:
    def __init__(self, player: int, position):
        self.player = player
        self.position = position

    def check_moves(self, board):
        available_moves = []
        x = self.position[0]
        y = self.position[1]

        if self.player == 2:
            direction = -1
        else:
            direction = 1

        if y + direction < 3 and y + direction > -1:
            if board[y + direction][x] == 0:
                available_moves.append([x, y + direction])
            if (x + 1) <= 2 and board[y + direction][x + 1]:
                available_moves.append([y + direction, x + 1])
            if (x - 1) >= 0 and board[y + direction][x - 1]:
                available_moves.append([y + direction, x - 1])
        return available_moves  # get possible moves

    def get_player(self):
        return self.player

    def get_position(self):
        return self.position
