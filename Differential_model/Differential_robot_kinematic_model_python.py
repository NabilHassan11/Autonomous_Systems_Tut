import numpy as np
import matplotlib.pyplot as plt

# Robot parameters
r = 0.025  # Wheel radius (2.5 cm converted to meters)
L = 0.15   # Wheelbase (15 cm converted to meters)

# Simulation parameters
dt = 0.1   # Time step (seconds)
total_time = 10.0  # Total simulation time
steps = int(total_time / dt)

# Initial conditions
x = np.zeros(steps)
y = np.zeros(steps)
theta = np.zeros(steps)  # Orientation in radians

# Set initial position and orientation
x[0] = 5.0
y[0] = 5.0
theta[0] = np.pi  # 180 degrees in radians


# Wheel angular velocities (rad/s)
# Scenario 1: Straight line (both wheels same speed)
# Scenario 2: Circular motion (different wheel speeds)

# Choose scenario (uncomment one)
# Scenario 1:
w_r = np.full(steps,3.0)  # Right wheel speed (rad/s)
w_l = np.full(steps, 6.0)  # Left wheel speed (rad/s)

# Scenario 2:
# w_r = np.full(steps, 10.0)   # Right wheel speed (rad/s)
# w_l = np.full(steps, 5.0)    # Left wheel speed (rad/s)

# Simulation loop
for i in range(1, steps):
    # Calculate wheel linear velocities
    v_r = r * w_r[i]
    v_l = r * w_l[i]
    
    # Calculate robot velocity components
    v = (v_r + v_l) / 2.0
    omega = (v_r - v_l) / L
    
    # Update pose using Euler integration
    x[i] = x[i-1] + v * np.cos(theta[i-1]) * dt
    y[i] = y[i-1] + v * np.sin(theta[i-1]) * dt
    theta[i] = theta[i-1] + omega * dt

# Plotting
plt.figure(figsize=(12, 8))

# Position vs Time
plt.subplot(2, 2, 1)
plt.plot(np.arange(steps)*dt, x, label='X Position')
plt.plot(np.arange(steps)*dt, y, label='Y Position')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Position vs Time')
plt.legend()
plt.grid(True)

# Orientation vs Time
plt.subplot(2, 2, 2)
plt.plot(np.arange(steps)*dt, np.degrees(theta), label='Orientation')
plt.xlabel('Time (s)')
plt.ylabel('Angle (degrees)')
plt.title('Orientation vs Time')
plt.grid(True)

# Trajectory Plot
plt.subplot(2, 2, (3,4))
plt.plot(x, y)
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.title('Robot Trajectory')
plt.axis('equal')
plt.grid(True)

plt.tight_layout()
plt.show()