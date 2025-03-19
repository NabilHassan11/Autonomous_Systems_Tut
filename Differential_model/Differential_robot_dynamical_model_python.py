import numpy as np
import matplotlib.pyplot as plt

# Robot parameters
r = 0.025    # Wheel radius [m]
L = 0.15     # Wheelbase [m]
m = 1.0      # Mass [kg]
J = 0.1      # Moment of inertia [kg·m²]

# Simulation parameters
dt = 0.1     # Time step [s]
total_time = 5.0  # Simulation duration [s]
steps = int(total_time / dt)

# Initial conditions
x = np.zeros(steps)
y = np.zeros(steps)
theta = np.zeros(steps)  # Orientation [rad]
v = np.zeros(steps)      # Linear velocity [m/s]
omega = np.zeros(steps)  # Angular velocity [rad/s]

# Torque inputs [N·m]
# Scenario 1: Straight acceleration (equal torques)
# Scenario 2: Rotational acceleration (unequal torques)

# Choose scenario (uncomment one)
# Scenario 1:
tau_r = np.full(steps, 0.1)  # Right wheel torque
tau_l = np.full(steps, 0.1)  # Left wheel torque

# Scenario 2:
# tau_r = np.full(steps, 0.15)  # Right wheel torque
# tau_l = np.full(steps, 0.05)  # Left wheel torque

# Simulation loop
for i in range(1, steps):
    # Calculate accelerations
    v_dot = (tau_r[i] + tau_l[i]) / (m * r)
    omega_dot = (tau_r[i] - tau_l[i]) * L / (2 * r * J)
    
    # Update velocities using Euler integration
    v[i] = v[i-1] + v_dot * dt
    omega[i] = omega[i-1] + omega_dot * dt
    
    # Update pose using velocities (kinematic model)
    x[i] = x[i-1] + v[i] * np.cos(theta[i-1]) * dt
    y[i] = y[i-1] + v[i] * np.sin(theta[i-1]) * dt
    theta[i] = theta[i-1] + omega[i] * dt

# Plotting
plt.figure(figsize=(14, 10))

# Position vs Time
plt.subplot(3, 2, 1)
plt.plot(np.arange(steps)*dt, x, label='X Position')
plt.plot(np.arange(steps)*dt, y, label='Y Position')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Position vs Time')
plt.legend()
plt.grid(True)

# Velocity vs Time
plt.subplot(3, 2, 2)
plt.plot(np.arange(steps)*dt, v, label='Linear Velocity')
plt.plot(np.arange(steps)*dt, np.degrees(omega), label='Angular Velocity (°/s)')
plt.xlabel('Time (s)')
plt.ylabel('Velocity')
plt.title('Velocity vs Time')
plt.legend()
plt.grid(True)

# Orientation vs Time
plt.subplot(3, 2, 3)
plt.plot(np.arange(steps)*dt, np.degrees(theta))
plt.xlabel('Time (s)')
plt.ylabel('Orientation (°)')
plt.title('Heading Angle vs Time')
plt.grid(True)

# Torque Inputs
plt.subplot(3, 2, 4)
plt.plot(np.arange(steps)*dt, tau_r, label='Right Torque')
plt.plot(np.arange(steps)*dt, tau_l, label='Left Torque')
plt.xlabel('Time (s)')
plt.ylabel('Torque (N·m)')
plt.title('Torque Inputs')
plt.legend()
plt.grid(True)

# Trajectory Plot
plt.subplot(3, 1, 3)
plt.plot(x, y)
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.title('Robot Trajectory')
plt.axis('equal')
plt.grid(True)

plt.tight_layout()
plt.show()