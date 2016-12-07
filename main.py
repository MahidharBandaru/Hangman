from Tkinter import *
import random
from game import *
from tries import *

#Generates words
def word_generator(num,tries,window):
	if(num==1):
		listofwords=["PEOPLE","HISTORY","INFORMATION","GOVERNMENT","COMPUTER","SYSTEM","HEALTH","UNDERSTAND","UNCOPYRIGHTABLE","PROXIMITY","publisher","cramp","composite","homework","glasses","blush","spill","intern","sweater","dart","kneel","fiddle","hatch","wrench","shrub","hike","quarter","grin","windmill","juggler"]
		num=random.randint(0,len(listofwords)-1)
		return listofwords[num].upper()
	elif(num==2):
		listofwords=["ELEPHANT","ALLIGATOR","EAGLE","DOLPHIN","JELLYFISH","NUDIBRANCH","STARFISH","SEAGULL","SQUIRREL","hippopotamus","grasshopper","dodo","anteater","rhinoceros","hamster","catfish","seahorse","starfish","panther","chameleon","stingray","cockroach","reindeer","salmon","tadpole","flamingo","shrimp","tortoise"]
		num=random.randint(0,len(listofwords)-1)
		return listofwords[num].upper()
	elif(num==3):
		listofwords=["BRAZIL","INDIA","AMERICA","ARGENTINA","GERMANY","SPAIN","PORTUGAL","PAKISTAN","CHINA","Afghanistan","Algeria","Bulgaria","Bolivia","Denmark","Ethiopia","Fiji","Georgia","Guinea","Israel","Jamaica","Kuwait","Maldives","Morocco","Mozambique","Namibia","Philippines","Paraguay","Qatar","Somalia","Sudan","Vietnam","Zambia","Uganda","Turkey","Thailand","Sweden","Romania","Panama","Nigeria","Norway","Monaco","Libya","Kuwait","Greece","Chile"]
		num=random.randint(0,len(listofwords)-1)
		return listofwords[num].upper()
	elif(num==4):
		listofwords=["Mathematics","PHYSICS","CHEMISTRY","BIOLOGY","BIOTECHNOLOGY","ENGINEERING","HISTORY","GEOGRAPHY","PSYCHOLOGY","SOCIOLOGY","ECONOMICS","Management","Accounting","aeronautics","anatomy","astrology","astrophysics","bibliology","biometrics","carcinology","cardiology","cosmology","ecology","electrology","floristry","geology","kinetics","lexicology","mythology","neurology","oceanology"]
		num=random.randint(0,len(listofwords)-1)
		return listofwords[num].upper()
	elif(num==8):
		wordentry=Toplevel()
		wordentry.resizable(0,0)
		word=StringVar()
		wordentry.title="HANGMAN"
		entrybox=Entry(wordentry,textvariable=word).grid(row=0)
		window.withdraw()
		submitbutton=Button(wordentry,text="SUBMIT",command=lambda:startgame(word.get().upper(),tries,wordentry)).grid(row=1)
		wordentry.mainloop()

#Makes the game-setup window
def gamesetup():
	setup=Toplevel()
	setup.resizable(0,0)
	setup.configure(background='#1A5276')
	setup.title="HANGMAN"
	word_var=IntVar()
	word_var.set(1)
	diff_var=IntVar()
	diff_var.set(5)
	label=Label(setup,text="GAME SETUP",font="Verdana 20 bold",bg='#1A5276',fg="#B03A2E").grid(row=0,columnspan=2)
	rb1=Radiobutton(setup,text="GENERAL ENGLISH",value=1,variable=word_var,bg='#1A5276',font="Verdana 20 bold").grid(row=1,sticky=W)
	rb2=Radiobutton(setup,text="ANIMALS",value=2,variable=word_var,bg='#1A5276',font="Verdana 20 bold").grid(row=2,sticky=W)
	rb3=Radiobutton(setup,text="COUNTRIES",value=3,variable=word_var,bg='#1A5276',font="Verdana 20 bold").grid(row=3,sticky=W)
	rb4=Radiobutton(setup,text="STREAMS OF STUDY",value=4,variable=word_var,bg='#1A5276',font="Verdana 20 bold").grid(row=4,sticky=W)
	rb5=Radiobutton(setup,text="EASY",value=5,variable=diff_var,bg='#1A5276',font="Verdana 20 bold").grid(row=1,column=1,sticky=W)
	rb6=Radiobutton(setup,text="MEDIUM",value=6,variable=diff_var,bg='#1A5276',font="Verdana 20 bold").grid(row=2,column=1,sticky=W)
	rb7=Radiobutton(setup,text="HARD",value=7,variable=diff_var,bg='#1A5276',font="Verdana 20 bold").grid(row=3,column=1,sticky=W)
	rb8=Radiobutton(setup,text="ENTER WORD (TWO PLAYERS)",value=8,variable=word_var,bg='#1A5276',font="Verdana 20 bold").grid(row=5,sticky=W)
	playbutton=Button(setup,text="START",bg="#1E8449",font="Verdana 20 bold")
	if(word_var.get()!=8):
		playbutton.configure(command=lambda:startgame(word_generator(word_var.get(),tries_generator(diff_var.get()),setup),tries_generator(diff_var.get()),setup))
	else:
		playbutton.configure(command=lambda:word_generator(word_var.get(),tries_generator(diff_var.get()),setup))
	playbutton.grid(row=6,columnspan=2)
	setup.mainloop()

#Main game window
root=Tk()
root.resizable(0,0)
img = PhotoImage(file='dead.gif')
root.tk.call('wm', 'iconphoto', root._w, img)
root.configure(background='#1A5276')
root.title("HANGMAN")
label1=Label(root,text="****HANGMAN****",font="Verdana 40 bold",bg="#1A5276",fg="#B03A2E").grid(row=0,columnspan=2)
pic=PhotoImage(file="dead.gif")
label2=Label(root,image=pic).grid(row=1,columnspan=2)
playbutton=Button(root,text="PLAY",width=20,command=gamesetup,font="Verdana 20 bold",bg="#1E8449").grid(row=2,column=0)
quitbutton=Button(root,text="QUIT",command=root.destroy,width=20,font="Verdana 20 bold",bg="#1E8449").grid(row=2,column=1)
#Menu
helpmenu=Menu(root)
root.config(menu=helpmenu)
submenu=Menu(helpmenu)
switch_menu=Menu(root)
helpmenu.add_cascade(label="Help", menu=submenu)
submenu.add_command(label="Instructions",command=instructions)
submenu.add_command(label="About",command=about)
submenu.add_command(label="Exit", command=root.destroy)
root.mainloop()
