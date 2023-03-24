from tkinter import *
import random
from random import shuffle
from PIL import ImageTk, Image
import pygame
import winsound 

pygame.init()

score = 0
flag=0
root = Tk()  # object of main window
root.iconbitmap(r'Images\\logo.ico')
soundstatus=1
frame = Frame(root, width=520, height=350 )

var1=IntVar()
var2=IntVar()
var3=IntVar()

root.title("The LOGO Game ")
i0 = "realmadrid.png"
i1 = "adidas.png"
i2 = "mercedes.png"
i3 = "whatsapp.png"
i4 = "instagram.png"
i5 = "android.png"
i6 = "dominos.png"
i7="apple.png"
i8="asus.png"
i9="Blackberry.png"
i10="Fastrack.png"
i11="Microsoft.png"
i12="Pepsi.png"
i13="porsche.png"
i14="Skullcandy.png"
i15="spotify.png"
i16="Starbucks.png"
i17="Tesla.png"
i18="Unity.png"
i19="Unreal.png"
i20="python.png"
i21="youtube.png"
i22="chatgpt.jpg"
i23="twitter.png"
musicflag=1

list1 = []
list = [[i0, "Real Madrid"], [i1, "Adidas"], [i2, "Mercedes"], [i3, "Whatsapp"], [i4, "Instagram"], [i5, 'Android'],
		[i6, 'Dominos'],[i7,"Apple"],[i8,"Asus"],[i9,"BlackBerry"],[i10,"Fastrack"],[i11,"Microsoft"],[i12,"Pepsi"],[i13,"Porsche"],[i14,"Skullcandy"],
		[i15,"Spotify"],[i16,"Starbucks"],[i17,"Tesla"],[i18,"Unity"],[i19,"Unreal"],[i20,"Python"],[i21,'Youtube'],[i22,"Chat GPT"],[i23,"Twitter"]]
list2 = [['Real Madrid', 'Barcelona', 'AC Milan', 'Arsenal'], 
         ['Nike', 'Puma', 'Reebok', 'Adidas'],
         ['Mercedes', 'Ferrari', 'Audi', 'Ford'], 
         ['Hike', 'Whatsapp', 'Telegram', 'Line'],
         ['Snapchat', 'Instagram', 'Whatsapp', 'Facebook'],
         ['Android', 'Windows', 'Microsoft', 'Symbian'], 
         ['Dominos', 'Pizza Hut', 'Burger King', 'McDonalds'],
         ['Apple','Samsung','One Plus','Google'],
         ['Asus','Hp','Lenovo','Acer'],
         ['BlackBerry','Nokia','Samsung','Apple'],
         ['Fastrack','Fossil','Titan','Casio'],
         ['Apple','Google','Amazon','Microsoft'],
         ['Pepsi','Coke','Coca Cola','Fanta'],
         ['Porsche','Mustang','BMW','Jaguar'],
         ['Skullcandy','JBL','Boat','Sony'],
         ['Spotify','Pandora','Gaana','Saavn'],
         ['Starbucks','CCD','Costa Coffee','Dunkin Donuts'],
         ['Tesla','Audi','Toyota','Bentley'],
         ['Unity','Unreal','Gnome','Cryengine'],
         ['Unreal','Game Maker','Corona','Unity'],
         ['Python','R language','C++','C#'],
         ['Youtube','Google','Tubudy','None of these'],
         ['Web browser','Flower','Chat GPT',"Updated Google"],
         ['Twitter','Instagram','Snapchat','Facebook']
         ]
#print(len(list2))
f_obj = open("highscore.txt", "r")
f_inst=open("instructions.txt","r")
hscore = int(f_obj.read())
instructions=f_inst.read()
#instructions=instructions.strip()

def showimage():

	def button_event(text, x):
		if text == list[x][1]:
			global score, hscore
			score = score + 1;#print("CURRENT SCORE: ", score)

			if hscore < score:
				f_obj = open("highscore.txt", "w")

				hscore = score
				# print("HIGHSCORE:", hscore)
				f_obj.write(str(score))
				f_obj.close()
			else:
				# print("HIGHSCORE", hscore)
			
			# print("correct")
			 
				answer=1
				sound(answer)
				frame1.destroy()
				showimage()
		else:
			# print("Wrong")
			frame1.destroy()
			
			answer=0
			sound(answer)
			frame3=Frame(root,width=500,height=330)
			canvas3=Canvas(frame3,width=600,height=400,bg="lightblue")
			
			canvas3.create_text(300,80,text="You Lose!!!!",fill="red",font=("Times",30))
			canvas3.create_text(300,150,text="Better Luck Next Time",fill="red",font=("Times",30))
			canvas3.create_text(300,225,text="Your Score: "+str(score),fill="darkblue",font=("Times",30))
				
			restart_but1 = Button(frame3, text="Play again", width=15, height=2, command=lambda: restart(frame3))
			restart_but1.place(x=135, y=300)
			exit_but1=Button(frame3, text="Quit", width=15, height=2, command=exit)
			exit_but1.place(x=360, y=300)
			canvas3.pack()
			frame3.pack()

	def showbuttons(n):
		if musicflag == 0:
			val=1
		else:
			val=0
		cbut_music1 = Checkbutton(frame1, text="Music",variable=var1,onvalue=val,offvalue=not val,command=music)
		cbut_music1.place(x=520,y=3)
		
		cbut_sound = Checkbutton(frame1, text="Sound",variable=var2,onvalue=0,offvalue=1,command=soundflag)
		cbut_sound.place(x=450,y=3)	
		
		shuffle(list2[n])
		x1=40
		y1=290
		option1 = Button(frame1, text=list2[n][0], width=34, height=2, command=lambda: button_event(list2[n][0], n))
		option1.place(x=x1, y=y1)

		x2=310
		y2=290
		option2 = Button(frame1, text=list2[n][1], width=34, height=2, command=lambda: button_event(list2[n][1], n))
		option2.place(x=x2, y=y2)
		
		x3=40
		y3=345
		option3 = Button(frame1, text=list2[n][2], width=34, height=2, command=lambda: button_event(list2[n][2], n))
		option3.place(x=x3, y=y3)
		
		x4=310
		y4=345
		option4 = Button(frame1, text=list2[n][3], width=34, height=2, command=lambda: button_event(list2[n][3], n))
		option4.place(x=x4, y=y4)
        
	frame.destroy()
	global frame1
	frame1 = Frame(root, width=600, height=400)
	canvas1 = Canvas(frame1, width=600, height=400,bg="yellow")
	canvas1.place(x=0, y=0)
	
	
	canvas1.create_rectangle(380,35,580,60,fill="white")   
	canvas1.create_rectangle(380,65,580,90,fill="white")	
	canvas1.create_text(470, 47, fill="darkblue", text="CURRENT SCORE : ",font=("Times",12))
	canvas1.create_text(550, 47, fill="darkblue", text=str(score),font=("Times",12))
	canvas1.create_text(470, 77, fill="red", text="HIGH  SCORE        : ",font=("Times",12))
	canvas1.create_text(550, 77, fill="red", text=str(hscore),font=("Times",12))
	
	n = random.randrange(0,len(list2), 1)
    
	def restart(frame2):
		global score
		score=0
		frame2.destroy()
		showimage()
		
	if len(list1) == len(list2):
		list1.clear()
		frame1.destroy()
		frame2 = Frame(root)
		canvas2 = Canvas(frame2, height=400, width=600,bg="lightblue")

		canvas2.create_text(300,100, fill="green", text="You Won!!!!", font=("Times", 30))
		canvas2.create_text(300,180, fill="darkblue", text="*Congratulations*", font=("Times", 30))
		
		restart_but = Button(frame2, text="Play again", width=15, height=2, command=lambda: restart(frame2))
		restart_but.place(x=170, y=280)
		exit_but=Button(frame2, text="Quit", width=15, height=2, command=exit)
		exit_but.place(x=320, y=280)
		canvas2.pack()
		frame2.pack()

	elif n in list1:
		showimage()

	else:
		
		# canvas1.create_rectangle(12,12,253,253)
		# canvas1.create_rectangle(10,10,255,255,fill="blue")
		# canvas1.create_rectangle(15,15,250,250,fill="red")
		img = ImageTk.PhotoImage(Image.open("Images/"+list[n][0]))
		canvas1.create_image(50, 21, anchor=NW, image=img)
		canvas1.image = img
		canvas1.place(x=0, y=0)
		
		list1.append(n)
		showbuttons(n)

	frame1.pack()
	# print("list1 : ",list1)
	
def soundflag():
	global soundstatus 
	if soundstatus == 0:
		# print("sound on\n")
		soundstatus=1
	elif soundstatus == 1:
		# print("sound off\n")
		soundstatus=0
		



def exit():

	quit()
def music():
	
	global musicflag
	if musicflag == 0:
		musicflag=1
		pygame.mixer.music.load('music.mp3')
		pygame.mixer.music.play(-1)
		#print("music on")
	else:   
		musicflag=0
		pygame.mixer.music.stop()
		#print("music off")	

def sound(answer):
	if soundstatus == 1:
		if answer == 1 :
			winsound.Beep(4000,100)
		
		elif answer == 0:
			winsound.Beep(400,300)


def showinst():
		def closeinsrtuct():
			instwindow.destroy()
			
		instwindow=Tk()
		instwindow.title("Instructions")
		global fr2
		fr2=Frame(instwindow, width=500, height=300)
		ca2 = Canvas(fr2, height=300, width=500,bg="lightblue")
		#ca2.create_rectangle(380,32,500,47,fill="white")
		instlabel=Label(ca2,text=instructions,font="Times 14")
		close_but=Button(fr2, text="Close",width=10, height=1, command=closeinsrtuct)
		
		instlabel.place(x=25,y=50)
		close_but.place(x=200,y=260)
		ca2.pack()
		fr2.pack()
		instwindow.resizable(0,0)
		instwindow.mainloop()
		
canvas4 = Canvas(frame, height=400, width=700)
back_img=ImageTk.PhotoImage(Image.open("Images\\background.png"))
canvas4.create_image(0, 0, anchor=NW, image=back_img)
canvas4.image = back_img
canvas4.pack()

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

but = Button(frame, text="Start",width=15,font=('Arial',12,'bold'), command=showimage,bg='red',fg='white')
but1 = Button(frame, text="Quit",width=15,font=('Arial',12,'bold'),command=exit,bg='red',fg='white')
cbut_music = Checkbutton(frame, text="Music",variable=var3,onvalue=0,offvalue=1,command=music,bg='red')
instbut=Button(frame,text="Help",width=15,font=('Arial',12,'bold'),command=showinst,bg='red',fg='white')

instbut.place(x=210,y=200)
but.place(x=80,y=150)
but1.place(x=330,y=150)
cbut_music.place(x=530,y=10)

frame.pack()
root.resizable(0,0)
root.geometry("600x400+380+80")
root.mainloop()
