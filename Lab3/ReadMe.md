## Post-Lab Assignment-1

We used the joystick and IMU, we also measured how big the gait of Jaden and Siddharth so we could see how much distance we were moving per step. We implemented the joystick to enable directionality in our movement measurements. One of our initial plans was to use the joystick to activate and deactivate accelerometers as we saw fit, but after a lot of trial and error, our measurements seemed accurate, but our actual analysis would keep failing in estimating position. 
We weren't sure why, so we ended up using the joystick method since it was the most accurate by far and gave us repeatable results. You can see in the graph that the position graph is accurate, and we return to almost our initial point. We added a factor of randomness to account for the fact that the human gait is not always a consistent value, so we varied our values between a range that we measured and found that we varied our gait in between. 


## Post-Lab Assignment-2





## Post-Lab Assignment-3

We used the SenseHat setPixel() to update the right-top corner pixel to a color based on the current read RSSI relative to the max RSSI. The max is initialized to a reasonable and desirable RSSI value that could indicate the presence of a device. The color is red when the read RSSI has a difference greater than 25 dBM compared to the Max. The other color ranges are as follows Blue [-25: -15] Teal [-15: -10] and Green is for when a new max is found. 

Therefore, the algorithm helps find a lower transmitting pi by guiding our walk when we detect a better RSSI value.


Link to All Videos for PostLab: https://drive.google.com/file/d/1pt2dIN3qRW86IFgx9xiUMY1rTCrVCVPD/view?usp=sharing
