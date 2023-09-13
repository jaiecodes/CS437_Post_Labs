import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from sense_hat import SenseHat
from datetime import datetime
import numpy as np
import time

sense = SenseHat()
temps = []
avg_temps = []
time = []


style.use("fivethirtyeight")
fig = plt.figure(num= "Temperature", figsize=[13,3])
ax1 = fig.add_subplot(1,1,1)

def get_data():
  data = []
  temperature = sense.get_temperature()
  #temperature = round(temperature,1)
  temps.append(temperature)
  data.append(temperature)

  temp = sense.get_temperature()
  temp_array = temps.copy()
  temp_array = temp_array.append(temp)
  
  avg_temp = np.mean(np.array(temp_array))
  avg_temps.append(avg_temp)
  data.append(avg_temp)

  curr_time = datetime.now()
  time.append(curr_time)
  data.append(curr_time)
  return data

def animate(i):
  data = get_data()
  ax1.clear()
  ax1.plot(time, temps)
  ax1.plot(time, avg_temps)
  ax1.legend(["Temp", "Avg Temp"])
  print(data)


animation = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

