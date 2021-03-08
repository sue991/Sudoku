import random

class Reader:

	#상중하 입력받고 빈칸 개수 정하기
	def get_level():
		level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
		while level not in {"상","중","하"}: #다른값 입력받는것 방지
			level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
		if level == "상":
			return 40
		elif level == "중":
			return 34
		elif level == "하":
			return 28


class Sudoku:

	def __init__(self,size):
		self.board = self.create_board() #board를 보드 만들기로 입력
	#	self.__hole = self.make_holes(self.__board,size) #보드와 구멍 개수를 입력해 구멍 만들어 hole로 입력


	#랜덤으로 보드 만들기
	@staticmethod
	def create_board():
		seed = [1,2,3,4,5,6,7,8,9]
		random.shuffle(seed) #seed 리스트 값 무작위로 배치 바꾸기
		n1 = seed[0]
		n2 = seed[1]
		n3 = seed[2]
		n4 = seed[3]
		n5 = seed[4]
		n6 = seed[5]
		n7 = seed[6]
		n8 = seed[7]
		n9 = seed[8]
		return [[n1, n2, n3, n4, n5, n6, n7, n8, n9],
				[n4, n5, n6, n7, n8, n9, n1, n2, n3],
				[n7, n8, n9, n1, n2, n3, n4, n5, n6],
				[n2, n3, n1, n5, n6, n4, n8, n9, n7],
				[n5, n6, n4, n8, n9, n7, n2, n3, n1],
				[n8, n9, n7, n2, n3, n1, n5, n6, n4],
				[n3, n1, n2, n6, n4, n5, n9, n7, n8],
				[n6, n4, n5, n9, n7, n8, n3, n1, n2],
				[n9, n7, n8, n3, n1, n2, n6, n4, n5]]


	#범위 내에 있는 숫자인지 판단하기
	@staticmethod
	def get_integer(message, i, j):
		number = input(message) #숫자 입력받기 i = 1, j = 9
		while not (number.isdigit() and i <= int(number) <= j):
			number = input(message)
		return int(number)

	#구멍 뚫기(구멍은 0)
	@staticmethod
	def make_holes(board, no_of_holes):
		holeset = set() #????
		while no_of_holes > 0:
			i = random.randint(0,8) #0-8 중 무작위로 하나 뽑기
			j = random.randint(0,8) #0-8 중 무작위로 하나 뽑기
			if board[i][j] != 0: #빈칸 아닐경우
				board[i][j] = 0 #빈칸으로 만들기
				holeset.add((i,j)) #빈칸으로 바꾼 좌표 저장
				no_of_holes -= 1
		return (board,holeset) #보드와 빈칸 좌표

	#섞어버리기 
	@staticmethod
	def shuffle_ribbons(board):
		top = board[:3] #위 세 줄
		middle = board[3:6]	#가운데 세 줄
		bottom = board[6:]	#아래 세 줄
		random.shuffle(top)	#top 섞기
		random.shuffle(middle)	#middle 섞기
		random.shuffle(bottom)	#bottom 섞기
		return top + middle + bottom


	#보드 옮기기
	@staticmethod
	def transpose(board):
		transposed = []
		for _ in range(len(board)): #보드의 길이만큼 돌리기
			transposed.append([]) #리스트에 보드 길이만큼 [] 붙이기 
		for row in board: #보드에 있는 숫자 차례로 돌리기
			i = 0
			for entry in row: 
				transposed[i].append(entry) #리스트 i번째 칸에 각 숫자 대입
				i += 1
		return transposed

	#보드 베끼기
	@staticmethod
	def copy_board(board):
		board_clone = []
		for row in board:
			row_clone = row[:]
			board_clone.append(row_clone)
		return board_clone

	#보드 보여주기
	@staticmethod
	def show_board(board):
		print()
		print('S', '|', '1', '2', '3', '4', '5', '6', '7', '8', '9')
		print('-', '+', '-', '-', '-', '-', '-', '-', '-', '-', '-')
		i = 1
		for row in board:
			print(i, end=' ')
			print('|', end=' ')
			for entry in row: #보드 각각 숫자 보여주기
				if entry == 0:
					print('.', end=' ') # 빈칸일 경우 '.''
				else:
					print(entry, end=' ')
			print()
			i += 1
		print()

	#답지보드 만들기
	@staticmethod
	def create_solution_board(size):
		board = Sudoku.create_board()
		board = Sudoku.shuffle_ribbons(board)
		board = Sudoku.transpose(board)
		board = Sudoku.shuffle_ribbons(board)
		board = Sudoku.transpose(board)
		return board

class SudokuController:

	def __init__(self,size):
		self.__size = size #구멍 개수 
		self.Sudoku1 = Sudoku(self.__size) #class Sudoku 저장 
		self.__solution = self.Sudoku1.create_solution_board(size) #답지함수 저장
		self.__no_of_holes = self.__size # 구멍개수를 다시 no_of_holes로 저장
		self.__puzzle = self.Sudoku1.copy_board(self.__solution) #답지를 puzzle로 저장
		(self.__puzzle, self.__holeset) = Sudoku.make_holes(self.__puzzle, self.__no_of_holes)
		#퍼즐에 구멍의 개수만큼 구멍을 만들기

	#실행
	def play(self):	
		Sudoku.show_board(self.__puzzle) #퍼즐 보이기
		while self.__no_of_holes > 0: #
			i = Sudoku.get_integer("가로줄번호(1~9): ", 1, 9) - 1 
			j = Sudoku.get_integer("세로줄번호(1~9): ", 1, 9) - 1
			if (i, j) not in self.__holeset:
				print("빈칸이 아닙니다.")
				continue
			n = Sudoku.get_integer("숫자(1~9): ", 1, 9)
			sol = self.__solution[i][j] #답지함수의 몇번째 칸
			if n == sol:
				self.__puzzle[i][j] = sol #퍼즐에 대입
				Sudoku.show_board(self.__puzzle) #대입한 퍼즐로 다시 보이기
				self.__holeset.remove((i, j)) #대입했으니 빈칸 좌표 지우기
				self.__no_of_holes -= 1 #빈칸 개수 지우기

			else:
				print(n, "가 아닙니다. 다시 해보세요.")
		print("잘 하셨습니다. 또 들려주세요.")		



def main():
	size = Reader.get_level() #상중하에 따른 구멍 개수를 size로 저장
	SudokuController(int(size)).play() 



main()