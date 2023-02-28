import tkinter
from tkinter import filedialog
from tkinter import font
tk=tkinter.Tk()
tk.geometry("800x600")
tk.title("Editor")

def savefile():
    inputTxt = txt.get("1.0","end")
    filename=filedialog.asksaveasfile(mode="a+")
    filename.write(inputTxt)
    filename.close()

def openfile():
    filename=filedialog.askopenfile(mode="r")
    filetxt = filename.read()
    txt.insert(tkinter.END, filetxt)
    filename.close()

def textColChange():
        l=len(textColList)
        global tColor,i
        tColor=textColList[i%l]
        txt.config(foreground=tColor)
        txt.update()
        i+=1

def backColChange():
        l=len(backColList)
        global bgColor,j
        bgColor=backColList[j%l]
        txt.config(background=bgColor)
        txt.update()
        j+=1

def fontSelector(fnt):
      global myfont
      myfont=fnt
      txt.config(font=(myfont,myfontsize)) 

def fontsizeSelector(fnt):
      global myfontsize
      myfontsize=fnt
      txt.config(font=(myfont,myfontsize)) 

backColList=["cyan","black","red","white"]
textColList=["red","white","blue","black"]
bgColor="white"
tColor="black"
i,j=0,0
fonts=list(font.families())
default=tkinter.StringVar()
default.set("Courier")

myfont=""
myfontsize=12
fontsize=[]
for i in range(8,34,2):
    fontsize.append(i)
fontDefault=tkinter.StringVar()
fontDefault.set(12)

OpenFile=tkinter.Button(text="Open", command=openfile).grid(row=0, column=0)
Save=tkinter.Button(text="Save", command=savefile).grid(row=0, column=1)
textCol=tkinter.Button(text="Color",command=textColChange).grid(row=0,column=2)
backCol=tkinter.Button(text="Background",command=backColChange).grid(row=0,column=3)
fontsizeSel=tkinter.OptionMenu(tk,fontDefault,*fontsize,command=fontsizeSelector).grid(row=0,column=4)
fontSel=tkinter.OptionMenu(tk,default,*fonts,command=fontSelector).grid(row=0,column=5)

txt=tkinter.Text(tk,background=bgColor, foreground=tColor, font=("Courier",12))  
txt.place(y=30,relheight=1,relwidth=1)
tk.mainloop()
