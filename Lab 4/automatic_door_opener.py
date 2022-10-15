import qwiic
import time
import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from adafruit_servokit import ServoKit

# Distance sensor
ToF = qwiic.QwiicVL53L1X()
if (ToF.sensor_init() == None):					 # Begin returns 0 on a good init
    print("Sensor online!\n")

# THIS IS FOR THE LED SCREEN
i2c = busio.I2C(board.SCL, board.SDA) # Create the I2C interface.
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c) # Create the SSD1306 OLED class.
oled.fill(0)
oled.show()
image = Image.new("1", (oled.width, oled.height)) # Create blank image for drawing.
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
#draw.text((0, 0), "Hello!", font=font, fill=255)

#THIS IS FOR THE SERVO
# Set channels to the number of servo channels on your kit. There are 16 channels on the PCA9685 chip.
kit = ServoKit(channels=16)
servo = kit.servo[2] # Name and set up the servo according to the channel you are using.
servo.set_pulse_width_range(500, 2500)# Set the pulse width range of your servo for PWM control of rotating 0-180 degree (min_pulse, max_pulse). Each servo might be different, you can normally find this information in the servo datasheet

while True:
    try:
        # Distance Sensor
        ToF.start_ranging()						 # Write configuration bytes to initiate measurement
        time.sleep(.005)
        distance = ToF.get_distance()	 # Get the result of the measurement from the sensor
        time.sleep(.005)
        ToF.stop_ranging()
        distanceInches = distance / 25.4
        distanceFeet = distanceInches / 12.0
        #print("Distance(mm): %s Distance(ft): %s" % (distance, distanceFeet))

        # LED SCREEN
        oled.fill(0) # Create blank image for drawing.
        image = Image.new("1", (oled.width, oled.height))
        draw = ImageDraw.Draw(image)

        # Determine if locked or unlocked
        if distanceFeet <= 5:
            draw.text((0, 0), "UNLOCKED!", font=font, fill=255) # SET THE LED SCREEN
            servo.angle = 180 # Set the servo to 180 degree position
            #time.sleep(2)
        else:
            draw.text((0, 0), "LOCKED!", font=font, fill=255) # SET THE LED SCREEN
            servo.angle = 0 # Set the servo to 0 degree position
            #time.sleep(2)

        
        #LED SCREEN
        oled.image(image) # Display image
        oled.show() # show all the changes we just made
    
    except Exception as e:
        # Once interrupted, set the servo back to 0 degree position
        servo.angle = 0
        time.sleep(0.5)

        print(e)