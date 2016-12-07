from Tkinter import *
#Function for generating number of tries based on difficulty
def tries_generator(diff):
	if(diff==5):
		tries=6
	if(diff==6):
		tries=5
	if(diff==7):
		tries=4
	return tries

#Functions for main game window menu
def about():
	popup=Tk()
	msg="CREDITS:\nBANDARU MAHIDHAR- IMT2016070\nSWAPNIL BUCHKE- IMT2016085\nPAVAN KUMAR REDDY POTHULA- IMT2016127"
	label=Label(popup,text=msg,font="Verdana 10 bold",bg="#1A5276")
	label.pack()
	popup.resizable(0,0)
	popup.title('ABOUT')
	popup.mainloop()
def instructions():
	popup=Tk()
	msg="INSTRUCTIONS:\n 1. ENTER LETTERS ONE BY ONE OR A COMPLETE WORD AT ONCE\n 2. IF THE LETTER(S) EXISTS IN THE WORD THOSE LETTERS GET FILLED IN THE RIGHT PLACE.\n 3. OTHERWISE YOUR TRIES DECREASE\n 4. WHEN YOU RUN OUT OF TRIES THE MAN IS HANGED AND YOU LOSE\n 5. IF YOU CAN GUESS THE WORD BEFORE THAT YOU WIN"
	label=Label(popup,text=msg,font="Verdana 10 bold",bg="#1A5276")
	label.pack()
	popup.resizable(0,0)
	popup.title('INSTRUCTIONS')
	popup.mainloop()
