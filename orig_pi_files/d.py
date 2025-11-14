import RPi.GPIO as GPIO
import time

# Pin setup (adjust to your wiring)
# Motor A
AIN1 = 6
AIN2 = 13
# Motor B
BIN1 = 19
BIN2 = 26

# Frequency for PWM
FREQ = 1000

GPIO.setmode(GPIO.BCM)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

pwm_AIN1 = GPIO.PWM(AIN1, FREQ)
pwm_AIN2 = GPIO.PWM(AIN2, FREQ)
pwm_BIN1 = GPIO.PWM(BIN1, FREQ)
pwm_BIN2 = GPIO.PWM(BIN2, FREQ)

pwm_AIN1.start(0)
pwm_AIN2.start(0)
pwm_BIN1.start(0)
pwm_BIN2.start(0)

def motor_control(pwm1, pwm2, speed):
    """Control motor with speed (-100 to 100)."""
    if speed > 0:  # forward
        pwm1.ChangeDutyCycle(speed)
        pwm2.ChangeDutyCycle(0)
    elif speed < 0:  # backward
        pwm1.ChangeDutyCycle(0)
        pwm2.ChangeDutyCycle(-speed)
    else:  # stop
        pwm1.ChangeDutyCycle(0)
        pwm2.ChangeDutyCycle(0)

try:
    speeds = [100, 0]
    for s in speeds:
        print(f"Motor A at {s}%")
        motor_control(pwm_AIN1, pwm_AIN2, s)
        time.sleep(1)
    for s in speeds:
        print(f"Motor B at {s}%")
        motor_control(pwm_BIN1, pwm_BIN2, s)
        time.sleep(1)

finally:
    pwm_AIN1.stop()
    pwm_AIN2.stop()
    pwm_BIN1.stop()
    pwm_BIN2.stop()
    #GPIO.cleanup()

