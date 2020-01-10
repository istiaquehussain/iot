import json
def loadGPIOConfig():
    gpioConfig = json.load(open("config/gpioconfig.json"))
    return gpioConfig

def getInputs():
    return loadGPIOConfig()["input"]

def getOutputs():
    return loadGPIOConfig()["output"]

def GPIO_OUT_Action(allOuts,actionOuts,action):
    # print("action ->",action)
    # print("allOuts->",allOuts)
    # print("actionOuts->",actionOuts)
    if action=="ON":
        for id in allOuts:
            print("Switching OFF ",id)
        for id in actionOuts:
            print("Switching ON ",id)
    else:
        for id in allOuts:
            print("Switching ON ",id)
        for id in actionOuts:
            print("Switching OFF ",id)

def setup_GPIO(inputs,outputs):
    print("Setting up GPIOS ...")
    print("INPUTS ...")
    print(inputs)
    print("OUTPUTS ...")
    print(outputs)




    




#outs=getOutputs()
#print(outs)

