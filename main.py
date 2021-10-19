#  Hexpawn
#  Krystian Dąbrowski s18550, Krzysztof Windorpski s18562

from easyAI import TwoPlayerGame, Negamax, AI_Player


class Hexapawn(TwoPlayerGame):
    """

    Zasady gry
    http://wikipedia.org/wiki/Hexapawn
    Dokumentacja easyAI
    https://zulko.github.io/easyAI/ref.html
    """

    def __init__(self, players, size=(3, 3)):
        # Stworzenie boarda
        self.size_y = size[0]
        self.size_x = size[1]
        board = [[(i, j) for j in range(self.size_y)] for i in [0, self.size_x - 1]]

        """ 
         Ustawienie graczy na planszy
          direction = strona poruszania gora lub dół
          goal_line = linia przeciwnika, jak do niej dotrzemy to wygrywamy gora lub dół
          pawns = przypisanie pionka gracza
        """
        for i, d, goal, pawns in [(0, 1, self.size_x - 1, board[0]), (1, -1, 0, board[1])]:
            players[i].direction = d
            players[i].goal_line = goal
            players[i].pawns = pawns

        self.players = players
        self.current_player = 1

    def possible_moves(self):
        moves = []
        # self.opponent pokazuje nam pionki przeciwnika
        opponent_pawns = self.opponent.pawns
        direction = self.player.direction

        """ Definiujemy wszystkie możliwe ruchy pionkiem dla danego gracza """
        for i, j in self.player.pawns:
            if (i + direction, j) not in opponent_pawns:
                moves.append(((i, j), (i + direction, j)))
            if (i + direction, j + 1) in opponent_pawns:
                moves.append(((i, j), (i + direction, j + 1)))
            if (i + direction, j - 1) in opponent_pawns:
                moves.append(((i, j), (i + direction, j - 1)))

        """ 
         Formatujemy je do wersji array zawierającej string z informacją skąd i dokąd pion ma sie przesunąć
         ['A1 B1', 'A2 B2', 'A3 B3']
         
         Wykonujemy to, ponieważ possible_moves nie przyjmuje osadzonych array'ów/list
        """
        to_string = lambda move: " ".join(
            ["ABCDEFGHIJ"[move[i][0]] + str(move[i][1] + 1) for i in (0, 1)]
        )
        possible_moves = list(map(to_string, [(i, j) for i, j in moves]))

        return possible_moves

    def make_move(self, move):
        """ Rozparsowywujemy string z informacją o ruchu i dzielimy go na tuple z pozycją skąd dokąd """
        to_tuple = lambda s: ("ABCDEFGHIJ".index(s[0]), int(s[1:]) - 1)

        """ Pierwsza część naszego stringu to skąd idzie pion, a druga dokąd """
        move = list(map(to_tuple, move.split(" ")))

        ind = self.player.pawns.index(move[0])
        self.player.pawns[ind] = move[1]

        if move[1] in self.opponent.pawns:
            self.opponent.pawns.remove(move[1])

    def lose(self):
        """ Jeżeli przeciwnik wkroczy na linię startu gracza lub gracz nie ma już ruchów - gracz przegrywa """
        return any([i == self.opponent.goal_line for i, j in self.opponent.pawns]) or (
                self.possible_moves() == []
        )

    def is_over(self):
        return self.lose()

    def show(self):
        """
             Wyświetlenie aktualniej tablicy po wykonanym ruchu
             Jezeli jest to pierwszy gracz to dajemy 1
             Jezeli jest to drugi gracz to dajemy 2
             Jezeli jest cokolwiek innego ( błą∂ ) to ustawia "."
        """
        f = (
            lambda x: "1"
            if x in self.players[0].pawns
            else ("2" if x in self.players[1].pawns else ".")
        )
        print(
            "\n".join(
                [
                    " ".join([f((i, j)) for j in range(self.size_x)])
                    for i in range(self.size_y)
                ]
            )
        )

    def scoring(self): return -100 if self.lose() else 0  # Dla AI

ai = Negamax(10)
game = Hexapawn([AI_Player(ai), AI_Player(ai)])
game.play()
print("Gracz %d wygrywa po %d ruchach " % (game.opponent_index, game.nmove))
