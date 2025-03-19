import numpy as np
import matplotlib.pyplot as plt

# Unicycle Kinematic Model
def unicycle_model(v, omega, dt, steps):
    # Initialize states: [x, y, theta]
    state = np.array([0.0, 0.0, 0.0])
    trajectory = [state.copy()]

    for _ in range(steps):
        x, y, theta = state
        # Update state
        x += v * np.cos(theta) * dt
        y += v * np.sin(theta) * dt
        theta += omega * dt
        state = np.array([x, y, theta])
        trajectory.append(state.copy())

    return np.array(trajectory)

# Simulation parameters
v = 1.0          # Linear velocity (m/s)
omega = 0.5      # Angular velocity (rad/s)
dt = 0.1         # Time step (s)
steps = 100      # Number of steps

# Run simulation
trajectory = unicycle_model(v, omega, dt, steps)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(trajectory[:, 0], trajectory[:, 1], label='Trajectory', color='royalblue')
plt.quiver(trajectory[:, 0], trajectory[:, 1], np.cos(trajectory[:, 2]), np.sin(trajectory[:, 2]), 
           scale=20, color='red', label='Heading')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.title('Unicycle Kinematic Model')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
