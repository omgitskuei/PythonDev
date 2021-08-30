
# a class that stores information on each of the pieces that have been
# moved at least once
class Moves:
    # name of piece; [piece type][initial col], in order to differentiate
    # between multiples of the same piece on the same team, eg, there's
    # 2 rooks (r1, r8) on white
    piece = ""
    coords = ()
    possible_moves = []

    def __init__(self, piece: str, coords: tuple, ):
        self.piece = piece
        self.coords = coords
        self.possible_moves
