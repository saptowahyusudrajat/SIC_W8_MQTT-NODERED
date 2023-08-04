import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM (Broadcom SOC channel numbering)
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for trigger and echo
trig_pin = 21
echo_pin = 20

# Set up GPIO pins
GPIO.setup(trig_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

def measure_distance():
    # Send a short pulse to the trigger pin (10 microseconds)
    GPIO.output(trig_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig_pin, GPIO.LOW)

    # Measure the time taken for the pulse to travel back and forth
    while GPIO.input(echo_pin) == GPIO.LOW:
        pulse_start_time = time.time()

    while GPIO.input(echo_pin) == GPIO.HIGH:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time

    # Calculate the distance using the speed of sound (34300 cm/s)
    # and considering the pulse traveled to the object and back
    distance_cm = (pulse_duration * 34300) / 2

    return distance_cm

try:
    while True:
        distance = measure_distance()
        print(f"Distance: {distance:.2f} cm")
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    GPIO.cleanup()