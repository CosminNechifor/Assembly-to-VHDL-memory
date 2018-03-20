from math import sqrt

# converts text in window to binary code
def convertAssemblyToBinary(assemblyCode, riscInstructions):
    binaryList = []
    for i in assemblyCode:
        # 0 -> Instruction type
        # 1-> Instruction coodification
        instructionArray = i.split(' ')
        # print(instructionArray)
        instruction = riscInstructions[instructionArray[0]]
        # print(instruction[0])
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

        if instruction[0] == 'I':
            registerCode = createInstructionTypeI(instructionArray[1]
                                                  .replace(',', ''),
                                                  instructionArray[2]
                                                  .replace(',', ''),
                                                  instructionArray[3]
                                                  .replace(',', ''))
            binary = instruction[1] + str(registerCode)
            binaryList.append(binary)

        if instruction[0] == 'J':
            code = createInstructionTypeJ(instructionArray[1])
            binary = instruction[1] + str(code)
            binaryList.append(binary)

    return binaryList



def createInstructionTypeR(arg0, arg1, arg2):
    return getRegBinaryAddress(arg0) + getRegBinaryAddress(arg1) + getRegBinaryAddress(arg2)

# creates Instructions of type I
def createInstructionTypeI(arg0, arg1, arg2):
    bin16 = lambda x: ''.join(reversed([str((x >> i) & 1) for i in range(16)]))
    return getRegBinaryAddress(arg0) + getRegBinaryAddress(arg1) + bin16(int(arg2))

def createInstructionTypeJ(arg):
    bin24 = lambda x: ''.join(reversed([str((x >> i) & 1) for i in range(24)]))
    if isRegister(arg):
        if len(arg) == 2:
            return bin24(int(arg[1]))
        else:
            return bin24(int(arg[(len(arg) - 2):len(arg)]))
    else:
        return bin24(int(arg))

# calls convert assembly and creates the memory in vhdl
def binaryToVHDLMemory(binaryList, pathS, pathE):
    text = open(pathS).read()
    memoryContent = ''

    memory_len = len(binaryList)
    address_size = round(sqrt(memory_len))
    for i in range(0, memory_len):
        if (i == memory_len-1):
            memoryContent = memoryContent + str(i) + '=>' \
                            + '\"' + binaryList[i] + '\"'
        else:
            memoryContent = memoryContent + str(i) + '=>' \
                            + '\"' + binaryList[i] + '\",\n'

    binify = lambda x: ''.join(reversed([str((x >> i) & 1) for i in range(address_size)]))

    memory_address = ''
    for i in range(0, memory_len):
        memory_address = memory_address + 'when' + '\"' \
                         + binify(i) + '\"' + "=> data <= my_rom(" + str(i) + ");\n"
    memory_address = memory_address + "when others => data <= \"00000000\";\n"

    text = text.replace("ADDRESS_SIZE", str(address_size)). \
        replace("MEMORY_LEN", str(memory_len)). \
        replace("CONTENT", memoryContent). \
        replace("CASE_ADDRESS", memory_address)

    outputFile = open(pathE, "w")
    outputFile.write(text)





def getRegBinaryAddress(regname):
    bin4 = lambda x: ''.join(reversed([str((x >> i) & 1) for i in range(4)]))
    if len(regname) == 2:
        return bin4(int(regname[1]))
    else:
        return bin4(int(regname[(len(regname ) -2):len(regname)]))

# def getBinaryOfNumber(number):
#     bin16 = lambda x: ''.join(reversed([str((x >> i) & 1) for i in range(16)]))
#     return bin16(int(number))

def isRegister(register):
    if register[0].upper() == 'R':
        return True
    else:
        return False