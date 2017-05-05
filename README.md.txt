Python Script : 

This function will read in a string of serial data from the Raspberry Pi containing information about the current state of the actuators and sensor data.

It will then parse this string and compare the data from each sensor with predetermined constraints; if the data is out of bounds of the constraints, the function will relay a command to the Pi to update the state of the appropriate actuator (on/off) to keep the conditions of the system within the constraints.