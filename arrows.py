from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

# Set up the colours (white, green, red, empty)
w = (150, 150, 150)
g = (0, 255, 0)
r = (255, 0, 0)
e = (0, 0, 0)

# Create images for three different coloured arrows

arrow = [
e,e,e,w,w,e,e,e,
e,e,w,w,w,w,e,e,
e,w,e,w,w,e,w,e,
w,e,e,w,w,e,e,w,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e
]

arrow_red = [
e,e,e,r,r,e,e,e,
e,e,r,r,r,r,e,e,
e,r,e,r,r,e,r,e,
r,e,e,r,r,e,e,r,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e
]

arrow_green = [
e,e,e,g,g,e,e,e,
e,e,g,g,g,g,e,e,
e,g,e,g,g,e,g,e,
g,e,e,g,g,e,e,g,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e
]

while True:
  sense.set_rotation(90)
  sense.set_pixels(arrow)
  sleep(2)
  
  sense.set_rotation(180)
  sense.set_pixels(arrow_green)
  sleep(2)
  
  sense.set_rotation(270)
  sense.set_pixels(arrow)
  sleep(2)
  
  sense.set_rotation(0)
  sense.set_pixels(arrow_red)
  sleep(2)
