import sys
import RPi.GPIO as GPIO
import time

# Config
X_DIR, X_STEP = 2, 3
Y_DIR, Y_STEP = 17, 27

SPEED_STEPS_PER_SEC = 10000  # overall vector speed
STEP_DELAY = 1 / SPEED_STEPS_PER_SEC

GPIO.setmode(GPIO.BCM)
GPIO.setup([X_DIR, X_STEP, Y_DIR, Y_STEP], GPIO.OUT)

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

def penDown():
    pass

def penUp():
    pass

def goto(x: int, y:int):
    global current_x, current_y
    dx = x - current_x
    dy = y - current_y

    steps_x = abs(dx)
    steps_y = abs(dy)
    dir_x = dx > 0
    dir_y = dy > 0

    GPIO.output(X_DIR, dir_x)
    GPIO.output(Y_DIR, dir_y)

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

    # run with controller
    goto(1000,0)
    goto(1000,1000)
    goto(0,1000)
    goto(0,0)

    # run with predefined file
if __name__ == "__main__":
    main()

