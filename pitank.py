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

class PiTank:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(AIN1, GPIO.OUT)
        GPIO.setup(AIN2, GPIO.OUT)
        GPIO.setup(BIN1, GPIO.OUT)
        GPIO.setup(BIN2, GPIO.OUT)

        self.pwm_AIN1 = GPIO.PWM(AIN1, FREQ)
        self.pwm_AIN2 = GPIO.PWM(AIN2, FREQ)
        self.pwm_BIN1 = GPIO.PWM(BIN1, FREQ)
        self.pwm_BIN2 = GPIO.PWM(BIN2, FREQ)

        self.pwm_AIN1.start(0)
        self.pwm_AIN2.start(0)
        self.pwm_BIN1.start(0)
        self.pwm_BIN2.start(0)

    def set_motor_speed(pwm1, pwm2, speed):
        """Control motor with speed (-100 to 100)."""
        print (f"Setting motor speed to {speed}%")
        print (f"pwm1: {pwm1}, pwm2: {pwm2}")
        if speed < 0:  # backward
            pwm1.ChangeDutyCycle(-speed)
            pwm2.ChangeDutyCycle(0)
        elif speed > 0:  # forward
            pwm1.ChangeDutyCycle(0)
            pwm2.ChangeDutyCycle(speed)
        else:  # stop
            pwm1.ChangeDutyCycle(0)
            pwm2.ChangeDutyCycle(0)

    def stop(self):
        """Stop both motors."""
        PiTank.set_motor_speed(self.pwm_AIN1, self.pwm_AIN2, 0)
        PiTank.set_motor_speed(self.pwm_BIN1, self.pwm_BIN2, 0)

    def turn_left(self, speed=50, time_duration=0.4):
        """Turn left by running right motor forward and left motor backward."""
        PiTank.set_motor_speed(self.pwm_AIN1, self.pwm_AIN2, speed)
        PiTank.set_motor_speed(self.pwm_BIN1, self.pwm_BIN2, -speed)
        time.sleep(time_duration)
        self.stop()

    def turn_right(self, speed=50, time_duration=0.4):
        """Turn right by running left motor forward and right motor backward."""
        PiTank.set_motor_speed(self.pwm_AIN1, self.pwm_AIN2, -speed)
        PiTank.set_motor_speed(self.pwm_BIN1, self.pwm_BIN2, speed)
        time.sleep(time_duration)
        self.stop()

    def move_forward(self, speed=50):
        """Move forward by running both motors forward."""
        PiTank.set_motor_speed(self.pwm_AIN1, self.pwm_AIN2, speed)
        PiTank.set_motor_speed(self.pwm_BIN1, self.pwm_BIN2, speed)

    def move_backward(self, speed=50):
        """Move backward by running both motors backward."""
        PiTank.set_motor_speed(self.pwm_AIN1, self.pwm_AIN2, -speed)
        PiTank.set_motor_speed(self.pwm_BIN1, self.pwm_BIN2, -speed)
    
if __name__ == "__main__":
    controls = PiTank()
    try:
        controls.turn_right(100, 0.4) # this is around 90 degrees
    except KeyboardInterrupt:
        pass
    finally:
        controls.stop()
        # GPIO.cleanup()
