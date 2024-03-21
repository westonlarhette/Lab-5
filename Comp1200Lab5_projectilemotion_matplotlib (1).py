#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:56:16 2024

@author: westonlarhette
"""

## Projectile Motion Problem using Matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Define constants
v0 = 30 # Initial velocity (m/s)
theta = 45 # Launch angle (degrees)
g = 9.81 # Acceleration due to gravity (m/s^2)

# Convert angle to radians
theta_rad = np.radians(theta)

# Define initial velocity in y-direction
v0_y = v0 * np.sin(theta_rad)
time = 2 * v0_y / g

# Time Intervals (s)
time_intervals = np.arange(0,time+0.5,0.5)
x = np.empty(len(time_intervals))
y = np.empty(len(time_intervals))

for i in range(len(time_intervals)):
    x_t = v0 * np.cos(theta_rad) * time_intervals[i]
    y_t = v0 * np.sin(theta_rad) * time_intervals[i] - 0.5 * g * time_intervals[i]**2
    x[i] = x_t
    y[i] = y_t
    
plt.subplot(1,3,1) # Create the first subplot
plt.plot(x,y) # Plot y vs. x
plt.title('Subplot 1: y(t) vs x(t)')
plt.xlabel('x(t) in meters')
plt.ylabel('y(t) in meters')

plt.subplot(1,3,2)
plt.plot(time_intervals,x) # Plot x vs. t
plt.title('Subplot 1: x(t) vs Time')
plt.xlabel('Time (s)')
plt.ylabel('x(t) in meters')

plt.subplot(1,3,3)
plt.plot(time_intervals,y) # Plot y vs. t
plt.title('Subplot 1: y(t) vs Time')
plt.xlabel('Time (s)')
plt.ylabel('y(t) in meters')

plt.tight_layout()
plt.show()

