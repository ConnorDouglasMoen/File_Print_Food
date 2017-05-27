
message = input("input instruction line: ")
instructionDict = {}
instructionArray = message.split(",")
codeArray = []
size  = 0
index = 0
for keys in instructionArray :
    sensor_key = keys.split(":")
    instructionDict[sensor_key[0]] = sensor_key[1]
    codeArray[size] = sensor_key[0]
    size = size + 1
while ii < size :
    print("Code: ", codeArray[ii], " Value: ", instructionDict[codeArray[ii]])

    
