

# creates Instructions of type R
def createInstructionTypeR(arg0, arg1, arg2):
    return getRegBinaryAddress(arg0) + getRegBinaryAddress(arg1) + getRegBinaryAddress(arg2)

# creates Instructions of type I
def createInstructionTypeI(arg0, arg1, arg2):
    bin16 = lambda x: ''.join(reversed([str((x >> i) & 1) for i in range(16)]))
    return getRegBinaryAddress(arg0) + getRegBinaryAddress(arg1) + bin16(int(arg2))

def createInstructionTypeJ():
    pass


# converts text in window to binary code
def convertAssemblyToBinary(assemblyCode, riscInstructions):
    binaryList = []
    for i in assemblyCode:
        # 0 -> Instruction type
        # 1-> Instruction coodification
        instructionArray = i.split()
        instruction = riscInstructions[instructionArray[0]]
        if instruction[0] == 'R':
            registerCode = createInstructionTypeR(instructionArray[1]
                                                  .replace(',', ''),
                                                  instructionArray[2]
                                                  .replace(',', ''),
                                                  instructionArray[3]
                                                  .replace(',', ''))
            registerCode = str(registerCode) + '000000000000'
            binary = instruction[1] + registerCode
            binaryList.append(binary)

        # if instruction[1] == 'I':
        #     registerCode = createInstructionTypeI(instructionArray[1], instructionArray[2], instructionArray[3])
        #     print(registerCode)
    return binaryList



# calls convert assembly and creates the memory in vhdl
def binaryToVHDLMemory(binaryCode):
    pass



def getRegBinaryAddress(regname):
    bin4 = lambda x: ''.join(reversed([str((x >> i) & 1) for i in range(4)]))
    if len(regname) == 2:
        return bin4(int(regname[1]))
    else:
        return bin4(int(regname[(len(regname)-2):len(regname)]))

def getBinaryOfNumber(number):
    return lambda x: ''.join()


def isRegister(register):
    if register[0]:
        return True
    else:
        return False


if __name__ == '__main__':
    print(getRegBinaryAddress('r7'))
    print(createInstructionTypeI('r1', 'r2', '100'))