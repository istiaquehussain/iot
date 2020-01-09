import json
def loadGPIOConfig():
    gpioConfig = json.load(open("config/gpioconfig.json"))
    return gpioConfig
def getInputs():
    return loadGPIOConfig()["input"]
def getOutputs():
    return loadGPIOConfig()["output"]

#outs=getOutputs()
#print(outs)

