## Hardware HowTo: Becoming a developer

## Overview
All of the programs written to run on the Raspberry Pi are written in python. This was the case because we needed to be able to access the General Purpose IO (GPIO) pins on the Pi and python provides an easy solution. There are two programs that are run on the Pi: sensor.py, which handles all things sensor related, and HeartbeatClient.py, which is used as a health checker for the Pi.

## sensor.py
This is the program that houses all sensor functionality. The library RPi.GPIO is used to communicate with the sensors. Anytime the count needs to be updated, an http post is used to send the information to the web service. There are two main pieces to this program: determining ins/outs and calibration settings to provide more accurate functionality.
## Ins/Outs
  The direction of a person (i.e. an in or an out) is determined by which order the sensors are tripped in. This is kept track of with the variables t1 and t2. When a sensor is tripped, it checks if the other sensor has been tripped or not. If it has, and the time between trips is not above the set value (discussed below in calibration setting), then an in/out has occurred and the flags are reset. If the other sensor has not be tripped yet, the flag and time stamp for the corresponding sensor is set. 
## Calibration Settings
  To provide as much flexibility and precision as possible, there are several things that can be calibrated. First, the distance between the sensors is important. If they are too close, their fields of view will overlap and accuracy will be lost. If they are too far apart, people could stand in-between the fields of view and be unseen by either sensor.  Second, the so-called sensor_timeout, is the minimum amount of time that must pass between consecutive trips of a given sensor. This is used to ensure that the person that triggers the sensor trip has enough time to exit the field of view of the tripped sensor before it can trip again. Finally, the multiple_trigger_timeout is the maximum amount of time that can pass between the trip of one sensor and the trip of the other. This is used to handle false trips where one sensor is tripped and it is not something contributing to an in/out.

## HeartbeatClient.py
This is a simple program that periodically does an http post to the web service. This is just to used to provide the server with knowledge that the Pi is up and running. Ideally, if the server does not receive a heartbeat in a given amount of time, someone is notified that something may be wrong with the Pi. 
