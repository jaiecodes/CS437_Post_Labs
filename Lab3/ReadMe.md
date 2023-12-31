## LINK TO GITHUB TO SEE README AND FULL CODE(RECOMMENDED VIEW):
https://github.com/jaiecodes/CS437_Post_Labs/tree/main/Lab3
pdf seems to look strange

## Lab 3 Checkpoint 2

We filtered the writing of x and y acceleration based on the MAC address of the transmitting Pi and the packet type. We take the RSSI value written into the CVS file as a data point to create a scatter plot using the ranges to determine the color of the dot in the scatter plot. You can see the scale is flawed since we were learning to edit the values when we took this but the yellow colors indicate when it is a higher RSSI aka when the signal strength is stronger, which makes sense since in this case we were walking toward the transmitting pi.

![71825687939__0DCEC21C-D66D-426B-856A-031078B04E9D jpeg](https://github.com/jaiecodes/CS437_Post_Labs/assets/72780632/c7582e4c-32ee-42a7-88c7-daf70fa13266)


## ALL POST LAB PLOTS SHOWN IN DEMO VIDEOS

## Post-Lab Assignment-1

We used the joystick and IMU, we also measured the gait of Jaden and Siddharth so we could see how much distance we were moving per step. We used the IMU in order to measure acceleration in each direction. For our final distance calculation, we used step detection with the code provided in the Lab document. We have our code detect the peaks and count the number of steps we have. We also double-check this value since we use the joystick to establish directionality. Every time we pressed in a direction we wrote an integer and parsed this in our analysis to ensure that we were performing the right operation to our final distance.

Part 1 Unfiltered is our collection code that collects data as we move and Part1Step is the analysis code that draws the XY position Graph
Link To Video: https://drive.google.com/file/d/16v-O4gIqP5yC7BiXP-hjdOC-9dGxQEk5/view?usp=sharing
## Post-Lab Assignment-2

Before we would sometimes get higher RSSI values when just walking during our path, so we decided to implement a moving window average so that the RSSI values are smooth based on the surrounding values read within a time frame. This helps avoid interpreting values as an incorrect max RSSI value when analyzing. The code for the rolling window analysis using Pandas is Contained within Analysis.py

Link to Video: https://drive.google.com/file/d/1pt2dIN3qRW86IFgx9xiUMY1rTCrVCVPD/view?usp=drive_link

## Post-Lab Assignment-3

We used the SenseHat setPixel() to update the right-top corner pixel to a color based on the current read RSSI relative to the max RSSI. The max is initialized to a reasonable and desirable RSSI value that could indicate the presence of a device. The color is red when the read RSSI has a difference greater than 25 dBM compared to the Max. The other color ranges are as follows Blue [-25: -15] Teal [-15: -10] and Green is for when a new max is found. 

Therefore, the algorithm helps find a lower transmitting pi by guiding our walk when we detect a better RSSI value.

Link to Video: https://drive.google.com/file/d/1JLChsKw4Nk7-LSCiBSa1wfpJ0l1-Y09v/view?usp=drive_link

Link to All Videos for PostLab: https://drive.google.com/file/d/1pt2dIN3qRW86IFgx9xiUMY1rTCrVCVPD/view?usp=sharing
