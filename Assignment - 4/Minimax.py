## Name: Sagar sharma
## UTA ID: 1001626958

from MaxConnect4Game import *
import copy

def possibleMoves(board):  ## define the next possible moves for a board state
	possibleMoves = [] ## introduce as a list
	for col, colVal in enumerate(board[0]):  ## run a loop to check the empty spaces in the board state through the columns.
		if colVal == 0:  ## if a columnm value is 0 then that position is added in the list of possible next places for a move.
			possibleMoves.append(col)
	return possibleMoves  ## return the list

## eval function for the depth-limited minimax
def result(oldGame, column):
	newGame = maxConnect4Game()

	try:
		newGame.nodeDepth = oldGame.nodeDepth + 1
	except AttributeError:
		newGame.nodeDepth = 1

	newGame.pieceCount = oldGame.pieceCount
	newGame.gameBoard = copy.deepcopy(oldGame.gameBoard)
	if not newGame.gameBoard[0][column]:
		for i in range(5, -1, -1):
			if not newGame.gameBoard[i][column]:
				newGame.gameBoard[i][column] = oldGame.currentTurn
				newGame.pieceCount += 1
				break
	if oldGame.currentTurn == 1:
		newGame.currentTurn = 2
	elif oldGame.currentTurn == 2:
		newGame.currentTurn = 1

	newGame.checkPieceCount()
	newGame.countScore()

	return newGame

##implementing alpha-beta pruned depth limited minimax algorithm
class Minimax:
	def __init__(self, game, depth):
		self.currentTurn = game.currentTurn
		self.game = game
		self.maxDepth = int(depth)
## alpha beta pruning with depth limited implemented
	def makeDecision(self): ## returns an action leading to the next board state with a utility v

		minValues = [] ## define as a empty list
		possMoves = possibleMoves(self.game.gameBoard)  ## possible moves for the board state

		for move in possMoves:

			rslt = result(self.game,move)
			minValues.append( self.minVal(rslt,99999,-99999) ) ##minval function called to figure out the next best action

		chosen = possMoves[minValues.index( max( minValues ) )] ## action chosen
		return chosen
## minval helps to get the max utility value for the best opponent moves
	def minVal(self, state, alpha, beta):
		if state.pieceCount == 42 or state.nodeDepth == self.maxDepth: ## check for the terminal state
			return self.utility(state) ## return the utility value
		v = 99999   ## max value possible for alpha

		for move in possibleMoves(state.gameBoard):  ## iterate through the possible moves
			newState = result(state,move)  ## new states iterate through the possible moves

			v = min(v,self.maxVal( newState,alpha,beta ))
			if v <= alpha: ## trunkate the next possible sub board state if true
				return v
			beta = min(beta, v) ## if not update the beta value
		return v
## maxval returns the best utility value possible for the best opponent moves
	def maxVal(self, state, alpha, beta):
		if state.pieceCount == 42 or state.nodeDepth == self.maxDepth: ## check fro the terminal state
			return self.utility(state) ## return the utility value
		v = -99999 ## min value for beta

		for move in possibleMoves(state.gameBoard):  ## iterate through the possible moves
			newState = result(state,move)   ## new states iterate through the possible moves

			v = max(v,self.minVal( newState,alpha,beta ))
			if v >= beta: ##trunkate the next possible sub board state if true
				return v
			alpha = max(alpha, v) ## if not update alpha value
		return v

	def utility(self,state): ## utility value function
		if self.currentTurn == 1: ## if player 1
			utility = state.player1Score * 2 - state.player2Score
		elif self.currentTurn == 2: ## if player 2
			utility = state.player2Score * 2 - state.player1Score

		return utility
