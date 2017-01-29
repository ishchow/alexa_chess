from itertools import product

class Board:
    """The game board.

    Contains information about:
        locations of chess pieces
        number of active pieces

    x-axis: a-h
    y-axis: 1-8

    """

    def __init__(self):
        self.board = {(x,y):None for x in range(8) for y in range(8)}
        self.pieceCount = 32
        self.whitePieces = 16
        self.blackPieces = 16
        self.SpawnAll()
        self.DisplayBoard()

    def SpawnAll(self):
        for x in range(8):
              self.board[(x, 1)] = pawn('pawn', 'white')
        self.board[(1, 0)] = knight('knight', 'white')
        self.board[(6,0)] = knight('knight', 'white')
        self.board[(0,0)] = rook('rook', 'white')
        self.board[(7,0)] = rook('rook', 'white')
        self.board[(2,0)] = bishop('bishop', 'white')
        self.board[(5,0)] = bishop('bishop', 'white')
        self.board[(4,0)] = king('king', 'white')
        self.board[(3,0)] = queen('king', 'white')

        for x in range(8):
              self.board[(x, 6)] = pawn('pawn', 'black')
        self.board[(1, 7)] = knight('knight', 'black')
        self.board[(6,7)] = knight('knight', 'black')
        self.board[(0,7)] = rook('rook', 'black')
        self.board[(7,7)] = rook('rook' , 'black')
        self.board[(2,7)] = bishop('bishop', 'black')
        self.board[(5,7)] = bishop('bishop', 'black')
        self.board[(4,7)] = king('king', 'black')
        self.board[(3,7)] = queen('queen', 'black')


    def DisplayBoard(self):
        print(self.board)

    def GetPieceCount(self):
        print(self.pieceCount)

    """Move Piece

    Moves a piece from one location to another

    Parameters:
        piece: the chess piece to move
        loc: the current location of the chess piece
        dest: the destination to move to
        game: the game

    """
    def Move(self, loc, dest, game):
        piece = self.board[loc] # the piece object to move
        if piece.color != game.currentPlayer:
            print("he ain't your guy ya dingus!")
            return None
        if piece == None:
            print("There's nobody there, ya dingus!")
            return None

        if (dest[0] not in range(8) or dest[1] not in range(8)):
            print("That destination ain't on the board, ya dingus!")
            return None

        legalMoves = piece.legalmoves() # a list of all possible movement vectors
        attemptedMove = (dest[0]-loc[0],dest[1]-loc[1])

        if attemptedMove not in legalMoves: # If the destination is not possible to move to
            print("Not a legal destination")
            return None

        if self.board[dest] != None:
            if self.board[dest].color == game.currentPlayer: # If you are moving to a space with your own unit
                print("You already have a guy there")
                return None
            else:
                print("You killed a guy!")
                print(piece)
                self.board[dest] = piece
                self.pieceCount -= 1
                if game.currentPlayer == "white":
                    self.blackPieces -= 1
                    print(self.blackPieces)
                    game.CurrentPlayer = "black"
                else:
                    self.whitePieces -= 1
                    print(self.whitePieces)
                    game.CurrentPlayer = "white"
                self.board[loc] = None


        else:
            print(piece)
            self.board[dest] = piece
            self.board[loc] = None
            print("Its now ")

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
    def legalmoves(self):
        return horizontal+vertical+diagonal1+diagonal2

class bishop(chesspiece):
    def legalmoves(self):
        return diagonal1+diagonal2

class knight(chesspiece):
    def legalmoves(self):
        return [(-1,2), (1,2), (2,1), (2,-1), (-2,1), (-2,1), (1,-2), (-1,-2)]

class rook(chesspiece):
    def legalmoves(self):
        return self.horizontal+self.vertical

class pawn(chesspiece):
    def legalmoves(self):
        return [(0,1),(0,2),(-1,1),(1,1)]

class rungame():
    def __init__(self):
        self.gameBoard = Board()
        self.currentPlayer = "white"

    def GetCurrentPlayer(self):
        return self.currentPlayer

    def ChangePlayer(self):
        if self.currentPlayer == "white":
            self.currentPlayer = "black"
        elif self.currentPlayer == "black":
            self.currentPlayer = "white"
        else:
            print("I don't know who's turn it is")


    def getinput(self):
        print('enter a location and destination as tuples:')
        playermove = input()
