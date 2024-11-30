# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(0, 10, 100)  # 100 evenly spaced values from 0 to 10
y = np.sin(x)                # Sine wave values for the x range
###############################################################???????##########
# Create a plot
plt.figure(figsize=(8, 6))  # Set figure size
plt.plot(x, y, label='Sine Wave')  # Plot the sine wave
plt.title('Sine Wave Plot')        # Add a title
plt.xlabel('X-axis')               # Label the x-axis
plt.ylabel('Y-axis')               # Label the y-axis
plt.legend()                       # Add a legend
plt.grid(True)                     # Enable grid for better readability

# Save the plot to a file
output_filename = 'sine_wave_plot.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')  # Save as a PNG file with high resolution
print(f"Plot saved as {output_filename}")

# Show the plot (optional)
plt.show()
