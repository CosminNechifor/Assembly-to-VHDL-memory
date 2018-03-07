import json


def createInstruction(instructions, type):
    pass



def getInstructions():
    data = json.loads(open("instructions.json").read())
    return data

if __name__ == '__main__':
    print(getInstructions())