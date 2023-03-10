import RPi.GPIO as GPIO
import time

# Define the GPIO pins for each servo motor
BASE_PIN = 18
SHOULDER_PIN = 23
ELBOW_PIN = 24
WRIST_PIN = 25
GRIPPER_PIN = 12
ROTATE_PIN = 16

# Set the PWM frequency in Hz
PWM_FREQ = 50

# Set the PWM duty cycle ranges for each servo motor
BASE_DUTY_MIN = 2.5
BASE_DUTY_MAX = 12.5
SHOULDER_DUTY_MIN = 2.5
SHOULDER_DUTY_MAX = 12.5
ELBOW_DUTY_MIN = 2.5
ELBOW_DUTY_MAX = 12.5
WRIST_DUTY_MIN = 2.5
WRIST_DUTY_MAX = 12.5
GRIPPER_DUTY_MIN = 2.5
GRIPPER_DUTY_MAX = 12.5
ROTATE_DUTY_MIN = 2.5
ROTATE_DUTY_MAX = 12.5

# Initialize the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(BASE_PIN, GPIO.OUT)
GPIO.setup(SHOULDER_PIN, GPIO.OUT)
GPIO.setup(ELBOW_PIN, GPIO.OUT)
GPIO.setup(WRIST_PIN, GPIO.OUT)
GPIO.setup(GRIPPER_PIN, GPIO.OUT)
GPIO.setup(ROTATE_PIN, GPIO.OUT)

# Create PWM objects for each servo motor
base_pwm = GPIO.PWM(BASE_PIN, PWM_FREQ)
shoulder_pwm = GPIO.PWM(SHOULDER_PIN, PWM_FREQ)
elbow_pwm = GPIO.PWM(ELBOW_PIN, PWM_FREQ)
wrist_pwm = GPIO.PWM(WRIST_PIN, PWM_FREQ)
gripper_pwm = GPIO.PWM(GRIPPER_PIN, PWM_FREQ)
rotate_pwm = GPIO.PWM(ROTATE_PIN, PWM_FREQ)

# Start the PWM signals for each servo motor
base_pwm.start(BASE_DUTY_MIN)
shoulder_pwm.start(SHOULDER_DUTY_MIN)
elbow_pwm.start(ELBOW_DUTY_MIN)
wrist_pwm.start(WRIST_DUTY_MIN)
gripper_pwm.start(GRIPPER_DUTY_MIN)
rotate_pwm.start(ROTATE_DUTY_MIN)

# Define functions to set the position of each servo motor
def set_base(angle):
    duty = ((BASE_DUTY_MAX - BASE_DUTY_MIN) / 180.0) * angle + BASE_DUTY_MIN
    base_pwm.ChangeDutyCycle(duty)

def set_shoulder(angle):
    duty = ((SHOULDER_DUTY_MAX - SHOULDER_DUTY_MIN) / 180.0) * angle + SHOULDER_DUTY_MIN
    shoulder_pwm.ChangeDutyCycle(duty)

def set_elbow(angle):
    duty = ((ELBOW_DUTY_MAX - ELBOW_DUTY_MIN) / 180.0) * angle + ELBOW_DUTY_MIN
    elbow_pwm.ChangeDutyCycle(duty)

def set_wrist(angle):
    duty = ((WRIST_DUTY_MAX - WRIST_DUTY_MIN) / 180.0) * angle + WRIST_DUTY_MIN
    wrist_pwm.ChangeDutyCycle(duty)

def set_gripper(angle):
    duty = ((GRIPPER_DUTY_MAX - GRIPPER_D_MIN) / 180.0) * angle + GRIPPER_DUTY_MIN
    gripper_pwm.ChangeDutyCycle(duty)

def set_rotate(angle):
    duty = ((ROTATE_DUTY_MAX - ROTATE_DUTY_MIN) / 180.0) * angle + ROTATE_DUTY_MIN
    rotate_pwm.ChangeDutyCycle(duty)

#Set the initial position of each servo motor
set_base(90)
set_shoulder(90)
set_elbow(90)
set_wrist(90)
set_gripper(90)
set_rotate(90)

#Wait for 2 seconds
time.sleep(2)

#Move the arm to a different position
set_base(45)
set_shoulder(135)
set_elbow(90)
set_wrist(45)
set_gripper(0)
set_rotate(180)

#Wait for 2 seconds
time.sleep(2)

#Move the arm back to the initial position
set_base(90)
set_shoulder(90)
set_elbow(90)
set_wrist(90)
set_gripper(90)
set_rotate(90)

#Stop the PWM signals for each servo motor
base_pwm.stop()
shoulder_pwm.stop()
elbow_pwm.stop()
wrist_pwm.stop()
gripper_pwm.stop()
rotate_pwm.stop()

#Clean up the GPIO pins
GPIO.cleanup()








import pygame
import RPi.GPIO as GPIO
import time

# Set up GPIO pins for the two servo motors
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
pwm_base = GPIO.PWM(11, 50)
pwm_arm = GPIO.PWM(13, 50)

# Start the PWM signals for the two servo motors
pwm_base.start(7.5)
pwm_arm.start(7.5)

# Initialize pygame joystick module
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

try:
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                # Get axis values from joysticks
                axis_0 = joysticks[0].get_axis(0)
                axis_1 = joysticks[0].get_axis(1)
                axis_2 = joysticks[1].get_axis(1)
                
                # Control the servo motors based on joystick axis values
                base_angle = 90 + int(axis_0 * 45)
                arm_angle = 90 + int(axis_1 * 45)
                
                pwm_base.ChangeDutyCycle(2.5 + 10 * base_angle / 180)
                pwm_arm.ChangeDutyCycle(2.5 + 10 * arm_angle / 180)
                
        time.sleep(0.01)

except KeyboardInterrupt:
    pass

# Stop the PWM signals for the two servo motors
pwm_base.stop()
pwm_arm.stop()

# Clean up the GPIO pins
GPIO.cleanup()

# Quit pygame
pygame.quit()
