from sense_hat import SenseHat
import numpy as np
import time

sense = SenseHat()
temperatures = np.array([])
while True:
  temperature=sense.get_temperature()
  
