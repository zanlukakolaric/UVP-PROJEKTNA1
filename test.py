import numpy as np
import matplotlib.pyplot as plt

# Create a range of x values
x = np.linspace(-2, 2, 400)

# Calculate the corresponding y values for the exponential function
y = np.exp(x)

# Create a figure with two subplots side by side
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Plot the exponential function on the first subplot
axs[0].plot(x, y, color='blue')
axs[0].set_title('Exponential Function')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')

# Plot the logarithmically scaled exponential function on the second subplot
axs[1].semilogy(x, y, color='green')
axs[1].set_title('Exponential Function (Log Scale)')
axs[1].set_xlabel('x')
axs[1].set_ylabel('y (Log Scale)')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
