import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24
TRIG_2 = 22
ECHO_2 = 27

R_MOTOR_1 = 5 
R_MOTOR_2 = 6 

L_MOTOR_1 = 25 
L_MOTOR_2 = 17 

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(TRIG_2, GPIO.OUT)
GPIO.setup(ECHO_2, GPIO.IN)
GPIO.setup(R_MOTOR_1, GPIO.OUT)
GPIO.setup(R_MOTOR_2, GPIO.OUT)
GPIO.setup(L_MOTOR_1, GPIO.OUT)
GPIO.setup(L_MOTOR_2, GPIO.OUT)

isMoved = False

def backwards():
        global isMoved
        if isMoved == False:
                isMoved = True
                GPIO.output(R_MOTOR_1, GPIO.HIGH)
                GPIO.output(L_MOTOR_1, GPIO.LOW)
                GPIO.output(R_MOTOR_2, GPIO.LOW)
                GPIO.output(L_MOTOR_2, GPIO.HIGH)
                isMoved = False

def forward():
        global isMoved
        if isMoved == False:
                isMoved = True
                GPIO.output(R_MOTOR_2, GPIO.HIGH)
                GPIO.output(L_MOTOR_2, GPIO.LOW)
                GPIO.output(R_MOTOR_1, GPIO.LOW)
                GPIO.output(L_MOTOR_1, GPIO.HIGH)
                isMoved = False

def left():
        global isMoved
        if isMoved == False:
                isMoved = True
                GPIO.output(R_MOTOR_1, GPIO.LOW)
                GPIO.output(L_MOTOR_2, GPIO.HIGH)
                GPIO.output(R_MOTOR_2, GPIO.HIGH)
                GPIO.output(L_MOTOR_1, GPIO.LOW)
                isMoved = False

def right():
        global isMoved
        if isMoved == False:
                isMoved = True
                GPIO.output(R_MOTOR_2, GPIO.HIGH)
                GPIO.output(L_MOTOR_1, GPIO.LOW)
                GPIO.output(R_MOTOR_1, GPIO.LOW)
                GPIO.output(L_MOTOR_2, GPIO.HIGH)
                isMoved = False

def stop():
        global isMoved
        if isMoved == False:
                isMoved = True
                GPIO.output(R_MOTOR_1, GPIO.LOW)
                GPIO.output(L_MOTOR_1, GPIO.LOW)
                GPIO.output(R_MOTOR_2, GPIO.LOW)
                GPIO.output(L_MOTOR_2, GPIO.LOW)
                isMoved = False

try:
    while True:
            GPIO.output(TRIG, False)
            print "Waiting for sensor to settle"
            time.sleep(2)

            GPIO.output(TRIG, True)
            time.sleep(0.1)
            GPIO.output(TRIG, False)

            while GPIO.input(ECHO)==0:
                    pulse_start = time.time()

            while GPIO.input(ECHO)==1:
                    pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 17150
            distance = round(distance, 2)
            print "Distance: ", distance, "cm"

            GPIO.output(TRIG_2, False)
            print "Waiting for sensor2 to settle"
            time.sleep(2)

            GPIO.output(TRIG_2, True)
            time.sleep(0.00001)
            GPIO.output(TRIG_2, False)

            while GPIO.input(ECHO_2)==0:
                    pulse_start_2 = time.time()

            while GPIO.input(ECHO_2)==1:
                    pulse_end_2 = time.time()

            pulse_duration_2 = pulse_end_2 - pulse_start_2
            distance_2 = pulse_duration_2 * 17150
            distance_2 = round(distance_2, 2)
            print "Distance: ", distance_2, "cm"

            if distance <= 41 or distance_2 <= 41:
                    stop()

except KeyboardInterrupt:
    print("Cleaning up!")
    GPIO.cleanup()

