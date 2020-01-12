import json
import RPIGpioService as rpiservice
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

def GPIO_OUT_Toggle(actionOuts):
    for pin in actionOuts:
        if(pin!="D-1"):
            rpiservice.toggleOutput(pin)
                
def reset():
    rpiservice.reset()  
    
def resetInputs(inputs):
     rpiservice.resetInputs(inputs)

def resetOutputs(outputs):
        rpiservice.resetOutputs(outputs)    

def setup_GPIO(inputs,outputs):
    print("Setting up GPIOS ...")
    print("INPUTS ...")
    print(inputs)
    rpiservice.setup_GPI(inputs)
    print("OUTPUTS ...")
    print(outputs)
    rpiservice.setup_GPO(outputs)
    



    




#outs=getOutputs()
#print(outs)

