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
        #spawn black pieces
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

    """
    Moves a piece from one location to another
    Parameters:
        piece: the chess piece to move
        loc: the current location of the chess piece
        dest: the destination to move to
        game: the game
    """
    def Move(self, loc, dest, game):
        piece = self.board[loc] # the piece object to move
        if piece == None:
            print("There's nobody there, ya dingus!")
            return None

        if piece.color != game.currentPlayer:
            print("he ain't your guy ya dingus!")
            return None

        if (dest[0] not in range(8) or dest[1] not in range(8)):
            print("That destination ain't on the board, ya dingus!")
            return None

        legalMoves = piece.legalmoves() # a list of all possible movement vectors
        attemptedMove = (dest[0]-loc[0],dest[1]-loc[1])

        if attemptedMove not in legalMoves: # If the destination is not possible to move to
            print("Not a legal move")
            return None
        #leftright
        if attemptedMove[0] != 0 and attemptedMove[1] == 0 and piece.piecetype == 'rook' or 'queen':
            left = min(loc[0],dest[0])
            right = max(loc[0],dest[0])
            checkblock = [(a,loc[1]) for a in range(left,right)]
            for i in range(len(checkblock)):
                if self.board[checkblock[i]] != None:
                    print('blocked')
                    return None
                    #ada
        #updown
        if attemptedMove[0] == 0 and attemptedMove[1] != 0 and piece.piecetype == 'rook' or 'queen':
            bot = min(loc[1],dest[1])
            top = max(loc[1],dest[1])
            checkblock = [(loc[0],a) for a in range(bot,top)]
            for i in range(len(checkblock)):
                if self.board[checkblock[i]] != None:
                    print('blocked')
                    return None
        #diagonal
        if attemptedMove[0] == attemptedMove[1] and piece.piecetype == 'bishop' or 'queen':
            botleftx = min(loc[0],dest[0])
            botlefty = min(loc[1],dest[1])
            toprightx = max(loc[0],dest[0])
            toprighty = max(loc[1],dest[1])
            for j in range(abs(attemptedMove[0])):
                checkblock += [(botleftx+j,botlefty+j)]
            for i in range(len(checkblock)):
                if self.board[checkblock[i]] != None:
                    print('blocked')
                    return None
        if attemptedMove[0] == -(attemptedMove[1]) and piece.piecetype == 'bishop' or 'queen':
            topleftx = min(loc[0],dest[0])
            toplefty = max(loc[1],dest[1])
            botrightx = max(loc[0],dest[0])
            botrighty = min(loc[1],dest[1])
            for j in range(abs(attemptedMove[0])):
                checkblock += [(topleftx+j,toplefty-j)]
            for i in range(len(checkblock)):
                if self.board[checkblock[i]] != None:
                    print('blocked')
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
                print("Its now %s turn" % (game.CurrentPlayer))

        else:
            print(piece)
            self.board[dest] = piece
            self.board[loc] = None
            print("Its now %s turn" % (game.CurrentPlayer))


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
    king.piecetype = 'king'
    def legalmoves():
        kingmoves = [(a,b) for a,b in product(range(-1,2),repeat = 2)]
        kingmoves.remove((0,0))
        castlemove = [(-2,0),(2,0)]
        return kingmoves+castlemove

class queen(chesspiece):
    queen.piecetype = 'queen'
    def legalmoves(self):
        return horizontal+vertical+diagonal1+diagonal2

class bishop(chesspiece):
    bishop.piecetype = 'bishop'
    def legalmoves(self):
        return diagonal1+diagonal2

class knight(chesspiece):
    knight.piecetype = 'knight'
    def legalmoves(self):
        return [(-1,2), (1,2), (2,1), (2,-1), (-2,1), (-2,1), (1,-2), (-1,-2)]

class rook(chesspiece):
    rook.piecetype = 'rook'
    def legalmoves(self):
        return self.horizontal+self.vertical

class pawn(chesspiece):
    pawn.piecetype = 'pawn'
    def legalmoves(self):
        if self.color == "white":
            return [(0,1),(0,2),(-1,1),(1,1)]
        elif self.color == "black":
            return [(0,-1),(0,-2),(-1,-1),(1,-1)]


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
