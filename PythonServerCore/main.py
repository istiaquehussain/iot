import json
from flask import Flask as webServer
from flask import render_template
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


@app.route(serverCong["rootcontext"]+"/welcome")
def welcome():
    return "Welcome to IOT Service "    

if __name__ == '__main__':
    app.run(port=serverCong["port"],debug=True)

