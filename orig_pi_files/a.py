from picamera2 import Picamera2
import time

# Initialize Picamera2
picam2 = Picamera2()

# Configure a simple capture mode
config = picam2.create_still_configuration()
picam2.configure(config)

# Start the camera
picam2.start()
time.sleep(2)  # Let camera adjust to lighting

# Capture image and save as JPEG
picam2.capture_file("a.jpg")


