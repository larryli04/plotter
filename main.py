import sys
import RPi.GPIO as GPIO
import time
from math import sin, cos, radians

# Config
X_DIR, X_STEP = 17, 27
Y_DIR, Y_STEP = 2, 3

SPEED_STEPS_PER_SEC = 10000  # overall vector speed
STEP_DELAY = 1 / SPEED_STEPS_PER_SEC

GPIO.setmode(GPIO.BCM)
GPIO.setup([X_DIR, X_STEP, Y_DIR, Y_STEP], GPIO.OUT)

SERVO_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# State
current_x, current_y = 0, 0

# handle arguments
n = len(sys.argv)
if(n == 3 and sys.argv[1] == "-f"):
    filename = sys.argv[2]
elif(n==2 and sys.argv[1] == "-c"):
    filename = None
    # initialize controller stuff (maybe use pygame)
    print("Controller not currently supported") 
    exit(1)

pwm = GPIO.PWM(SERVO_PIN, 50)  # 50Hz
pwm.start(0)

def dot(r: int):
    global current_x, current_y
    loc_x=current_x
    loc_y=current_y
    for theta in range(0,360*5):
        angle=radians(theta)
        goto(loc_x+((theta/(360*5))*r*cos(angle)), loc_y+((theta/(360*5))*r*sin(angle)))
        time.sleep(0.001)

    goto(loc_x, loc_y)
def set_angle(angle):
    duty = 2.5 + (angle / 180.0) * 10
    pwm.ChangeDutyCycle(duty)

def penDown():
    set_angle(160)

def penUp():
    set_angle(70)

def zero():
    global current_x, current_y
    current_x=0
    current_y=0

def goto(x_in: float, y_in:float):
    global current_x, current_y
    x=int(x_in)
    y=int(y_in)
    dx = x - current_x
    dy = y - current_y

    steps_x = abs(dx)
    steps_y = abs(dy)
    dir_x = dx > 0
    dir_y = dy > 0

    GPIO.output(X_DIR, dir_x)
    GPIO.output(Y_DIR, not dir_y)

    total_steps = max(steps_x, steps_y)
    if total_steps == 0:
        return

    ratio_x = steps_x / total_steps if steps_x else 0
    ratio_y = steps_y / total_steps if steps_y else 0
    acc_x = acc_y = 0.0

    for _ in range(total_steps):
        acc_x += ratio_x
        acc_y += ratio_y

        if acc_x >= 1:
            GPIO.output(X_STEP, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(X_STEP, GPIO.LOW)
            acc_x -= 1

        if acc_y >= 1:
            GPIO.output(Y_STEP, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(Y_STEP, GPIO.LOW)
            acc_y -= 1

        time.sleep(STEP_DELAY)

    current_x, current_y = x, y

def main():
    # zero plotter

    set_angle(110)
    # run with controller
    goto(1000,0)
    goto(1000,1000)
    goto(0,1000)
    goto(0,0)

    for theta in range(0,360):
        angle = radians(theta)
        goto(int(1000*cos(angle)), int(1000*sin(angle)))


    # run with predefined file

    goto(0,0)
if __name__ == "__main__":
    main()

