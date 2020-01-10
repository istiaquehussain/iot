import json
from flask import Flask as webServer
from flask import render_template
from flask import redirect, url_for, request
import GPIOService as gpioservice

def readServerConfig():
    conf = json.load(open("config/serverconfig.json"))
    return conf

serverCong=readServerConfig()
inputs=gpioservice.getInputs()
outputs=gpioservice.getOutputs()
app = webServer(__name__)

@app.route(serverCong["rootcontext"])
def renderIndex():
    return render_template("/index.html")

@app.route(serverCong["rootcontext"]+"/singlebuttonlayout")
def renderSingleButtonLoayout():
    return render_template("/singlebuttonlayout.html",buttons=inputs)

@app.route(serverCong["rootcontext"]+"/multibuttonlayout")
def renderMutiButtonLoayout():
    return render_template("/multibuttonlayout.html",buttons=inputs)

@app.route(serverCong["rootcontext"]+"/singlebuttonaction",methods = ['POST', 'GET'])
def renderSingleButtonAction():
    actionLeds=["D-1"]
    if request.method == 'GET':
        leds = request.args.get("ID")
        actionLeds.append(leds)
        #actionLeds=actionLeds.append(leds)
        #actionLeds=actionLeds+[leds]
        #print("Following LD will be on")
        #print(actionLeds)
        gpioservice.GPIO_OUT_Action(outputs,actionLeds,"ON")
        return render_template("/singlebuttonlayout.html",buttons=outputs)
    else:
        leds = request.form["ID"]
        actionLeds.append(leds)
        gpioservice.GPIO_OUT_Action(outputs,actionLeds,"ON")
        print("Following LD will be on")
        print(leds)
        return render_template("/singlebuttonlayout.html",buttons=outputs)


@app.route(serverCong["rootcontext"]+"/welcome")
def welcome():
    return "Welcome to IOT Service "    

if __name__ == '__main__':
    app.run(port=serverCong["port"],debug=True)

