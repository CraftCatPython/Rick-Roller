#Importing Modules
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import time
import tkvideo
import pygame
import tkinter.font as font
from tkinter import ttk
import time

#Window
pygame.mixer.init()
root = Tk()
root.title("Pokemon Orange")
root.geometry("480x285")
myFont = font.Font(size=30)

#Images
Begin = ImageTk.PhotoImage(Image.open("Img/OpenScreen.png"))
Charmander = ImageTk.PhotoImage(Image.open("Img/Char.png"))
Cufant = ImageTk.PhotoImage(Image.open("Img/Cufant.png"))
Growlithe = ImageTk.PhotoImage(Image.open("Img/Growlithe.png"))
Rival = ImageTk.PhotoImage(Image.open("Img/HJjehrjuhn.png"))
WhiteSpace = ImageTk.PhotoImage(Image.open("Img/White_Space.png"))

#Variables
OakTalkP1 = Label(root, text="Welcome To The World Of Pokemon")
OakTalkP2 = Label(root, text="My Name Is Professor. Blah")
OakTalkP3 = Label(root, text="Blah Blah Blah Blah Blah Blah Blah Blah")
OakTalkP4 = Label(root, text="You rememblah your rival, HJjehrjuhn right?")
OakTalkP5 = Label(root, text="Choose A Pokemon Blah")
C = Label(root, text="Charmander")
E = Label(root, text="Cufant")
G = Label(root, text="Growlithe")
BattleStart = Label(root, text="And Dont Even Think About Leaving Without A Fight")
RPCH = Label(root, text="If Youre Gonna Get Charmander Then Im Gonna Get Cufant")
RPC = Label(root, text="If Youre Gonna Get Cufant Then Im Gonna Get Growlithe")
RPG = Label(root, text="If Youre Gonna Get Growlithe Then Im Gonna Get Charmander")
RivalCH = Label(root, image=Cufant)
RivalC = Label(root, image=Growlithe)
RivalG = Label(root, image=Charmander)
Space = Label(root, image=WhiteSpace)
HealthBarNPC = ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode='determinate')
HealthBarS = ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode='determinate')
HealthBarSA = Label(root, text="10/10")
Move = Label(root, text="HJjehrjuhn Used Rick Roll")

#Peoplemon
Antagonist = Label(root, image=Rival)

def Clear():
  C.grid_forget()
  E.grid_forget()
  G.grid_forget()
  STRTR1.grid_forget()
  STRTR2.grid_forget()
  STRTR3.grid_forget()

#Fonts/Size
myFont = font.Font(size=15, family='Algerian')
Move['font'] = myFont
HealthBarSA['font'] = myFont
OakTalkP1['font'] = myFont
OakTalkP2['font'] = myFont
OakTalkP3['font'] = myFont 
OakTalkP4['font'] = myFont
OakTalkP5['font'] = myFont
C['font'] = myFont
E['font'] = myFont
G['font'] = myFont

#----POKEMON-MOVES-FUNCTIONS----#
def HealthBar():
  for x in range(10):
    HealthBarS['value'] += 20
    HealthBarNPC['value'] += 20
    root.update_idletasks()

def RickRoll():
  #Clear
  Space.grid()
  RivalCH.grid_forget()
  RivalG.grid_forget()
  HealthBarS.grid_forget()
  HealthBarNPC.grid_forget()
  HealthBarSA.grid_forget()
  RivalCH.grid_forget()
  RivalG.grid_forget()
  RivalC.grid_forget()
  RPG.grid_forget()
  Move.grid_forget()

  pygame.mixer.music.load("Video/Song.mp3")
  pygame.mixer.music.play(loops=5)
  my_label = Label(root)
  my_label.grid()
  player = tkvideo.tkvideo("C:\\Users\\asadp\\OneDrive\\Desktop\\RickRoller\\Video\\RickRollTime.mp4", my_label, loop = 1, size = (1280,720))
  player.play()
  root.geometry("1300x900")


def BattleCH():
  RPCH.grid_forget()
  Antagonist.grid_forget()
  BattleStart.grid_forget()
  RivalC.grid(row=1, column=16)
  RivalG.grid(row=5,column=1)
  root.geometry("800x700")
  HealthBarS.grid(row=8, column=1)
  HealthBarNPC.grid(row=5, column=16)
  HealthBarSA.grid(row=6,column=1)
  HealthBar()
  Move.grid(row=10, column=2)
  root.after(2000, RickRoll)


def BattleC():
  RPC.grid_forget()
  Antagonist.grid_forget()
  BattleStart.grid_forget()
  RivalC.grid(row=1, column=16)
  RivalG.grid(row=5,column=1)
  root.geometry("800x700")
  HealthBarS.grid(row=8, column=1)
  HealthBarNPC.grid(row=5, column=16)
  HealthBarSA.grid(row=6,column=1)
  HealthBar()
  Move.grid(row=10, column=2)
  root.after(2000, RickRoll)
  
def BattleG():
  RPG.grid_forget()
  Antagonist.grid_forget()
  BattleStart.grid_forget()
  RivalC.grid(row=1, column=16)
  RivalG.grid(row=5,column=1)
  root.geometry("800x700")
  HealthBarS.grid(row=8, column=1)
  HealthBarNPC.grid(row=5, column=16)
  HealthBarSA.grid(row=6,column=1)
  HealthBar()
  Move.grid(row=10,column=2)
  root.after(2000, RickRoll)

def Char():
  Clear()
  RPCH['font'] = myFont
  BattleStart['font'] = myFont
  Antagonist.grid(row=0, column=1)
  RPCH.grid(row=1, column=1)
  BattleStart.grid(row=2, column=1)
  root.geometry("630x350")
  root.after(3000, BattleCH)
  
STRTR1 = Button(root, image=Charmander, command=Char)

def Cuf():
  Clear()
  RPC['font'] = myFont
  BattleStart['font'] = myFont
  Antagonist.grid(row=0, column=1)
  RPC.grid(row=1, column=1)
  BattleStart.grid(row=2, column=1)
  root.geometry("630x350")
  root.after(3000, BattleC)

STRTR2 = Button(root, image=Cufant, command=Cuf)

def Growl():
  Clear()
  RPG['font'] = myFont
  BattleStart['font'] = myFont
  Antagonist.grid(row=0, column=1)
  RPG.grid(row=1, column=1)
  BattleStart.grid(row=2, column=1)
  root.geometry("650x350")
  root.after(3000, BattleG)
  

STRTR3 = Button(root, image=Growlithe, command=Growl) 

#----POKEMON-MOVES-FUNCTIONS----#

#—---FUNCTIONS----#

def Starters():

  #Unpacking The Screen
  OakTalkP1.grid_forget()
  OakTalkP2.grid_forget()
  OakTalkP3.grid_forget()
  OakTalkP4.grid_forget()
  start.grid_forget()
  Antagonist.grid_forget()
  OakTalkP5.grid_forget()

  #Resizing it
  root.geometry("700x300")

  #Starter
  STRTR1.grid(row=1,column=1)
  STRTR2.grid(row=1,column=2)
  STRTR3.grid(row=1,column=3)
  
  #Sorting Labels
  C.grid(row=2, column=1) 
  E.grid(row=2, column=2)
  G.grid(row=2, column=3)

def One():
  OakTalkP1.grid_forget()
  OakTalkP2.grid()
  root.after(2000, Two)

def Two():
  OakTalkP2.grid_forget()
  OakTalkP3.grid()
  root.after(2000, Three)

def delayed():
  print("this is getting delayed for ze thing")

def Three():
  OakTalkP3.grid_forget()
  OakTalkP4.grid()
  Antagonist.grid(row=0, column=1)
  root.geometry("700x305")
  root.after(3000, Four)

def Four():
  OakTalkP4.grid_forget()
  OakTalkP5.grid()
  Antagonist.grid_forget()
  root.geometry("480x285")
  root.after(3000, Starters)
  
#—---FUNCTIONS----#

#Beginning
start = Label(root, image=Begin)
start.grid() 
OakTalkP1.grid()
root.after(3000, One)

root.mainloop()