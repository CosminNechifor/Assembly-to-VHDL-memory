from tkinter import *
from src.model.Instruction import Instruction
from src.tools import parser

global text

def createMemory():
    return text.get("1.0",END)



def createWindow():
   global text
   quit = Button(text="QUIT", fg="red",
                  command=root.destroy)
   quit.pack(side="bottom")
   assemble = Button(text="Create memory", fg="blue", command=createMemory)
   assemble.pack(side="bottom")

   scroolBar = Scrollbar(root)

   text = Text(root, height=50, width=50)
   scroolBar.pack(side=RIGHT, fill=Y)
   text.pack(side=LEFT, fill=Y)
   scroolBar.config(command=text.yview)
   text.config(yscrollcommand=scroolBar.set)

if __name__ == '__main__':
   root = Tk()
   createWindow()
   root.mainloop()
