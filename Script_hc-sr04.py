import RPi.GPIO as GPIO
import time
import pulseio
import board
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24
TRIG_2 = 22
ECHO_2 = 27

R_MOTOR_1 = 1 #change me (RED)
R_MOTOR_2 = 1 #change me (BROWN)

L_MOTOR_1 = 1 #change me (RED)
L_MOTOR_2 = 1 #change me  (BROWN)

# Forward - > R_MOTOR_1 and L_MOTOR_1 high
# Backwards -> R_MOTOR_2 and L_MOTOR_2 high

# Left - > R_MOTOR_1 and L_MOTOR_2 high
# Right - > L_MOTOR_1 and R_MOTOR_2 high

# Stop - > All low

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(TRIG_2, GPIO.OUT)
GPIO.setup(ECHO_2, GPIO.IN)
GPIO.setup(R_MOTOR_1, GPIO.OUT)
GPIO.setup(R_MOTOR_2, GPIO.OUT)
GPIO.setup(L_MOTOR_1, GPIO.OUT)
GPIO.setup(L_MOTOR_2, GPIO.OUT)

def forward():
        GPIO.output(R_MOTOR_1, GPIO.HIGH)
        GPIO.output(L_MOTOR_1, GPIO.HIGH)
        GPIO.output(R_MOTOR_2, GPIO.LOW)
        GPIO.output(L_MOTOR_2, GPIO.LOW)

def backwards():
        GPIO.output(R_MOTOR_2, GPIO.HIGH)
        GPIO.output(L_MOTOR_2, GPIO.HIGH)
        GPIO.output(R_MOTOR_1, GPIO.LOW)
        GPIO.output(L_MOTOR_1, GPIO.LOW)

def left():
        GPIO.output(R_MOTOR_1, GPIO.HIGH)
        GPIO.output(L_MOTOR_2, GPIO.HIGH)
        GPIO.output(R_MOTOR_2, GPIO.LOW)
        GPIO.output(L_MOTOR_1, GPIO.LOW)
        
def right():
        GPIO.output(R_MOTOR_2, GPIO.HIGH)
        GPIO.output(L_MOTOR_1, GPIO.HIGH)
        GPIO.output(R_MOTOR_1, GPIO.LOW)
        GPIO.output(L_MOTOR_2, GPIO.LOW)

def stop():
        GPIO.output(R_MOTOR_1, GPIO.LOW)
        GPIO.output(L_MOTOR_1, GPIO.LOW)
        GPIO.output(R_MOTOR_2, GPIO.LOW)
        GPIO.output(L_MOTOR_2, GPIO.LOW)

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

                if distance <= 22:
                        stop()

except KeyboardInterrupt:
        print("Cleaning up!")
        GPIO.cleanup()
