import serial

ser = serial.Serial('/dev/ttyACM0', 9600) #opens serial communications

# Step 1: read line of instructions
read_serial = ser.readline() #reads line from arduino

# Step 2: Check which sensor the instruction is coming from

# Step 3: Store value that came with said instruction code
# Step 4: Use the value to determine what to do with the actuator
# Step 5: Send Actuator code back through arduino

