#newone
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
        self.whiteKingLoc = (4,0)
        self.blackKingLoc = (4,7)
        self.whiteKingCheck = False
        self.blackKingCheck = False

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
        self.board[(3,0)] = queen('queen', 'white')

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
        # if game.currentPlayer == "white" and self.whiteKingCheck == True:
        #     if loc != self.whiteKingLoc:
        #         print("Please move the white king")
        #         return None
        # if game.currentPlayer == "black" and self.blackKingCheck == True:
        #     if loc != self.blackKingLoc:
        #         print("Please move the white king")
        #         return None
        piece = self.board[loc] # the piece object to move
        if piece == None:
            print("There's nobody there, ya dingus!")
            return None

        if piece.color != game.currentPlayer:
            print("he ain't your guy ya dingus!")
            return None

        legalMoves = piece.legalmoves() # a list of all possible movement vectors
        attemptedMove = (dest[0]-loc[0],dest[1]-loc[1])

        if (dest[0] not in range(8) or dest[1] not in range(8)):
            print("That destination ain't on the board, ya dingus!")
            return None

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
                    game.currentPlayer = "black"
                else:
                    self.whitePieces -= 1
#                     print(self.whitePieces)
                    game.currentPlayer = "white"
                self.board[loc] = None
                print("Its now %s turn" % (game.currentPlayer))
                self.SearchForChecks(self.whiteKingLoc, self.blackKingLoc, game.currentPlayer)
                return None

        else:
            print(piece)
            self.board[dest] = piece
            self.board[loc] = None
            game.ChangePlayer()
            print("Its now %s turn" % (game.currentPlayer))
            self.SearchForChecks(self.whiteKingLoc, self.blackKingLoc, game.currentPlayer)


    def UpdateKingLocation(self, loc, color):
        """
        Updates the location of the king

        Parameters:
            loc - the new location of the king
            color - the color of the king to move

        """

        if color == "white":
            self.whiteKingLoc = loc
        elif color == "black":
            self.blackKingLoc = loc

    def Check(self, loc, color):
        """
        Checks for a checkmate

        Gets called after the player turn change happens.

        Creates a bool check
        Checks all possible pawn locations for pawns
        Checks all possible rook locations for rooks and queens
        Checks all possible bishop locations for bishops and queens
        Checks all possible knight locations for knights

        Parameters:
            loc - the location of the king as a tuple
            color - the current player's turn

        """
        pawnLocations = []
        rookLocations = []
        bishopLocations = []
        knightLocations = []

        # Get pawn locations
        if color == "white":
            pawnLocations = [(loc[0]-1,loc[1]+1),(loc[0]+1,loc[1]+1)]
        elif color == "black":
            pawnLocations = [(loc[0]-1,loc[1]-1),(loc[0]+1,loc[1]-1)]

        # Get rook locations
        rookLocations += [(a,loc[1]) for a in range(8)]
        rookLocations += [(loc[0],a) for a in range(8)]

        # Get bishop locations
#         minloc = min(loc[0],loc[1])
#         maxloc = max(loc[0],loc[1])
#         botleft = (loc[0]-minloc,loc[1]-minloc)
#         diag1 = max(botleft[0],botleft[1])
#         bishopLocations += [(botleft[0]+a,botleft[1]+a) for a in range(7-diag1)]
#         topleft = (loc[0]-minloc,loc[1]+minloc)
#         diag2 = max(topleft[0],topleft[1])
#         bishopLocations += [(botleft[0]+a,botleft[1]-a) for a in range(7-diag2)]
        bishopLocations += [(loc[0]+a,loc[1]+a) for a in range(-7,8)]
        bishopLocations += [(loc[0]+a, loc[1]-a) for a in range(-7,8)]
#         print("Initial bishopLocations: %s" %(bishopLocations))
        bishopLocations = self.RemoveInvalidSpaces(bishopLocations)
#         print("After bishopLocations: %s" % (bishopLocations))

        # Get knight locations
        knightLocations += [(loc[0]+1,loc[1]+2), (loc[0]+1,loc[1]-2)]
        knightLocations += [(loc[0]-1,loc[1]+2), (loc[0]-1,loc[1]-2)]
        knightLocations += [(loc[0]+2,loc[1]+1), (loc[0]+2,loc[1]-1)]
        knightLocations += [(loc[0]-2,loc[1]+1), (loc[0]-2,loc[1]-1)]
        knightLocations = self.RemoveInvalidSpaces(knightLocations)

        for space in pawnLocations:
            if (self.board[space] != None): #need this cuz of piecetype stuff don't delete
                if self.board[space].piecetype == "pawn":
                    if self.board[space].color != color:
                        print("pawn check")
                        return True

        for space in rookLocations:
            if self.board[space] != None:
                if ((self.board[space].piecetype == "rook") or (self.board[space].piecetype == "queen")):
                    if self.board[space].color != color:
                        if not self.blocking((loc[0]-space[0],loc[1]-space[1]), space, loc):
                            print("rook/queen check")
                            return True

        for space in bishopLocations:
            if self.board[space] != None:
#                 print('nonecheck')
#                 print(space)
#                 print(self.board[space])
                if ((self.board[space].piecetype == "bishop") or (self.board[space].piecetype == "queen")):
#                     print('typechk')
                    if self.board[space].color != color:
#                         print('colrchk')
                        if not self.blocking((loc[0]-space[0],loc[1]-space[1]), space, loc):
                            print("bishop/queen check")
                            return True

        for space in knightLocations:
            if (self.board[space] != None):
                if self.board[space].piecetype == "knight":
                    if self.board[space].color != color:
                        print("knight check")
                        return True

    def RemoveInvalidSpaces(self, spaces):
        """Removes Invalid Spaces

        Parameters:
            spaces - a list of spaces

        """
        filteredSpaces = []
        for item in spaces:
#             print(item)
            if (item[0] > -1) and (item[0] < 8) and (item[1] > -1) and (item[1] < 8):
                filteredSpaces.append(item)
#         print(filteredSpaces)
        return filteredSpaces

    def SearchForChecks(self, whiteloc, blackloc, color):
        if color == "white": #white turn see if white is in checkmate
            self.whiteKingCheck = self.Check(whiteloc, color)
            if self.whiteKingCheck:
                print("white king in check")
        elif color == "black":
#             print('testingtesting123')
            self.blackKingCheck = self.Check(blackloc, color)
#             print('testingtesting321')
            if self.blackKingCheck:
                print("black king in check")

    def CheckForSafeMoves(self, legalMoves): #returns false if there are no safe moves
        safeMoves = []
        safeMoves.append(legalMoves)
        for item in safeMoves:
            if (item[0] not in range(8) or item[1] not in range(8)):
                item = None
            elif self.board[item] != None:
                if self.board[item].color == game.currentPlayer:
                    item = None
        if not safeMoves:
            return False

    def blocking(self, potentialmove, loc, dest):
        #leftright
        if (potentialmove[0] != 0 and potentialmove[1]) == 0 and (self.board[loc].piecetype == ('rook' or 'queen')):
            left = min(loc[0],dest[0])
            right = max(loc[0],dest[0])
            checkblock = [(a,loc[1]) for a in range(left,right)]
            for i in range(len(checkblock)):
                if self.board[checkblock[i]] != None:
                    print('blocked1')
                    return True
        #updown
        # print(piece.piecetype)
        if (potentialmove[0] == 0 and potentialmove[1] != 0) and (self.board[loc].piecetype == ('rook' or 'queen')):
            bot = min(loc[1],dest[1])
            top = max(loc[1],dest[1])
            checkblock = [(loc[0],a) for a in range(bot,top)]
            for i in range(len(checkblock)):
                if self.board[checkblock[i]] != None:
                    print('blocked2')
                    return True
        #diagonal
        if (potentialmove[0] == potentialmove[1]) and (self.board[loc].piecetype == ('bishop' or 'queen')):
            botleftx = min(loc[0],dest[0])
            botlefty = min(loc[1],dest[1])
            toprightx = max(loc[0],dest[0])
            toprighty = max(loc[1],dest[1])
            for j in range(abs(potentialmove[0])):
                checkblock += [(botleftx+j,botlefty+j)]
            for i in range(len(checkblock)):
                if self.board[checkblock[i]] != None:
                    print('blocked3')
                    return True
        if (potentialmove[0] == -(potentialmove[1])) and (self.board[loc].piecetype == ('bishop' or 'queen')):
            topleftx = min(loc[0],dest[0])
            toplefty = max(loc[1],dest[1])
            botrightx = max(loc[0],dest[0])
            botrighty = min(loc[1],dest[1])
            for j in range(abs(potentialmove[0])):
                checkblock += [(topleftx+j,toplefty-j)]
            for i in range(len(checkblock)):
                if self.board[checkblock[i]] != None:
                    print('blocked4')
                    return True
        else:
            return False



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
        return self.horizontal+self.vertical+self.diagonal1+self.diagonal2

class bishop(chesspiece):
    def legalmoves(self):
        return self.diagonal1+self.diagonal2

class knight(chesspiece):
    def legalmoves(self):
        return [(-1,2), (1,2), (2,1), (2,-1), (-2,1), (-2,1), (1,-2), (-1,-2)]

class rook(chesspiece):
    def legalmoves(self):
        return self.horizontal+self.vertical

class pawn(chesspiece):
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
