import numpy as np
import time
from datetime import datetime,date
import matplotlib.pyplot as plt
import pandas as pd


## Install the following libraries if they are not already installed on your Raspi:
## pip3 install seaborn
## sudo apt-get install python3-pandas
## sudo apt-get install python3-matplotlib



filename="/home/pi/Desktop/IMUData15:13:39.csv"

## CSV file template:
# time in seconds, timestamp (H:M:S), X-Acceleration, Y-Acceleration, Z-Acceleration, X-Gyroscope, Y-Gyro,Z-Gyro, X-Gyro, Y-Gyro, Z-gyro


df =pd.read_csv(filename, header=None)
df=df.dropna()

timestamp = df[0]

timestamps2=df[1]
x_axis=df[2]
y_axis=df[3]
z_axis=df[4]
rssi=df[5]


## Plot X and Y positions with respect to time:
plt.plot(timestamp.to_numpy(),x_axis.to_numpy(), label="X positions", c="red")
plt.plot(timestamp.to_numpy(),y_axis.to_numpy(), label="Y positions", c="green")
plt.legend(loc="upper left")
plt.xlabel("Timestamp (seconds)")
plt.ylabel("Positions (m)")
#plt.ylim(-5, 5)  # Set the y-axis limits
plt.show()


## Visualizing scatter plot in 2D

window_size = 10 
rssi_smoothed = rssi.rolling(window=window_size).mean() 

plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
scatter = plt.scatter(x_axis.to_numpy(), y_axis.to_numpy(), c=rssi_smoothed, cmap='viridis', marker='o')

# Add labels and a colorbar
plt.xlabel('X position')
plt.ylabel('Y position')
cbar = plt.colorbar(scatter, label='RSSI')
cbar.set_label('RSSI')
#plt.ylim(-5, 5) # Set the y-axis limits
plt.show()
##