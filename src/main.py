from tkinter import *
from src.tools import parser
from src.bll import logic

global text
global riscInstructions

PATH_TO_JSON = './tools/instructions.json'

def writeMemory():
    # assemblyCode = text.get("1.0",END)
    assemblyCode = ['XOR r1, r2, r3', 'ADDI r3, r2, 100', 'JMP r4']
    binary = logic.convertAssemblyToBinary(assemblyCode, riscInstructions)



def createWindow():
   global text
   global riscInstructions

   quit = Button(text="QUIT", fg="red",
                  command=root.destroy)
   quit.pack(side="bottom")
   assemble = Button(text="Create memory", fg="blue", command=writeMemory)
   assemble.pack(side="bottom")

   scroolBar = Scrollbar(root)

   text = Text(root, height=50, width=50)
   scroolBar.pack(side=RIGHT, fill=Y)
   text.pack(side=LEFT, fill=Y)
   scroolBar.config(command=text.yview)
   text.config(yscrollcommand=scroolBar.set)
   riscInstructions = parser.getInstructions(PATH_TO_JSON)

if __name__ == '__main__':
   root = Tk()
   createWindow()
   root.mainloop()
