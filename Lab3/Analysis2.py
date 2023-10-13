import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt

import time
from datetime import datetime,date

import pandas as pd


filename="/home/pi/Desktop/IMUData22:03:32.csv"

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
# Data cleansing (optional)
# Remove outliers, fill missing data, etc.

# Spatial interpolation
# Define a grid of x, y coordinates for interpolation
x_interp = np.linspace(min(x_axis), max(x_axis), 100)
y_interp = np.linspace(min(y_axis), max(y_axis), 100)
X, Y = np.meshgrid(x_interp, y_interp)

# Choose an interpolation method (IDW in this example)
interp_method = 'linear'
rssi_interp = griddata((x_axis, y_axis), rssi, (X, Y), method=interp_method)

# Improved Positioning Algorithm (replace with your algorithm)
# Estimated x and y coordinates based on the improved algorithm
x_estimated = np.array([1.5, 2.5, 3.5, 4.5])
y_estimated = np.array([1.5, 2.5, 3.5, 4.5])

# Plot data
plt.figure(figsize=(10, 8))

# Plot interpolated RSSI values
plt.contourf(X, Y, rssi_interp, 20, cmap='viridis')
plt.colorbar()

# Plot estimated positions
plt.scatter(x_estimated, y_estimated, c='red', label='Estimated Positions', s=100, marker='x')

# Plot original data points
plt.scatter(x, y, c='blue', label='Original Data', s=50, marker='o')

plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Interpolated RSSI Data with Estimated Positions')
plt.legend()
plt.grid(True)
plt.show()
