import serial

ser = serial.Serial('/dev/ttyACM0', 9600) #opens serial communications

# Step 1: read line of instructions
read_serial = ser.readline() #reads line from arduino
# Step 2: Check which sensor the instruction is coming from

# Step 3: Store value that came with said instruction code

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
