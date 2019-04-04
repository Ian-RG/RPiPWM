import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin = 21
triggerPin = 4
echoPin = 17

GPIO.setup(led_pin, GPIO.OUT)
pwm = GPIO.PWM(led_pin, 100)
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

pwm.start(0)
try:
    while 1:
        GPIO.output(triggerPin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(triggerPin, GPIO.LOW)
        
        while GPIO.input(echoPin) == 0:
            pulseStartTime = time.time()
        while GPIO.input(echoPin) == 1:
            pulseEndTime = time.time()
            
        pulseDuration = pulseEndTime-pulseStartTime
        outputVal = 100 - ((pulseDuration*17150)*4) #*4 will use 1/4 of a metre (25cm) as the max range
        if (outputVal < 0): outputVal = 0
        pwm.ChangeDutyCycle(outputVal)
        time.sleep(0.1)
  

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()
