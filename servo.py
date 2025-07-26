import RPi.GPIO as GPIO
import time

SERVO_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)  # 50Hz
pwm.start(0)

def set_angle(angle):
    duty = 2.5 + (angle / 180.0) * 10
    pwm.ChangeDutyCycle(duty)
try:
    while True:
        for angle in range(20, 160, 1):   # 0 → 180° in 1° steps
            set_angle(angle)
            time.sleep(0.01)
        for angle in range(160, 20, -1): # 180 → 0° in 1° steps
            set_angle(angle)
            time.sleep(0.01)
except KeyboardInterrupt:
    pass

finally:
    if pwm is not None:
        pwm.stop()
    GPIO.cleanup()

