import numpy as np
import matplotlib.pyplot as plt

# Generate some random data
x = np.random.rand(10)
y = np.random.rand(10)

# Plot the data
plt.plot(x, y)

# Add labels and title
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Random data')

# Show the plot
plt.show()