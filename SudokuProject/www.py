import random
from tkinter import *
from PIL import Image, ImageTk
font_a = 'times 20 bold italic'

class App(Frame):
	def __init__(self,master):
		super().__init__(master)
		self.pack(padx=10,pady=200)
		self.start()
		self.master = master
		self.configure(bg='black')

		#각각 숫자 적힌 카드 리스트에 붙이기
		self.photo = []
		self.photo.append(ImageTk.PhotoImage(Image.open("block.gif")))
		for i in range(1,10):
			self.photo.append(ImageTk.PhotoImage(Image.open(str(i)+".gif")))

		self.photo1 = []
		self.photo1.append(ImageTk.PhotoImage(Image.open("block.gif")))
		for i in range(1,10):
			self.photo1.append(ImageTk.PhotoImage(Image.open(str(i)+"-1.gif")))
	



	def start(self):
		"""Game Start"""
		self.title = Label(self)
		self.title["text"] = "Sudoku"
		self.title["font"] ='times 90 bold italic'
		self.title["bg"] = 'black'
		self.title["fg"] = 'white' 
		self.title.grid(row = 0,column = 1)

		self.start0 = Button(self)
		self.start0["text"] = "Game Start"
		self.start0["font"] = font_a
		self.start0["bg"] = 'black'
		self.start0["fg"] = 'white'
		self.start0["command"] =self.select_level
		self.start0.grid(row=1,column=1)
		self.start0.configure(bg='black')


		self.exit = Button(self)
		self.exit["text"] = "Exit Game"
		self.exit["font"] = font_a
		self.exit["bg"] = 'black'
		self.exit["fg"] = 'white'
		self.exit["command"] = self.quit
		self.exit.grid(row=2,column=1)
		self.exit.configure(bg='black')

	
	def select_level(self):
		"""Select Level"""
		self.start0.grid_forget()
		self.exit.grid_forget()

		self.num = Label(self)
		self.num["text"] = "level"
		self.num["font"] = 'times 30 italic'
		self.num["bg"] = 'black'
		self.num["fg"] = 'white'
		self.num.grid(row = 1,column=1)


		self.back0 = Button(self)
		self.back0["text"] = "Back"
		self.back0["font"] = 'times 20 italic'
		self.back0["bg"] = 'black'
		self.back0["fg"] = 'white'
		self.back0["command"] = self.back
		self.back0.grid(row=4,column=4)
		self.back0.configure(bg='black')

		self.a = Button(self,bg='black',fg='white',text = "Hard",command=self.get_level1 ,font = font_a)
		self.a.grid(row=3,column=0)
		self.b = Button(self,bg='black',fg='white',text = "Normal",command=self.get_level2 ,font = font_a)
		self.b.grid(row=3,column=1)
		self.c = Button(self,bg='black',fg='white',text = "Easy",command=self.get_level3 ,font = font_a)
		self.c.grid(row=3,column=2)

	def back(self):
		self.num.grid_forget()
		self.title.grid_forget()
		self.a.grid_forget()
		self.b.grid_forget()
		self.c.grid_forget()
		self.back0.grid_forget()
		self.start()

	def get_level1(self):
		self.pack(padx=10,pady=20)
		self.back0.grid_forget()
		self.num.grid_forget()
		self.a.grid_forget()
		self.b.grid_forget()
		self.c.grid_forget()
		self.title.grid_forget()
		self.make_holes(40)
		

	def get_level2(self):
		self.pack(padx=10,pady=20)
		self.back0.grid_forget()
		self.num.grid_forget()
		self.a.grid_forget()
		self.b.grid_forget()
		self.c.grid_forget()
		self.title.grid_forget()
		self.make_holes(34)
		

	def get_level3(self):
		self.pack(padx=10,pady=20)
		self.back0.grid_forget()
		self.num.grid_forget()
		self.a.grid_forget()
		self.b.grid_forget()
		self.c.grid_forget()
		self.title.grid_forget()
		self.make_holes(1)


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

	#보드 베끼기
	@staticmethod
	def copy_board(board):
		board_clone = []
		for row in board:
			row_clone = row[:]
			board_clone.append(row_clone)
		return board_clone

	@staticmethod
	def shuffle_ribbons(board):
		top = board[:3]		#위 세 줄
		middle = board[3:6]   #가운데 세 줄
		bottom = board[6:]   #아래 세 줄
		random.shuffle(top)   #top 섞기
		random.shuffle(middle)   #middle 섞기
		random.shuffle(bottom)   #bottom 섞기
		return top + middle + bottom

	#구멍 뚫기(구멍은 0)
	def make_holes(self,no_of_holes):
		self.no_of_holes = no_of_holes
		self.solution = self.create_solution_board()
		self.__puzzle = self.copy_board(self.solution)
		board = self.__puzzle
		holeset = set() #????
		while no_of_holes > 0:
			i = random.randint(0,8) #0-8 중 무작위로 하나 뽑기
			j = random.randint(0,8) #0-8 중 무작위로 하나 뽑기
			if board[i][j] != 0: #빈칸 아닐경우
				board[i][j] = 0 #빈칸으로 만들기
				holeset.add((i,j)) #빈칸으로 바꾼 좌표 저장
				no_of_holes -= 1
		self.create_canvas(board)
		return (board,holeset) #보드와 빈칸 좌표


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


	@staticmethod
	def copy_board(board):
		board_clone = []
		for row in board:
			row_clone = row[:]
			board_clone.append(row_clone)
		return board_clone


	
	def create_solution_board(self):
		board = self.create_board()
		board = self.shuffle_ribbons(board)
		board = self.transpose(board)
		board = self.shuffle_ribbons(board)
		board = self.transpose(board)
		return board



	#작은 창 띄우기
	def little_square(self,x,y,board):
		self.window = Toplevel(self.master)
		self.window.geometry("200x150")
		self.window.title("Select Button")
		number = [0,1,2,3,4,5,6,7,8,9]
		n = 1
		for i in range(3):
			for j in range(3):
				a = number[n]
				self.button = Button(self.window,width=4,height=2, text =a, command = lambda a = a: self.reflect(a,board,x,y))
				self.button.grid(row=i,column=j)
				n += 1


	#보드에 반영하기
	def reflect(self, num, board,x,y):
		self.window.destroy()
		board[x][y] = num #보드의 숫자
		self.no_of_holes -= 1
		self.button_list[x][y] = Button(self,width=50,height=50,image=self.photo1[num])

		self.button_list[x][y]["command"] = lambda x=x ,y=y : self.little_square(x,y,board)

		self.button_list[x][y].grid(row=x,column=y)

		#보드가 꽉 찼을 경우
		if self.no_of_holes == 0:
			self.ok_button["state"] = NORMAL



	#답이랑 맞는지 확인
	def sol_check(self,board):
		clear = True
		for i in range(9):
			for j in range(9):
				if board[i][j] != self.solution[i][j]:
					clear = False

		if clear: # 창 생성
			self.ok = Toplevel(self.master,relief='groove')
			self.ok.geometry("300x100")
			self.ok.title("Finish")
			self.label = Label(self.ok,text = "Great!",font='times 25 bold italic',height=2,width=5,justify=CENTER)
			self.label.place(x=120,y=10)

			self.button = Button(self.ok,text="quit",width=30,command=self.quit,justify=CENTER).place(y=60)


			



	def create_canvas(self,board):
		#버튼리스트 [] 으로 만들기
		self.button_list = []
		for _ in range(9):
			self.button_list.append([])
		for i in range(9):
			for j in range(9):
				self.button_list[i].append([])

		#각각 돌리면서 버튼리스트에 버튼 이미지 넣기
		for i in range(9):
			for j in range(9):
	
				if board[i][j] == 0:#빈칸
					self.button = Button(self,width=50,height=50,image=self.photo[0])
					self.button.grid(row=i,column=j)
					self.button_list[i][j] = self.button

				else:
					num = board[i][j] #보드에 적힌 숫자
					self.button = Button(self,width=50,height=50,image=self.photo[num])
					self.button.grid(row=i,column=j)
					self.button_list[i][j] = self.button

		#빈칸 버튼을 누르면 실행
		for i in range(9):
			for j in range(9):
				if board[i][j] == 0:
					self.button_list[i][j]["command"] =  lambda i=i,j=j : self.little_square(i,j,board)
#					self.button_list[i][j]["command"] =  self.little_square -> 오류 발생
	

		#제출 버튼(평소엔 누르기 불가능)
		self.ok_button = Button(self,width=6, text= "SUBMIT",state = DISABLED)
		self.ok_button.grid(row=10,column=10)
		self.ok_button["command"] = lambda : self.sol_check(board)
		

		return self.button_list



######################################
root = Tk()
root.title("Sudoku")
root.geometry("700x700")
root.configure(bg='black')
app = App(root)
app.mainloop()