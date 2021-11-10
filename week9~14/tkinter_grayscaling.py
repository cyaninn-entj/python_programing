from tkinter import *
from tkinter.filedialog import *

def func_open() :
    sl_filename = askopenfilename(initialdir="/", title="Select file", 
                filetypes=(("gif files", "*.gif"), ("all files", "*.*")))
    photo=PhotoImage(file=sl_filename)

    ph_wid=photo.width()
    ph_hei=photo.height()

    for i in range(1, ph_hei+1) :
        for j in range(1, ph_wid+1) :
            rgb=photo.get(i,j)
            r=rgb[0];g=rgb[1];b=rgb[2]
            gray=int((r*g*b)/3)
            photo.put("#%02x%02x%02x" % (gray, gray, gray), (i,j))


    pLabel.configure(image=photo)
    pLabel.image=photo
    
def func_exit() :
    window.quit()
    window.destroy()

window=Tk()
window.geometry("400x400")
window.title("영화 감상하기")

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

window.mainloop()