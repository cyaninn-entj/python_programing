from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox

def loadImage(fname) :
    global inImage, XSIZE, YSIZE
    fp=open(fname, 'rb')
    for i in range(0,XSIZE) :
        tmpList=[]
        for k in range(0, YSIZE) :
            data=int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)
    fp.close()

def displayImage(image) :
    global XSIZE, YSIZE
    rgbString=""
    for i in range(0,XSIZE) :
        tmpString=""
        for k in range(0, YSIZE) :
            data=image[i][k]
            tmpString+="%02x%02x%02x" %(data, data, data)
        rgbString+="{"+tmpString+"}"
    paper.put(rgbString)

def success() :
    global filename
    messagebox.showinfo("파일로드결과",filename+"가 정상 처리 됨")
def fail() :
    global filename
    messagebox.showerror("파일로드결과",filename+"처리 불가")
def shudown() :
    messagebox.showinfo("종료","수고하셧습니다.")

window=None
canvas=None
XSIZE,YSIZE=256,256
inImage=[]

window=Tk()
window.title("흑백사진보기")
canvas=Canvas(window, height=XSIZE, width=YSIZE)
paper = PhotoImage(width=XSIZE, height=YSIZE)
canvas.create_image((XSIZE/2, YSIZE/2), image=paper, state="normal")
filename=askopenfilename(parent = window,filetypes=(("raw 파일","*.raw"),("모든 파일","*.*")))

try :
    loadImage(filename)
    displayImage(inImage)
    success()
except :
    fail()

shudown()
canvas.pack()
window.mainloop()


