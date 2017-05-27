import serial

ser.serial = serial.Serial('/dev/ttyACM0', 9600)
message = ser.readline()
sensorDict = {}
actuatorDict = {}
instructionArray = message.split(",")
codeArray = [0] * len(instructionArray)
size  = 0
ii = 0
for keys in instructionArray :
    sensor_key = keys.split(":")
    if(sensorKey[0].index(1) == "S") :
        sensorDict[sensor_key[0]] = sensor_key[1]
    elif(sensorKey[1].index(1) == "A")
        actuatorDict[sensor_key[0]] = sensor_key[1]
    codeArray[size] = sensor_key[0]
    size += 1
while ii < size :
    print("Code: ", codeArray[ii], " Value: ", instructionDict[codeArray[ii]])
    ii += 1

maxDict = {}
minDict = {}
sensor_actuatorDict = {}
def readTextFile(fileName) :
    file = open(fileName)
    for sensor in file :
        values = sensor.split(",")
        minDict[values[0]] = float(values[1])
        maxDict[values[0]] = float(values[2])
        sensor_actuatorDict[values[0]] = values[3]

readTextFile("recipe.txt")
for sensor in codeArray :
    if(float(sensorDict[sensor]) > maxDict[sensor]) :
        actuatorDict[sensor_actuatorDict[sensor]] = "0"; # Turn off
    elif(float(instructionDict[sensor]) < minDict[sensor]) :
        actuatorDict[sensor_actuatorDict[sensor]] = "1"; # Turn on

returnMessage = "GTYP\":\"Stream\","
for code in codeArray :
    if(code.index(1) == "S") :
        returnMessage += code
        returnMessage += ":"
        returnMessage += sensorDict[code]
        returnMessage += ","
    elif(code.index(1) == "A") :
        returnMessage += code
        returnMessage += ":"
        returnMessage += actuatorDict[code]
        returnMessage += ","
returnMessage += "\"GEND\":0"
ser.write(returnMessage)

