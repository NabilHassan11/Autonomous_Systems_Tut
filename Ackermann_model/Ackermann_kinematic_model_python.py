import numpy as np
import matplotlib.pyplot as plt

# Robot parameters
L = 0.25  # Wheelbase [m]
MAX_STEER = np.radians(30)  # Maximum steering angle (30 degrees)

# Simulation parameters
dt = 0.01  # Time step [s]
total_time = 10.0  # Simulation duration [s]
steps = int(total_time / dt)

# Initial conditions
x = np.zeros(steps)
y = np.zeros(steps)
theta = np.zeros(steps)  # Heading angle [rad]
phi = np.zeros(steps)    # Steering angle [rad]

# Inputs (2 scenarios - uncomment desired one)
# Scenario 1: Straight line
# v = np.full(steps, 0.5)  # Constant velocity [m/s]
# steering_rate = np.zeros(steps)

# Scenario 2: Constant steering
v = np.full(steps, 0.5)  # Constant velocity [m/s]
steering_rate = np.full(steps, 0.1)  # Steering rate [rad/s]

# Simulation loop with angle wrapping
for i in range(1, steps):
    # Apply steering constraints
    phi[i] = np.clip(phi[i-1] + steering_rate[i] * dt, -MAX_STEER, MAX_STEER)
    
    # Calculate derivatives
    x_dot = v[i] * np.cos(theta[i-1])
    y_dot = v[i] * np.sin(theta[i-1])
    theta_dot = (v[i] / L) * np.tan(phi[i])
    
    # Update states
    x[i] = x[i-1] + x_dot * dt
    y[i] = y[i-1] + y_dot * dt
    theta[i] = (theta[i-1] + theta_dot * dt) % (2 * np.pi)  # Wrap to 0-2π

# Plotting
plt.figure(figsize=(14, 10))

# Position plots
plt.subplot(3, 2, 1)
plt.plot(np.arange(steps)*dt, x, label='X Position')
plt.plot(np.arange(steps)*dt, y, label='Y Position')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Position vs Time')
plt.legend()
plt.grid(True)

# Heading angle
plt.subplot(3, 2, 2)
plt.plot(np.arange(steps)*dt, np.degrees(theta) % 360)
plt.xlabel('Time (s)')
plt.ylabel('Heading (°)')
plt.title('Vehicle Orientation')
plt.ylim(0, 360)
plt.grid(True)

# Steering angle
plt.subplot(3, 2, 3)
plt.plot(np.arange(steps)*dt, np.degrees(phi))
plt.xlabel('Time (s)')
plt.ylabel('Steering Angle (°)')
plt.title('Front Wheel Steering')
plt.grid(True)

# Velocity input
plt.subplot(3, 2, 4)
plt.plot(np.arange(steps)*dt, v)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Driving Velocity')
plt.grid(True)

# Trajectory plot
plt.subplot(3, 1, 3)
plt.plot(x, y)
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.title('Vehicle Trajectory')
plt.axis('equal')
plt.grid(True)

plt.tight_layout()
plt.show()