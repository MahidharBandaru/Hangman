from Tkinter import *
#Class for the display of hangman
class Hangman:
	def __init__(self,label):
		self.label=label
	def showhangman(self,tries):
		if(tries==5):
			pic=PhotoImage(file="head.gif")
			self.label.configure(image=pic)
			self.label.image=pic
		elif(tries==4):
			pic=PhotoImage(file="noarms.gif")
			self.label.configure(image=pic)
			self.label.image=pic
		elif(tries==3):
			pic=PhotoImage(file="rightarm.gif")
			self.label.configure(image=pic)
			self.label.image=pic
		elif(tries==2):
			pic=PhotoImage(file="nolegs.gif")
			self.label.configure(image=pic)
			self.label.image=pic
		elif(tries==1):
			pic=PhotoImage(file="almostdead.gif")
			self.label.configure(image=pic)
			self.label.image=pic
		elif(tries==0):
			pic=PhotoImage(file="dead.gif")
			self.label.configure(image=pic)
			self.label.image=pic
