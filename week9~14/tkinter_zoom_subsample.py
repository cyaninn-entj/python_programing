from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *

sl_filename = ""

def func_open() :
    global sl_filename
    sl_filename = askopenfilename(initialdir="/", title="Select file", 
                filetypes=(("gif files", "*.gif"), ("all files", "*.*")))
    photo=PhotoImage(file=sl_filename)
    ph_wid=photo.width()
    ph_hei=photo.height()
    """for i in range(1, ph_hei+1) :
        for j in range(1, ph_wid+1) :
            rgb=photo.get(i,j)
            r=rgb[0];g=rgb[1];b=rgb[2]
            gray=int((r*g*b)/3)
            photo.put("#%02x%02x%02x" % (gray, gray, gray), (i,j))"""
    pLabel.configure(image=photo)
    pLabel.image=photo
    
def func_exit() :
    window.quit()
    window.destroy()

def func_zoom() : 
    value = askinteger("확대배수", "2배~8배 입력: ", minvalue = 2, maxvalue = 8)
    photo = PhotoImage(file = sl_filename)
    photo = photo.zoom(value,value)
    pLabel.configure(image = photo)
    pLabel.image = photo
 
def func_zoomout() :  
    value = askinteger("축소배수", "2배~8배 입력: ", minvalue = 2, maxvalue = 8)
    photo = PhotoImage(file = sl_filename)
    photo = photo.subsample(value,value)
    pLabel.image = photo

window=Tk()
window.geometry("400x400")
window.title("명화 감상하기")

photo=PhotoImage()
pLabel=Label(window, image=photo)
pLabel.pack(expand=1,anchor=CENTER)

mainMenu=Menu(window)
window.config(menu=mainMenu)
fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램종료", command=func_exit)

imageMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "확대or축소", menu = imageMenu)
imageMenu.add_command(label = "확대하기", command = func_zoom)
imageMenu.add_separator()
imageMenu.add_command(label = "축소하기", command = func_zoomout)

window.mainloop()