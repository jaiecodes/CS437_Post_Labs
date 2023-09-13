import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from sense_hat import SenseHat
from datetime import datetime
import numpy as np
import time

sense = SenseHat()
temps = np.array([])
avg_temps = np.array([])
time = np.array([])


style.use("fivethirtyeight")
fig - plt.figure(num= "Temperature", figsize=[13,3])
ax1 = fig.add_subplore(1,1,1)

def get_data():
  data = np.array([])
  temperature = sense.get_temperature()
  temperature = round(temperature,1)
  data.append(temperature)
  temps.append(temperature)

  temp_array = np.array([])
  for i in range(4):
    temp=sense.get_temperature()
    temp_array.append(temp)

  avg_temp = np.mean(temp_array)
  data.append(avg_temp)
  avg_temps.append(avg_temp)

  curr_time = datetime.now()
  time.append(curr_time)
  data.append(curr_time)
  return data

def animate(i):
  data = get_temps()
  ax1.clear()
  ax1.plot(time, temps)
  ax1.plot(time, avg_temps)
  ax1.legend(["Temp", "Avg Temp"])
  print(data)

  ani = animation.FuncAnimation(fig, animate, interval=1000)
  plt.show()

