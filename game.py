from Tkinter import *
from showhangman import Hangman
import tkMessageBox
#Starts the main game
def startgame(secret, tryvalue, setup):
	global tries
	tries=tryvalue
	check=[]
	word=[]
	letters_entered=[]
	entry=StringVar()
	triesleft=StringVar()
	lettersentered=StringVar()
	wordyet=StringVar()
	wordyet.set("_ "*len(secret))
	lettersentered.set("LETTERS ENTERED: "+str(" ".join(letters_entered)))
	triesleft.set("TRIES LEFT= "+str(tries))
	for i in secret:
		if i not in check:
			check.append(i)
	setup.withdraw()
	game=Toplevel()
	game.resizable(0,0)
	game.configure(background='#1A5276')
	game.title="HANGMAN"
	pic=PhotoImage(file="gallows.gif")
	label_image=Label(game,image=pic,bg='#1A5276')
	label_image.image=pic
	label_image.grid(row=0,columnspan=2,sticky=W)
	hangman=Hangman(label_image)
	label_letters_entered=Label(game,textvariable=lettersentered,bg='#1A5276',font="Verdana 12 bold").grid(row=1,sticky=W)
	label_word=Label(game,textvariable=wordyet,bg='#1A5276',font="Verdana 12 bold").grid(row=0,column=2)
	entrybox=Entry(game,textvariable=entry).grid(row=3,sticky=W)
	label_tries=Label(game,textvariable=triesleft,bg='#1A5276',font="Verdana 12 bold").grid(row=3,column=2,sticky=E)
	letterguessbutton=Button(game,text="GUESS LETTER",command=lambda:letterguess(hangman,wordyet,lettersentered,triesleft,entry.get(),letters_entered,secret,word,check,game),font="Verdana 12 bold",bg="#1E8449").grid(row=4,sticky=W)
	wordguessbutton=Button(game,text="GUESS WORD (ONLY ONCE)",command=lambda:win_lose_wordguessbutton(game,entry.get(),secret,hangman),font="Verdana 12 bold",bg="#1E8449").grid(row=4,column=2)
	game.mainloop()

def win_lose_wordguessbutton(window, enteredstring, secret,hangman):
	global tries
	if len(enteredstring)<1:
		tkMessageBox.showinfo("NO INPUT", "Please enter something")
	else:
		if(enteredstring.upper()==secret):
			tkMessageBox.showinfo("WIN", "YOU WIN! The word was "+secret)
			window.withdraw()
		else:
			tries=0
			hangman.showhangman(tries)
			tkMessageBox.showinfo("LOST", "GAME OVER\nYou lost! The word was "+secret)
			window.withdraw()

def letterguess(hangman,wordyet,lettersentered,triesleft,letter,letters_entered,secret,word,check,game):
	global tries
	if len(letter)<1:
		tkMessageBox.showinfo("NO INPUT", "Please enter something")
	else:
		letter=letter[0].upper()
		if letter in letters_entered:
			tkMessageBox.showinfo("ALREADY ENTERED", "You have already entererd this letter")
		else:
			letters_entered.append(letter)
			lettersentered.set("LETTERS ENTERED: "+str("".join(letters_entered)))
			if letter in secret:
				word.append(letter)
				if(sorted(word)==sorted(check)):
					game.withdraw()
					tkMessageBox.showinfo("WIN", "YOU WIN! The word was "+secret)
			else:
				tries-=1
				triesleft.set("TRIES LEFT= "+str(tries))
				hangman.showhangman(tries)
	if(tries==0):
		tkMessageBox.showinfo("LOST", "GAME OVER\nYou lost! The word was "+secret)
		game.withdraw()
	l=map(lambda x:x if x in word else '_',list(secret))
	wordyet.set(str(" ".join(l)))
