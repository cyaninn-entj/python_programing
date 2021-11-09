from tkinter import *
import random

btnList=[None]*9
fnameList = ["black.gif", "blue.gif", "brown.gif", "yellow.gif",
"gray.gif", "green.gif", "orange.gif", "pink.gif", "purple.gif", "red.gif"]
photoList=[None]*9
i,k=0,0
xPos, yPos=0,0
num=0


window = Tk()
window.geometry("210x210")
random.shuffle(fnameList)

for i in range(0,9) :
    photoList[i] = PhotoImage(file="pp/"+fnameList[i])
    btnList[i]=Button(window, image=photoList[i])


for i in range(0,3) :
    for k in range(0,3) :
        btnList[num].place(x=xPos, y=yPos)
        num+=1
        xPos+=70
    xPos=0
    yPos+=70

window.mainloop()