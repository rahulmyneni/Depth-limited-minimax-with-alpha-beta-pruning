#Rahul Myneni 1001678634
from MaxConnect4Game import *
import copy

def availablemoves(board):
	availablemoves = []
	n=enumerate(board[0])
	for col, Val in n:
		if Val == 0:
			availablemoves.append(col)
	return availablemoves
		
def result(oldGame, column):
	new = maxConnect4Game()

	try:
		new.nodeDepth = oldGame.nodeDepth + 1
	except AttributeError:
		new.nodeDepth = 1

	new.pieceCount = oldGame.pieceCount
	new.gameBoard = copy.deepcopy(oldGame.gameBoard)
	if not new.gameBoard[0][column]:
		for j in range(5, -1, -1):
			if not new.gameBoard[j][column]:
				new.gameBoard[j][column] = oldGame.currentTurn
				new.pieceCount += 1
				break
	if oldGame.currentTurn == 2:
		new.currentTurn = 1
	elif oldGame.currentTurn == 1:
		new.currentTurn = 2

	new.checkPieceCount()
	new.countScore()
	return new

class Minimax:
	def __init__(self, game, depth):
		self.currentTurn = game.currentTurn
		self.game = game
		self.maxd = int(depth)
		
	def decision(self):

		mini = []
		avamoves = availablemoves(self.game.gameBoard)
		
		for move in avamoves:

			opt = result(self.game,move)
			mini.append( self.minimumValue(opt,9999999,-9999999) )
			
		selected = avamoves[mini.index( max( mini ) )]
		return selected

	def minimumValue(self, state, alfa, beta):
		if state.pieceCount == 42 or state.nodeDepth == self.maxd:
			return self.utility(state)
		k = 9999999

		for move in availablemoves(state.gameBoard):
			new = result(state,move)
			k = min(k,self.maximumValue( new,alfa,beta ))
			if k <= alfa:
				return k
			beta = min(beta, k)
		return k
		
	def maximumValue(self, state, alfa, beta):
		if state.pieceCount == 42 or state.nodeDepth == self.maxd:
			return self.utility(state)
		k = -9999999

		for move in availablemoves(state.gameBoard):
			new = result(state,move)

			k = max(k,self.minimumValue( new,alfa,beta ))
			if k >= beta:
				return k
			alfa = max(alfa, k)
		return k

	def utility(self,state):
		m=self.currentTurn
		if m == 2:
			utility = state.player2Score - state.player1Score
		elif m == 1:
			utility = state.player1Score - state.player2Score

		return utility

