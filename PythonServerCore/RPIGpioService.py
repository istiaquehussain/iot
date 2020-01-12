import RPi.GPIO as GPIO
def setup_GPI(inputs):
    GPIO.setmode(GPIO.BCM)
    for pin in inputs:
        if(pin!="D-1"):
            print("Set up input...",pin)
            GPIO.setup(int(pin), GPIO.IN)
            print("done")
            
def setup_GPO(outputs):
    GPIO.setmode(GPIO.BCM)
    for pin in outputs:
        if(pin!="D-1"):
            print("Set up output ...",pin)
            GPIO.setup(int(pin), GPIO.OUT)
            print("done")

def reset(inputs,outputs):
    GPIO.cleanup()  
    
def resetInputs(inputs):
    GPIO.setmode(GPIO.BCM)
    for pin in inputs:
        if(pin!="D-1"):
            if GPIO.input(int(pin)):
                print("Switing off ...",pin)
                GPIO.input(int(pin), GPIO.LOW)
                print("done")

def resetOutputs(outputs):
    GPIO.setmode(GPIO.BCM)
    for pin in outputs:
        if(pin!="D-1"):
            if GPIO.input(int(pin)):
                print("Switing off ...",pin)
                GPIO.output(int(pin), GPIO.LOW)
                print("done")                
    
def swithOnInput(pin):
    if not(GPIO.input(int(pin))):
        print("Switing on ...",pin)
        GPIO.input(pin, GPIO.HIGH)
        print("done")

def swithOffInput(pin):
    if GPIO.input(int(pin)):
        print("Switing off ...",pin)
        GPIO.input(pin, GPIO.LOW)
        print("done")    

    
def swithOnOutput(pin):
    if not(GPIO.input(int(pin))):
        print("Switing on ...",pin)
        GPIO.input(int(pin), GPIO.HIGH)
        print("done")

def swithOffOutput(pin):
    if GPIO.input(int(pin)):
        print("Switing off ...",pin)
        GPIO.output(int(pin), GPIO.LOW)
        
def toggleOutput(pin):
    if GPIO.input(int(pin)):
        print("Switing off ...",pin)
        GPIO.output(int(pin), GPIO.LOW)
        print("done")
    else:
        print("Switing on ...",pin)
        GPIO.output(int(pin), GPIO.HIGH)
        print("done")

def toggleInput(pin):
    if GPIO.inputint((pin)):
        print("Switing off ...",pin)
        GPIO.input(int(pin), GPIO.LOW)
        print("done")
    else:
        print("Switing on ...",pin)
        GPIO.input(int(pin), GPIO.HIGH)
        print("done")
        