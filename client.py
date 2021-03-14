# import the necessary packages
from imutils.video import VideoStream
import imagezmq
import argparse
import socket
import time
import imutils
import cv2
from motorControll import *

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--server-ip", required=True,
        help="ip address of the server to which the client will connect")
args = vars(ap.parse_args())

sender = imagezmq.ImageSender(connect_to="tcp://{}:5555".format(
        args["server_ip"]))

rpiName = socket.gethostname()

vs = VideoStream(src=-1).start()
time.sleep(2.0)

frame_width = 640
frame_height = 480

def get_angle(power):
    normalized = power / (frame_width//2)
    cam_fov = 70
    angle = (cam_fov//2) * normalized
    return angle

rotate_speed = 8
def take_action(command, power):
        global moveable
        if command == "LEFT":
                angle = get_angle(power)
                left()
                time.sleep((rotate_speed*angle)/90)
                stop()
                
        if command == "RIGHT":
                angle = get_angle(power)
                right()
                time.sleep((rotate_speed*angle)/90)
                stop()

        if command == "FORWARD":
                angle = get_angle(power)
                forward()
                time.sleep((power/40))
                stop()

        if command == "PICKUP":
                pickup()
        moveable = True


moveable = False
while True:
        global moveable
        frame = vs.read()
        frame=imutils.resize(frame,width=frame_width,height=frame_height)
        answer = sender.send_image(rpiName, frame).decode("ascii")
        command, power = answer.split[" "]
        if moveable:
                take_action(command, power)

        if cv2.waitKey(1) & 0xFF == ord('q'): break

vs.stream.strea.release()
