from tkinter import *
from time import *

fnameList=["black.gif", "blue.gif", "brown.gif", "yellow.gif",
"gray.gif", "green.gif", "orange.gif", "pink.gif", "purple.gif", "red.gif"]
photoList=[None]*9
num=0

def clickNext() :
    global num
    num+=1
    if num>8 :
        num=0
    photo=PhotoImage(file="pp/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image_names= photo
    btnFn['text']=fnameList[num]

def clickPrev() :
    global num
    num=num-1
    if num<0 :
        num=8
    photo=PhotoImage(file="pp/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image_names = photo
    btnFn['text']=fnameList[num]

window=Tk()
window.geometry("600x350")
window.title("사진 앨범 보기")
btnPrev=Button(window, text="다음>>", command=clickPrev)
btnNext=Button(window, text="<<이전", command=clickNext)
btnFn=Button(window, text="사진명")

photo=PhotoImage(file="pp/"+fnameList[0])
pLabel= Label(window, image=photo)

btnNext.place(x=250, y=10)
btnFn.place(x=325, y=10)
btnPrev.place(x=400, y=10)
pLabel.place(x=15, y=50)

window.mainloop()