#!/usr/bin/python3

import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
while True :
    message = str(ser.readline())
    if(len(message) > 6) :
        if(message[6] == "Y"):
           # message = input("input instruction: ")
            sensorDict = {}
            actuatorDict = {}
            instructionArray = message.split(",")
            codeArray = [0] * len(instructionArray)
            size  = 0
            sensorSize = 0
            actuatorSize = 0
            ii = 1
            for keys in instructionArray :
                sensor_key = keys.split(":")
                if(sensor_key[0][1] == "S") :
                    sensorDict[sensor_key[0]] = sensor_key[1]
                    sensorSize += 1
                elif(sensor_key[0][1]== "A") :
                    actuatorDict[sensor_key[0]] = sensor_key[1]
                    actuatorSize += 1
                codeArray[size] = sensor_key[0]
                size += 1
            while ii <= sensorSize :
                print("Code: ", codeArray[ii], " Value: ", sensorDict[codeArray[ii]])
                ii += 1
            while ii < actuatorSize + sensorSize:
                print("Code: ", codeArray[ii], " Value: ", actuatorDict[codeArray[ii]])
                ii += 1

            maxDict = {}
            minDict = {}
            sensor_actuatorDict = {}
            def readTextFile(fileName) :
                file = open(fileName)
                for sensor in file :
                    sensor = sensor.strip()
                    values = sensor.split(",")
                    minDict[values[0]] = float(values[1])
                    maxDict[values[0]] = float(values[2])
                    sensor_actuatorDict[values[0]] = values[3]

            readTextFile("testRecipe.txt")
            for sensor in codeArray :
                if(sensor[1] == "S") :
                    if(float(sensorDict[sensor]) > maxDict[sensor]) :
                        actuatorDict[sensor_actuatorDict[sensor]] = "0"; # Turn off
                    elif(float(sensorDict[sensor]) < minDict[sensor]) :
                        actuatorDict[sensor_actuatorDict[sensor]] = "1"; # Turn on



            returnMessage = ""
            for code in codeArray :
                if(code[1] == "A") :
                    returnMessage += code[1:7]
                    returnMessage += " "
                    returnMessage += actuatorDict[code]
                    print(returnMessage)
                    x = bytearray(returnMessage+"\n","UTF-8")
                    ser.write(x)
                    returnMessage = ""


