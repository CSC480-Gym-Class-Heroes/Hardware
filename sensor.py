import RPi.GPIO as GPIO
import time
import py_compile
import datetime
import requests

GPIO.setmode(GPIO.BCM)

PIR_PIN1 = 7
PIR_PIN2 = 9
t1 = 0
t2 = 0
count = 0
t1_time = datetime.datetime.now()
t2_time = datetime.datetime.now()
url='http://pi.cs.oswego.edu:8080/Gym/updatecount?'
gym_param='gym='
gym='glimmerglass'
#gym='cooper'                                                                                   
timestamp_param='timestamp='
count_param='count='

GPIO.setup(PIR_PIN1, GPIO.IN)
GPIO.setup(PIR_PIN2, GPIO.IN)

def MOTION(PIR_PIN):
    global t1
    global t2
    global count
    global t1_time
    global t2_time

    #print "Motion Detected PIN: " + str(PIR_PIN)                                               

    if PIR_PIN == 7:
        if t2 == 1:
            if abs(t1_time-datetime.datetime.now()).total_seconds() < 1:
                return
            t1_time = datetime.datetime.now()
            print "Motion Detected PIN: " + str(PIR_PIN)
            if abs(t1_time-t2_time).total_seconds() < 5:
                print "out"
                count = count - 1
                t2 = 0
                #r=requests.post(url+gym_param+gym+'&'+timestamp_param+str(int(time.time()*1000\))+'&'+count_param+str(count))                                                                  
                #print r.status_code                                                            
            else:
                t1 = 1
                t2 = 0
   

      else:
            t1 = 1
            if abs(t1_time-datetime.datetime.now()).total_seconds() < 1:
                return
            t1_time = datetime.datetime.now()
            print "Motion Detected PIN: " + str(PIR_PIN)
    elif PIR_PIN == 9:
        if t1 == 1:
            if abs(t2_time-datetime.datetime.now()).total_seconds() < 1:
                return
            t2_time = datetime.datetime.now()
            print "Motion Detected PIN: " + str(PIR_PIN)
            if abs(t1_time-t2_time).total_seconds() < 5:
                print "in"
                count = count + 1
                t1 = 0
                #r=requests.post(url+gym_param+gym+'&'+timestamp_param+str(int(time.time()*1000\
))+'&'+count_param+str(count))                                                                  
                #print r.status_code                                                            
            else:
                t1 = 0
                t2 = 1
        else:
            t2 = 1
            if abs(t2_time-datetime.datetime.now()).total_seconds() < 1:
                return
            t2_time = datetime.datetime.now()
            print "Motion Detected PIN: " + str(PIR_PIN)


print "PIR Module Test (CTRL+C to exit)"

#time.sleep(2)                                                                                  
#print "Pulling power from Sweden"                                                              
#time.sleep(2)                                                                                  
#print "Spinning up LHC"                                                                        
#time.sleep(2)                                                                                  

print "Initialize Science"
print "Ready"

try:

    GPIO.add_event_detect(PIR_PIN1, GPIO.RISING, callback=MOTION)
    GPIO.add_event_detect(PIR_PIN2, GPIO.RISING, callback=MOTION)

    while 1:
        time.sleep(0)

except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()
