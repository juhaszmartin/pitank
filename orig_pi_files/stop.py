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

try:
   pwm_AIN1.stop()
   pwm_AIN2.stop()
   pwm_BIN1.stop()
   pwm_BIN2.stop()
finally:
   pwm_AIN1.stop()
   pwm_AIN2.stop()
   pwm_BIN1.stop()
   pwm_BIN2.stop()