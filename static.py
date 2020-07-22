import argparse
from tkinter import Tk, Frame, Menu, filedialog
import time
# from lib.fileDetails import getFileSize
from lib.fileDetails import getFileCreationDateTime

banner = """
  /\//    __        __  _     /\//
 //\/____/ /_____ _/ /_(_)___//\/ 
   / ___/ __/ __ `/ __/ / ___/    
  (__  ) /_/ /_/ / /_/ / /__      
 /____/\__/\__,_/\__/_/\___/   
 """



class Window(Frame):
	currentFile = ''

	def __init__(self):
		super().__init__()

		self.initUI()


	def initUI(self):
		self.master.title("~static~")
		menubar = Menu(self.master)
		self.master.config(menu=menubar)
		fileMenu = Menu(menubar)
		fileMenu.add_command(label="Open", command=self.openFile)
		fileMenu.add_command(label="Exit", command=self.onExit)
		menubar.add_cascade(label="File", menu=fileMenu)


	def openFile(self):
		currentFile = filedialog.askopenfilename() 
		print(currentFile)


	def onExit(self):
		self.quit()


def main():
	print(banner)
	root = Tk()
	root.geometry("500x500+300+300")
	app = Window()
	root.mainloop()


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Static Malware Analysis")
	parser.add_argument('-f', "--file", help="File", type=str)
	args = parser.parse_args()
	main()