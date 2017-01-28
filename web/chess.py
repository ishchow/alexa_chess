from itertools import product

class chesspiece(object):
    horizontal = [(a,0) for a in range(-7,8)]
    horizontal.remove((0,0))
    vertical = [(0,b) for b in range(-7,8)]
    vertical.remove((0,0))
    diagonal1 = [(a,a) for a in range(-7,8)]
    diagonal1.remove((0,0))
    diagonal2 = [(a,-a) for a in range(-7,8)]
    diagonal2.remove((0,0))
    def __init__(self,piecetype,color):
        self.piecetype = piecetype
        self.color = color

class king(chesspiece):
    def legalmoves():
        kingmoves = [(a,b) for a,b in product(range(-1,2),repeat = 2)]
        kingmoves.remove((0,0))
        castlemove = [(-2,0),(2,0)]
        return kingmoves+castlemove

class queen(chesspiece):
    def legalmoves():
        return horizontal+vertical+diagonal1+diagonal2

class bishop(chesspiece):
    def legalmoves():
        return diagonal1+diagonal2

class knight(chesspiece):
    def legalmoves():
        return [(a,b) for a,b in product(range(-7,8),repeat = 2)]

class rook(chesspiece):
    def legalmoves():
        return horizontal+vertical

class pawn(chesspiece):
    def legalmoves():
        return [(0,1),(0,2),(-1,1),(1,1)]
