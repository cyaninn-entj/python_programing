from tkinter import *
import os
import os.path
 
## 함수 선언 부분 ##
def clickListBox(evt) :
    global currentDir, searchDirList
    if (dirListBox.curselection() == ()) :
        return
    dirName = str(dirListBox.get(dirListBox.curselection())) # 클릭한 폴더명
    if dirName == '상위폴더' :
        if len(searchDirList) == 1 : # 상위 폴더를 클릭했는데 현재 C:\\면 무시
            return
        searchDirList.pop() # 상위 폴더 이동이라 마지막 검색 폴더(현재 폴더) pop
    else :
        searchDirList.append(currentDir + dirName + '\\') #검색 리스트에 클릭한 폴더 추가
         
    fillListBox()
         
def fillListBox() :
    global currentDir, searchDirList, dirLabel, dirListBox, fileListBox
    dirListBox.delete(0 ,END)   # 폴더 리스트 box를 비움
    fileListBox.delete(0, END)  # 파일 리스트 box를 비움
 
    dirListBox.insert(END, "상위폴더")
    currentDir = searchDirList[len(searchDirList) - 1]
    dirLabel.configure(text = currentDir)
    folderList = os.listdir(currentDir)
    

    for i,item in enumerate(folderList) :
        if os.path.isdir(currentDir + item) :
            dirListBox.insert(END, item)
        elif os.path.isfile(currentDir + item) :
            #fileListBox.insert(END, item)
            fileSize=os.path.getsize(currentDir+item)
            fileName, fileExt = os.path.splitext(item)

            if fileSize < 1000000 : #1mb미만
                fileSize=fileSize//1000
                fileListBox.insert(END,item+" "+"["+str(fileSize)+" KB]")
            elif 1000000 <= fileSize :
                fileSize=fileSize//1000000
                fileListBox.insert(END,item+" "+"["+str(fileSize)+" MB]")
            
            fileExt=fileExt.lower()
            if fileExt=='.exe' or fileExt=='.msi' : 
                fileListBox.itemconfig(i,foreground='green')
            elif fileExt=='.jpg' or fileExt=='.bmp' or fileExt=='.png' or fileExt=='.gif' : 
                fileListBox.itemconfig(i,foreground='red')
            elif fileExt=='.py' :
                fileListBox.itemconfig(i,foreground='blue')

            

 ## 전역 변수 선언 부분 ##
window = None
searchDirList = ['C:\\']    # 중요변수! 검색한 폴더 목록의 스택
currentDir = 'C:\\'
dirLabel, dirListBox, fileListBox = None, None, None

## 메인 코드 부분 ##
window = Tk()
window.title("폴더 및 파일 목록 보기")
window.geometry("300x500")
 
dirLabel = Label(window, text = currentDir)
dirLabel.pack()
 
dirListBox = Listbox(window)
dirListBox.pack(side = LEFT, fill = BOTH, expand = 1)
dirListBox.bind('<<ListboxSelect>>', clickListBox)
 
fileListBox = Listbox(window)
fileListBox.pack(side = RIGHT, fill = BOTH, expand = 1)
 
fillListBox()   # 초기에는 C:\\의 모든 폴더 목록 만들기
 
window.mainloop()

