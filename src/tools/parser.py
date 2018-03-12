import json

def getInstructions(path):
    data = json.loads(open(path).read())
    instructionDict = dict()

    for typeR in data['TypeR']:
        instructionDict[typeR['name']] = ('R', typeR['codification'])
    for typeI in data['TypeI']:
        instructionDict[typeI['name']] = ('I', typeI['codification'])
    for typeJ in data['TypeJ']:
        instructionDict[typeJ['name']] = ('J', typeJ['codification'])
    return instructionDict

