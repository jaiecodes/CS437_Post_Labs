import numpy as np
import time
import scipy.signal as signal
from datetime import datetime,date
import matplotlib.pyplot as plt
import pandas as pd

import seaborn as sns # visualization


## Install the following libraries if they are not already installed on your Raspi:
## pip3 install seaborn
## sudo apt-get install python3-pandas
## sudo apt-get install python3-matplotlib



filename="/home/pi/Desktop/Code/Lab3/Part2/IMUDataRSSI16:35:57.csv"

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
plt.plot(x_axis,  label="X-axis Raw Acceleration")
plt.plot(y_axis,  label="Y-axis Raw Acceleration")
plt.plot(z_axis,  label="Z-axis Raw Acceleration")
plt.legend(loc="upper left")
plt.ylabel("Raw Acceleration in m/s^2")
plt.xlabel("Number of Data Points")

plt.show()
### CALIBERATION
x_calib_mean = np.mean(x_axis[10:5000])
## caliberate x,y,z to reduce the bias in accelerometer readings. Subtracting it from the mean means that in the absence of motion, the accelerometer reading is centered around zero to reduce the effect of integrigation drift or error.
## change the upper and lower bounds for computing the mean where the RPi is in static position at the begining of the experiment (i.e. for the first few readings). You can know these bounds from the exploratory plots above.
x_calib = x_axis - x_calib_mean
x_calib = x_calib[:]
timestamp = timestamp[:]

y_calib_mean = np.mean(y_axis[10:5000])
y_calib = y_axis - y_calib_mean
y_calib = y_calib[:]
timestamp = timestamp[:]


z_calib_mean = np.mean(y_axis[10:5000])
z_calib = z_axis - z_calib_mean
z_calib = z_calib[:]
timestamp = timestamp[:]

plt.plot(x_calib, label="X-axis Caliberated Acceleration")
plt.plot(y_calib, label="Y-axis Caliberated Acceleration")
plt.plot(z_axis, label="Z-axis Caliberated Acceleration")
plt.legend(loc="upper left")
plt.ylabel("Caliberated Acceleration in m/s^2")
plt.xlabel("Number of Data Points")
plt.ylim(-5, 5)  # Set the y-axis limits
plt.show()


#print("Check if lengths of each vector are same for tracking time", len(timestamp), len(x_calib), len(y_calib), len(z_calib))
# Find sampling time:
dt = (timestamp[len(timestamp)-1] - timestamp[0]) / len(timestamp)

## Computing Velocity and Position along Y Axis:
y_vel = [0]
for i in range(len(y_calib)-1):
    y_vel.append(y_vel[-1] + dt * y_calib[i])

y = [0]

for i in range(len(y_vel)-1):
    y.append(y[-1] + dt * y_vel[i])
    
## Integrations along X axis
x_vel = [0]
for i in range(len(x_calib)-1):
    x_vel.append(x_vel[-1] + dt * x_calib[i])

plt.plot(x_vel, label="X-axis velocity")
plt.plot(y_vel, label="Y-axis velocity")
plt.legend(loc="upper left")
plt.ylabel("Velocity in m/s")
plt.xlabel("# of Samples")
plt.ylim(-5, 5)  # Set the y-axis limits
plt.show()

x = [0]

for i in range(len(x_vel)-1):
    x.append(x[-1] + dt * x_vel[i])

## Integrations along Z axis:

z_vel = [0]
for i in range(len(z_calib)-1):
    z_vel.append(z_vel[-1] + dt * z_calib[i])

#plt.plot(z_vel)

z = [0]
plt.figure()
for i in range(len(z_vel)-1):
    z.append(z[-1] + dt * z_vel[i])
#plt.plot(z)



accel_raw = np.linalg.norm(np.array([x_calib, y_calib, z_calib]), axis=0)
accel = scipy.signal.savgol_filter(accel_raw, window_length=11, polyorder=4) ## Same as rolling average --> Savitzky-Golay smoothing
## change the window size as it seems fit. If you keep window size too high it will not capture the relevant peaks/steps

# Plot the original and smoothed data
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(accel_raw)
plt.title("Original Data")
plt.subplot(2, 1, 2)
plt.plot(accel)
plt.title("Smoothed Data")
plt.show()


## Step Detection: The instantaneous peaks in the accelerometer readings correspond to the steps. We use thresholding technique to decide the range of peak values for step detection
# Set a minimum threshold (e.g., 1.0) for peak detection
min_threshold = 0.1  ## Change the threshold (if needed) based on the peak accelerometer values that you observe in your plot above

# Calculate the upper threshold for peak detection as the maximum value in the data
upper_threshold = np.max(accel)

# Define the range for peak detection
my_range = (min_threshold, upper_threshold)

# print("range of Accel. values  for peak detection",my_range)
## Visualize the detected peaks in the accelerometer readings based on the selected range
plt.plot(accel)
peak_array, _ = signal.find_peaks(accel, height=my_range, distance=5)
plt.plot(peak_array, accel[peak_array], "x", color="r")
plt.show()

print("Accel values at high peaks-->", accel[peak_array])

print("Peak array indices are", peak_array)

# Extract  the timestamps corresponding to detected peaks
timestamp_for_peaks = df[1][peak_array]

# Create a new DataFrame with timestamp and peak values
peaks_df = pd.DataFrame({'Timestamp': timestamp_for_peaks, 'PeakValue': accel[peak_array]})
print("Peaks_df is", peaks_df)

# Set the orientation/direction of motion (walking direction).
# walking_direction is an angle in degrees with global frame x-axis. It can be from 0 degrees to 360 degrees.
# for e.g. if walking direction is 90 degrees, user is walking in the positive y-axis direction.
# Assuming you are moving along the +X-axis with minor deviations/drifts in Y, we set the orientation to 5 (ideally it should be 0 but to take into account the drifts we keep 5)
# Additionally, we assume that the walking direction will be the same throught the trajectory that you capture in this exercise.

walking_dir = np.deg2rad(5) ## deg to radians





# To compute the step length, we estimate it to be propertional to the height of the user.
height=1.95 # in meters
step_length= 0.415 * height # in meters

# Convert walking direction into a 2D unit vector representing motion in X, Y axis:
angle = np.array([np.cos(walking_dir), np.sin(walking_dir)])
