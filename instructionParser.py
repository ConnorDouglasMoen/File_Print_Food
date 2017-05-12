import serial

ser = serial.Serial('/dev/ttyACM0', 9600) #opens serial communications
firstCheck = true
code = ""
char = ""
value = ""	
odd  = 0
counter = 1
# Step 1: read line of instructions
read_serial = ser.readline() #reads line from arduino
instructionDict = {}
# Step 2: Check which sensor the instruction is coming from
if read_serial[2:17] == "GTYP\":\"Stream\"" :
	if(firstCheck == true):
		for ii in (16:length(read_serial)):
			if read_serial[ii] == "\"":
				odd++
				if odd%2 != 0 :
					char = read_serial[ii+counter]
					while char != "\"":
						tempCode = tempCode + char
						counter++
						char = read_serial[ii+counter]
					counter = 1
					code = tempCode
					tempCode = ""
				else :
					char = read_serial[ii+counter]
					while char != ",":
						tempValue = tempValue + char
						counter++
						char = read_serial[ii+counter]
					value = tempValue
					tempValue = ""
					counter = 1
# Step 3: Store value that came with said instruction code
		instructionDict[code] = float(value)
# Step 4: Use the value to determine what to do with the actuator
		
# Step 5: Send Actuator code back through arduino








# Example Stream Message:
# “{"GTYP":"Stream","SWPH 1":6.9,"SWTM 1":25.4,"SWEC 1":2.6,"SLIN 1":33,"SLPA
# 1":0.73,"SATM 1":24.7,"SAHU 1":31.3,"SACO 1":400,"SATM 2":25.2,"SAHU 2":39.0,"SGSO
# 1":0,"SGWO 1":1,"AAHE 1":0,"AAHU 1":0,"AAVE 1":1,"AACR 1":1,"ALPN 1":0,"ALPN
# 2":0,"ALMI 1":1,"GEND":0}”

# Interpret as:
# "GTYP":"Stream" - This message type is a stream message.
# "SWPH 1":6.9 - The 1st Sensor of Water PH is reporting a value of 6.9
# "SWTM 1":25.4 - The 1st Sensor of Water Temperature is reporting a value of 25.4 degrees C
# etc, etc, etc.

# How to determine beginning/end
#   - The curly brackets encompass the entirety of the pertinent message --> Begin analyzing message at first curly bracket,
#     end at the last curly bracket.

# Reading individual messages
#   - Each snipet is divided into two portions: One is the Sensor/Actuator tag, which is surrounded by double quotes;
#     The other is the numerical data, which immediately follows a colon (no spaces before or after the colon); a comma marks the end of
#     each snipet.
#   - To parse the Sensor/Actuator tag we can read all chars between the two double quotes as one string --> We can store this string in
#     a hash table (to make for speedy-quick lookup times!) and put the (float) numerical data as its value.

# Comparing Sensor data to bounds
#   - Look up the current state of each sensor (by hashing the tag and finding its value), then simply compare this to the bounds
#   - If greater, tell actuator to turn off, if less tell actuator to turn on (or visa versa, if appropriate).

# Edge Cases
#   - This algorithm will be fairly simple, apart from the beginning and end snipets.
#   - These snipets disobey the overall trend because A) Both don't correspond to sensors/actuators and B) The very first snipet doesn't
#     have a numerical value after the colon, but another string.
#   - As of now, it appears that we do not need to interpret these messages within our parse function, but we do need to identify how to
#     make them not break our code. Any ideas?
