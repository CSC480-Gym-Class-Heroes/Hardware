## What to purchase

- HC-SR501 Human Sensor Module Pyroelectric Infrared
- Raspberry Pi Model B+ 512MB
- Soldering Iron
- Soldering Iron Stand
- Jumper Wires
- SD card
- Ethernet cable
- Breadboard
- Electrical/duct tape

## How to use them

The HC-SR501 is not sensitive enough so solder off 102 and 105.
 See video for reference:
 
 https://www.youtube.com/watch?v=juOtoUabyH8
 
 Solder off 102 and 105
 See below on how to set up and run the hardware


## How to calibrate sensors

Depending on how far apart the 2 sensors are from each other, this line should be calibrated to how long it takes to walk from sensor A to sensor B. Ideally, and if they are close together they are less than a second part. The line below says the sensors are around 5 seconds apart from each other. Therefore if the sensors are really close to each other, change it to less than a second.

    if abs(t1_time-t2_time).total_seconds() < 5:

To calibrate the sensors please refer to the source code below:
Referring to line 37

    if abs(t1_time-datetime.now()).total_seconds() < 1:

Depending on how fast the sensors should reset after they trigger, less than one second is ideal for responsive and accurate data. This is important because users can accidentally set off one sensor and not the other. So in reality, the 1 should not be changed.

## How to recreate this project
 Follow this diagram below for steps 1-3

- Get a breadboard and connect 2 wires from pin I9 to I29. Connect A7 TO A27
- On the right side closest to the red of the I-9 wires connect number 7 with J17.
- On the right side closest to the red of the I-9 wires connect number 24 with J19.
- Connect the bus on ground and 5V, corresponding to the J17 and J19(J wires are already connected: J17 is the white    wire and J19 is the brown wire, just put the bus on the left of the I-9 wire).
- Grab 3 different colored wires and connect it to the HC-sr501 Sensor (In this case we will have 3 wires: black,       brown, and red): Connect the red wire closest to the yellow tower of the sensor, brown in the middle, and black on   the last available slot. Connect red to the red strip on the right side of the bus. Connect the black wire to the    left of the red wire. Connect the brown wire to the right. Connect the brown wire to the left of PIN I-9.
- To connect the second sensor, repeat step 5 with different colored wires. Make sure the second "brown" wire gets      connected to the right of A7. The other two wires can go anywhere below or above from step 5.
- Open up the Pi and go to the working directory(type "cd" to access a directory and "ls" to list the current           directories")


  In this diagram, “ls” is listing the directories
  “cd” in this diagram is accessing the “files” directories
- Once the source code is reached, type sudo python NameOfSource.py
- The hardware has successfully run. Good job!
