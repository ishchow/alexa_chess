from itertools import product

class Board:
    """The game board.

    Contains information about:
        locations of chess pieces
        state of the game
        number of active pieces

    x-axis: a-h
    y-axis: 1-8

    """

    def __init__(self):
        self.board = {(x,y):None for x in range(8) for y in range(8)}
        self.pieceCount = 32
        self.currentPlayer = "white"
        DisplayBoard()


    # Returns empty spaces
    def GetOpenPositions(self):
        pass


    def SpawnPawns(self):
        for x in range(8):
              self.board[(x, 1)] = pawn('white')
        self.Board[(1, 0)] = knight('white')
        self.Board[(6,0)] = knight('white')
        self.Board[(0,0)] = rook('white')
        self.Board[(7,0)] = rook('white')
        self.Board[(2,0)] = bishop('white')
        self.Board[(5,0)] = bishop('white')
        self.Board[(4,0)] = king('white')
        self.Board[(3,0)] = queen('white')

        for x in range(8):
              self.board[(x, 6)] = pawn('black')
        self.Board[(1, 7)] = knight('black')
        self.Board[(6,7)] = knight('black')
        self.Board[(0,7)] = rook('black')
        self.Board[(7,7)] = rook('black')
        self.Board[(2,7)] = bishop('black')
        self.Board[(5,7)] = bishop('black')
        self.Board[(4,7)] = king('black')
        self.Board[(3,7)] = queen('black')


    def DisplayBoard(self):
        print(self.board)

    def GetPieceCount(self):
        print(self.pieceCount)

    def GetCurrentPlayer(self):
        return self.currentPlayer

    def ChangePlayer(self):
        if self.currentPlayer == "white":
            self.currentPlayer = "black"
        elif self.currentPlayer == "black":
            self.currentPlayer = "white"
        else:
            print("I don't know who's turn it is")

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
        return [(-1,2), (1,2), (2,1), (2,-1), (-2,1), (-2,1), (1,-2), (-1,-2)]

class rook(chesspiece):
    def legalmoves():
        return horizontal+vertical

class pawn(chesspiece):
    def legalmoves():
        return [(0,1),(0,2),(-1,1),(1,1)]

class rungame():
    def __init__(self):
        gameBoard = Board()
    def getinput(self):
        print('enter a location and destination as tuples:')
        playermove = input()

        """Move Piece

        Moves a piece from one location to another

        Parameters:
            piece: the chess piece to move
            loc: the current location of the chess piece
            dest: the destination to move to

        """
    def Move(self, loc, dest):
        piece = self.board[loc] # the piece object to move
        legalMoves = piece.legalmoves()
        if self.board[dest] != None:
            print("invalid move ya dingus")
            return None
        attemptedMove = (dest[0]-loc[0],dest[1]-loc[1])
        if attemptedMove not in legalMoves:
            print('didnt work')
        else:
            print(piece)
            self.board[dest] = piece
            self.board[loc] = None
