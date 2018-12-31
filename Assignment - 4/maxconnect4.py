## Name: Sagar Sharma
## UTA ID: 1001626958

import sys
from MaxConnect4Game import *
from Minimax import *

def oneMoveGame(currentGame,depth):
    if currentGame.pieceCount == 42:    # Is the board full already?
        print 'BOARD FULL\n\nGame Over!\n'
        sys.exit(0)

    #currentGame.aiPlay() # Make a move (only random is implemented)
    ## instead of using a random play, implement aplha-beta pruned depth limited minimax algo
    searchTree = Minimax(currentGame,depth)
    move = searchTree.makeDecision()
    result = currentGame.playPiece(move)
    afterMoveOperations(currentGame,move)
    currentGame.gameFile.close()

# display the game state after move by either of the players for a game state
def afterMoveOperations(currentGame,move):

    print('\n\nMove number: %d: Player %d, column %d\n' % (currentGame.pieceCount, currentGame.currentTurn, move+1))
    if currentGame.currentTurn == 1: ## if player 1 played then
        currentGame.currentTurn = 2 ## player 2 has the next turn
    elif currentGame.currentTurn == 2: ## if player 2 played then
        currentGame.currentTurn = 1 ## player 1 has the next move

    print 'Game state after move:'
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile() ## print the board state to the output file.


def interactiveGame(currentGame,depth):

## implement the interactive game mode
    while not currentGame.pieceCount == 42: ## if not the end game board state
        if currentGame.currentTurn == 1: ## if player 1 next move
            userMove = input("Enter the column number [1-7] where you would like to play : ")
            if not 0 < userMove < 8: ## keep in range of game
                print "Invalid column number!"
                continue
            if not currentGame.playPiece(userMove-1): ## if no space available in the column
                print "This column is full!"
                continue
            try:
                currentGame.gameFile = open("humanplayer.txt", 'w') ## if error opeing the output files
            except:
                sys.exit('Error opening output file.')
            afterMoveOperations(currentGame,userMove-1)

        elif not currentGame.pieceCount == 42: ## if not the end game board state
            searchTree = Minimax(currentGame,depth) ## implement depth limited alpha beta pruned minimax algo
            move = searchTree.makeDecision()
            result = currentGame.playPiece(move)
            try:
                currentGame.gameFile = open("comupterplayer.txt", 'w') ##  if error openinig output files
            except:
                sys.exit('Error opening output file.')
            afterMoveOperations(currentGame,move)

    currentGame.gameFile.close()

    if currentGame.player1Score > currentGame.player2Score:
        print "Player 1 wins"
    elif currentGame.player2Score > currentGame.player1Score:
        print "Computer wins"
    else:
        print "DRAW GAME"
    print "I hope you enjoyed playing MaxConnect4Game"

def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print 'Four command-line arguments are needed:'
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() # Create a game

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print '\nMaxConnect-4 game\n'
    print 'Game state before move:'
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        if argv[3] == 'computer-next': #override current turn according to commandline arguments
            currentGame.currentTurn = 2
        else: #human-next
            currentGame.currentTurn = 1
        interactiveGame(currentGame,argv[4]) # Be sure to pass whatever else you need from the command line
    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame,argv[4]) # Be sure to pass any other arguments from the command line you might need.


if __name__ == '__main__':
    main(sys.argv)
