import json
from src.model.Instruction import Instruction



def getInstructions():
    data = json.loads(open("instructions.json").read())
    instructionList = []
    for typeR in data['TypeR']:
        instructionList.append(Instruction('R', typeR['name'], typeR['codification']))
    for typeI in data['TypeI']:
        instructionList.append(Instruction('I', typeI['name'], typeI['codification']))
    for typeJ in data['TypeJ']:
        instructionList.append(Instruction('J', typeI['name'], typeI['codification']))
    return instructionList
