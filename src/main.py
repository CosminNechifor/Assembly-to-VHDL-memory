from tkinter import *
from src.tools import parser
from src.bll import logic


global text
global riscInstructions

PATH_TO_JSON = './tools/instructions.json'
PATH_TO_MEMORY_S = './bll/memoryStart.txt'
PATH_TO_MEMORY_E = './bll/memoryEnd.txt'

def writeMemory():
    # assemblyCode = text.get("1.0",END).split('\n')
    # assemblyCode.pop()
    assemblyCode = ['XOR r1, r2, r3', 'ADDI r3, r2, 100', 'JMP r4']
    size = len(assemblyCode)
    binary = logic.convertAssemblyToBinary(assemblyCode, riscInstructions)
    print(binary)
    logic.binaryToVHDLMemory(binary, pathS=PATH_TO_MEMORY_S, pathE=PATH_TO_MEMORY_E)




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
