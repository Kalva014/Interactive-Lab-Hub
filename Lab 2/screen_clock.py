import time
import subprocess
import digitalio
import board
import datetime
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/quicksand/Quicksand-Regular.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# BUTTON SETUP
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()
t = 4500 #1 hour and 15 minutes converted into seconds left
dayOfTheWeek = 0
while True:
    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    y = -2# Padding
    t -= 1 # Class time
    
    if buttonA.value and buttonB.value:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.rectangle((0, 0, width, height / 2), outline=0, fill=500)
        #draw.text((x, y), "Press top button for time\n until Graduation! \n\n\nPress bottom button for time\n until class!", font=ImageFont.truetype("/usr/share/fonts/truetype/quicksand/Quicksand-Regular.ttf", 18), fill="#FFFFFF")
        draw.text((x, y), "\n      Time until Graduation! \n\n\n           Time until class!", font=ImageFont.truetype("/usr/share/fonts/truetype/quicksand/Quicksand-Regular.ttf", 18), fill="#FFFFFF")
    if not buttonA.value and not buttonB.value:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        monday_str = "Monday To Do List:\n   -Finish IDD homework\n   -Cook dinner\n   -Push workout"
        tuesday_str = "Tuesday To Do List:\n   -Finish VR/AR homework\n   -Cook lunch\n   -Pull workout"
        wednesday_str = "Wednesday To Do List:\n   -Finish MLE homework\n   -Buy takeout\n   -Legs workout"
        thursday_str = "Thursday To Do List:\n   -Finish Robotics homework\n   -Cook breakfast\n   -Buy groceries"
        friday_str = "Friday To Do List:\n   -Finish Product Studio\n   -Meet with the professor\n   -Play soccer with friends"
        saturday_str = "Saturday To Do List:\n   -Check out the Brooklyn\n   -Call parents\n   -Meet with friends"
        sunday_str = "Sunday To Do List:\n   -Check out museum\n   -Apply for jobs\n   -Legs workout"
        daily_planner = []
        daily_planner.append(monday_str)
        daily_planner.append(tuesday_str)
        daily_planner.append(wednesday_str)
        daily_planner.append(thursday_str)
        daily_planner.append(friday_str)
        daily_planner.append(saturday_str)
        daily_planner.append(sunday_str)
        draw.text((x, y), daily_planner[dayOfTheWeek], font=ImageFont.truetype("/usr/share/fonts/truetype/quicksand/Quicksand-Regular.ttf", 18), fill="#FFFFFF")
        if dayOfTheWeek == len(daily_planner) - 1:
            dayOfTheWeek = 0
        else:
            dayOfTheWeek += 1
    if not buttonA.value and buttonB.value:
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        time.sleep(0.0000001)
        time_until_date = datetime.datetime(2023, 5, 27) - datetime.datetime.now()
        total_seconds = round((time_until_date).total_seconds())
        total_minutes = round(total_seconds / 60)
        total_hours = round(total_minutes / 60)
        total_days = round(total_hours / 24)
        total_weeks = round(total_days / 7)
        time_str = "Time Left Until Graduation:\nWeeks: " + str(total_weeks) + "\nDays: " + str(total_days) + "\nHours: " + str(total_hours) + "\nMinutes: " + str(total_minutes)  + "\nSeconds: " + str(total_seconds)
        draw.text((x, y), time_str, font=ImageFont.truetype("/usr/share/fonts/truetype/quicksand/Quicksand-Regular.ttf", 18), fill="#FFFFFF")
    if not buttonB.value and buttonA.value:
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        mins, secs = divmod(t, 60)
        time_str = "Time Left Until Class Ends:\nMinutes: " + str(mins) + "\nSeconds: " + str(secs)
        time.sleep(0.01)
        #t -= 1
        draw.text((x, y), time_str, font=ImageFont.truetype("/usr/share/fonts/truetype/quicksand/Quicksand-Regular.ttf", 18), fill="#FFFFFF")

    # Display image.
    disp.image(image, rotation)
    time.sleep(1)

