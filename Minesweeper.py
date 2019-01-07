from graphics import *
import random
numberOfBombs = 10
width = 400
height = 400
rows = 9
columns = 9
win = GraphWin("Minesweeper", width, height)
class Square():
	def __init__(self, bomb, numberOfBombsNear, window):
		self.bomb = bomb
		self.bombsNear = numberOfBombsNear
		self.window = window
		self.flagged = False
		self.revealed = False
	def reveal(self, tileNumber):
		if self.flagged:
			pass
		else:
			x = ((width/columns)/2)+(width/columns)*((tileNumber)%columns)
			y = ((height/rows)/2)+((height/rows)*((tileNumber)//columns))
			p = Point(x, y)
			if self.bomb:
				text = "B"
			else:
				text = str(self.bombsNear)
			self.bombText = Text(p, text)
			self.bombText.draw(self.window)
			self.revealed = True
	def getRevealed(self):
		return self.revealed
	def bombsNear(self):
		if self.bomb:
			return "B"
		return self.bombsNear
	def getBomb(self):
		return self.bomb
	def flag(self, tileNum):
		if self.flagged:
			self.text.undraw()
			self.flagged = False
		else:
			x = ((width/columns)/2)+(width/columns)*((tileNum)%columns)
			y = ((height/rows)/2)+((height/rows)*((tileNum)//columns))
			p = Point(x, y)
			self.text = Text(p, "F")
			self.text.draw(self.window)
			self.flagged = True
	def getFlagged(self):
		return self.flagged
def bombGenerator():
	bombs = []
	for i in range(numberOfBombs):
		tileBomb = random.randint(0, rows*columns-1)
		while tileBomb in bombs:
			tileBomb = random.randint(0, rows*columns-1)
		bombs.append(tileBomb)
	return bombs
def findBombsNear(bombLocations):
	tileInfo = []	
	for tileNum in range((rows*columns)):
		counter = 0
		tempInfo = []
		if tileNum in bombLocations:
			tempInfo.append(True)
			tempInfo.append(-1)
		else:
			tempInfo.append(False)
			if tileNum > columns and (tileNum%columns) != 0:
				if tileNum-(columns+1) in bombLocations:
					counter += 1
			if tileNum > columns:
				if tileNum-columns in bombLocations:
					counter += 1
			if tileNum > columns and (tileNum%columns) != 8:
				if tileNum-(columns-1) in bombLocations:
					counter += 1
			if (tileNum%columns) != 8:
				if tileNum+1 in bombLocations:
					counter += 1
			if (tileNum%columns) != 8 and tileNum <= (rows*columns)-columns:
				if tileNum+columns+1 in bombLocations:
					counter += 1
			if tileNum <= (rows*columns)-columns:
				if tileNum+columns in bombLocations:
					counter += 1
			if tileNum <= (rows*columns)-columns and (tileNum%columns) != 0:
				if tileNum+columns-1 in bombLocations:
					counter += 1
			if (tileNum%columns) != 0:
				if tileNum-1 in bombLocations:
					counter += 1
			tempInfo.append(counter)
		tileInfo.append(tempInfo)
	return(tileInfo)
def returnSquares(tileInfo, window):
	tiles = []
	for i in range(rows*columns):
		tile = Square(tileInfo[i][0], tileInfo[i][1], window)
		tiles.append(tile)
	return tiles
def createGrid(window):
	horizontalBaseline = height/rows
	for i in range(columns+1):
		x = (width/columns)*i
		p1 = Point(x, 0)
		p2 = Point(x, height)
		tempLine = Line(p1, p2)
		tempLine.setWidth(2)
		tempLine.draw(window)
	for i in range(rows+1):
		y = (height/rows)*i
		p1 = Point(0, y)
		p2 = Point(width, y)
		tempLine = Line(p1, p2)
		tempLine.setWidth(2)
		tempLine.draw(window)
def main():
	bombs = bombGenerator()
	tileInfo = findBombsNear(bombs)
	squares = returnSquares(tileInfo, win)
	regularSquares = []
	for i in range(rows*columns):
		regularSquares.append(i)
	for i in bombs:
		regularSquares.remove(i)
	createGrid(win)
	seen = []
	while True:
		seen.sort()
		if seen == regularSquares:
			end = "win"
			break
		lst = []
		key = win.getKey()
		if key == "space":
			click = win.getMouse()
			xPixels = click.getX()
			yPixels = click.getY()
			x = (xPixels)//(width/columns)
			y = (yPixels)//(height/rows)
			tileNum = x+(y*columns)
			if squares[int(tileNum)].getBomb():
				end = "bomb"
				break
			if tileNum not in seen:
				seen.append(int(tileNum))
				if tileNum > columns and (tileNum%columns) != 0:
					if squares[int(tileNum-(columns+1))].getBomb() or int(tileNum-(columns+1)) in seen:
						pass
					else:
						if squares[int(tileNum)].bombsNear == 0:
							if int(tileNum-(columns+1)) not in lst and squares[int(tileNum-(columns+1))].bombsNear == 0:
								lst.append(int(tileNum-(columns+1)))
							seen.append(int(tileNum-(columns+1)))
							squares[int(tileNum-(columns+1))].reveal(int(tileNum-(columns+1)))
				if tileNum > columns:
					if squares[int(tileNum-columns)].getBomb() or int(tileNum-columns) in seen:
						pass
					else:
						if squares[int(tileNum)].bombsNear == 0:
							if int(tileNum-columns) not in lst and squares[int(tileNum-columns)].bombsNear == 0:
								lst.append(int(tileNum-columns))
							seen.append(int(tileNum-columns))
							squares[int(tileNum-columns)].reveal(int(tileNum-columns))
				if tileNum > columns and (tileNum%columns) != 8:
					if squares[int(tileNum-(columns-1))].getBomb() or int(tileNum-(columns-1)) in seen:
						pass
					else:
						if squares[int(tileNum)].bombsNear == 0:
							if int(tileNum-(columns-1)) not in lst and squares[int(tileNum-(columns-1))].bombsNear == 0:
								lst.append(int(tileNum-(columns-1)))
							seen.append(int(tileNum-(columns-1)))
							squares[int(tileNum-(columns-1))].reveal(int(tileNum-(columns-1)))
				if (tileNum%columns) != 8:
					if squares[int(tileNum+1)].getBomb() or int(tileNum+1) in seen:
						pass
					else:
						if squares[int(tileNum)].bombsNear == 0:
							if int(tileNum+1) not in lst and squares[int(tileNum+1)].bombsNear == 0:
								lst.append(int(tileNum+1))
							seen.append(int(tileNum+1))
							squares[int(tileNum+1)].reveal(int(tileNum+1))
				if (tileNum%columns) != 8 and tileNum <= (rows*columns)-(columns+1):
					if squares[int(tileNum+columns+1)].getBomb() or int(tileNum+columns+1) in seen:
						pass
					else:
						if squares[int(tileNum)].bombsNear == 0:
							if int(tileNum+columns+1) not in lst and squares[int(tileNum+columns+1)].bombsNear == 0:
								lst.append(int(tileNum+columns+1))
							seen.append(int(tileNum+columns+1))
							squares[int(tileNum+columns+1)].reveal(int(tileNum+columns+1))
				if tileNum <= (rows*columns)-(columns+1):
					if squares[int(tileNum+columns)].getBomb() or int(tileNum+columns) in seen:
						pass
					else:
						if squares[int(tileNum)].bombsNear == 0:
							if int(tileNum+columns) not in lst and squares[int(tileNum+columns)].bombsNear == 0:
								lst.append(int(tileNum+columns))
							seen.append(int(tileNum+columns))
							squares[int(tileNum+columns)].reveal(int(tileNum+columns))
				if tileNum <= (rows*columns)-(columns+1) and (tileNum%columns) != 0:
					if squares[int(tileNum+columns-1)].getBomb() or int(tileNum+columns-1) in seen:
						pass
					else:
						if squares[int(tileNum)].bombsNear == 0:
							if int(tileNum+columns-1) not in lst and squares[int(tileNum+columns-1)].bombsNear == 0:
								lst.append(int(tileNum+(columns-1)))
							seen.append(int(tileNum+(columns-1)))
							squares[int(tileNum+(columns-1))].reveal(int(tileNum+columns-1))
				if (tileNum%columns) != 0:
					if squares[int(tileNum-1)].getBomb() or int(tileNum-1) in seen:
						pass
					else:
						if squares[int(tileNum)].bombsNear == 0:
							if int(tileNum-1) not in lst and squares[int(tileNum-1)].bombsNear == 0:
								lst.append(int(tileNum-1))
							seen.append(int(tileNum-1))
							squares[int(tileNum-1)].reveal(int(tileNum-1))
				squares[int(tileNum)].reveal(int(tileNum))
			while True:
				for i in lst:
					tileNum = i
					if tileNum > columns and (tileNum%columns) != 0:
						if squares[int(tileNum-(columns+1))].getBomb() or int(tileNum-(columns+1)) in seen:
							pass
						else:
							if squares[int(tileNum)].bombsNear == 0:
								if int(tileNum-(columns+1)) not in lst and squares[int(tileNum-(columns+1))].bombsNear == 0:
									lst.append(int(tileNum-(columns+1)))
								seen.append(int(tileNum-(columns+1)))
								squares[int(tileNum-(columns+1))].reveal(int(tileNum-(columns+1)))
					if tileNum > columns:
						if squares[int(tileNum-columns)].getBomb() or int(tileNum-columns) in seen:
							pass
						else:
							if squares[int(tileNum)].bombsNear == 0:
								if int(tileNum-columns) not in lst and squares[int(tileNum-columns)].bombsNear == 0:
									lst.append(int(tileNum-columns))
								seen.append(int(tileNum-columns))
								squares[int(tileNum-columns)].reveal(int(tileNum-columns))
					if tileNum > columns and (tileNum%columns) != 8:
						if squares[int(tileNum-(columns-1))].getBomb() or int(tileNum-(columns-1)) in seen:
							pass
						else:
							if squares[int(tileNum)].bombsNear == 0:
								if int(tileNum-(columns-1)) not in lst and squares[int(tileNum-(columns-1))].bombsNear == 0:
									lst.append(int(tileNum-(columns-1)))
								seen.append(int(tileNum-(columns-1)))
								squares[int(tileNum-(columns-1))].reveal(int(tileNum-(columns-1)))
					if (tileNum%columns) != 8:
						if squares[int(tileNum+1)].getBomb() or int(tileNum+1) in seen:
							pass
						else:
							if squares[int(tileNum)].bombsNear == 0:
								if int(tileNum+1) not in lst and squares[int(tileNum+1)].bombsNear == 0:
									lst.append(int(tileNum+1))
								seen.append(int(tileNum+1))
								squares[int(tileNum+1)].reveal(int(tileNum+1))
					if (tileNum%columns) != 8 and tileNum <= (rows*columns)-(columns+1):
						if squares[int(tileNum+columns+1)].getBomb() or int(tileNum+columns+1) in seen:
							pass
						else:
							if squares[int(tileNum)].bombsNear == 0:
								if int(tileNum+columns+1) not in lst and squares[int(tileNum+columns+1)].bombsNear == 0:
									lst.append(int(tileNum+columns+1))
								seen.append(int(tileNum+columns+1))
								squares[int(tileNum+columns+1)].reveal(int(tileNum+columns+1))
					if tileNum <= (rows*columns)-(columns+1):
						if squares[int(tileNum+columns)].getBomb() or int(tileNum+columns) in seen:
							pass
						else:
							if squares[int(tileNum)].bombsNear == 0:
								if int(tileNum+columns) not in lst and squares[int(tileNum+columns)].bombsNear == 0:
									lst.append(int(tileNum+columns))
								seen.append(int(tileNum+columns))
								squares[int(tileNum+columns)].reveal(int(tileNum+columns))
					if tileNum <= (rows*columns)-(columns+1) and (tileNum%columns) != 0:
						if squares[int(tileNum+columns-1)].getBomb() or int(tileNum+columns-1) in seen:
							pass
						else:
							if squares[int(tileNum)].bombsNear == 0:
								if int(tileNum+columns-1) not in lst and squares[int(tileNum+columns-1)].bombsNear == 0:
									lst.append(int(tileNum+(columns-1)))
								seen.append(int(tileNum+(columns-1)))
								squares[int(tileNum+(columns-1))].reveal(int(tileNum+columns-1))
					if (tileNum%columns) != 0:
						if squares[int(tileNum-1)].getBomb() or int(tileNum-1) in seen:
							pass
						else:
							if squares[int(tileNum)].bombsNear == 0:
								if int(tileNum-1) not in lst and squares[int(tileNum-1)].bombsNear == 0:
									lst.append(int(tileNum-1))
								seen.append(int(tileNum-1))
								squares[int(tileNum-1)].reveal(int(tileNum-1))
					lst.remove(i)
				if len(lst) == 0:
					break
		elif key == "f":
				click = win.getMouse()
				xPixels = click.getX()
				yPixels = click.getY()
				x = (xPixels)//(width/columns)
				y = (yPixels)//(height/rows)
				tileNum = x+(y*columns)
				if squares[int(tileNum)].getRevealed():
					pass
				else:
					squares[int(tileNum)].flag(tileNum)
	if end == "bomb":
		newWin = GraphWin("Solved Minesweeper", width, height)
		newSquares = returnSquares(tileInfo, newWin)
		createGrid(newWin)
		for i in range(rows*columns):
			newSquares[i].reveal(i)
		newWin.getMouse()
	else:
		for i in bombs:
			if not squares[i].getFlagged():
				squares[i].reveal(i)
		newWin = GraphWin("CONGRATS", width, height)
		x = width/2
		y = height/2
		p = Point(x, y)
		winTextBox = Text(p, "CONGRATS: YOU WIN!")
		winTextBox.draw(newWin)
		newWin.getMouse()

main()
