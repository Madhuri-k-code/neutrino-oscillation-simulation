import numpy as np
import matplotlib.pyplot as plt

# Parameters
theta = np.pi / 4
dm2 = 2.4e-3
E = 1.0

# Distance range
L = np.linspace(0, 1000, 500)

# Oscillation probability
P = (np.sin(2*theta)**2) * (np.sin(1.27 * dm2 * L / E)**2)

# Plot
plt.plot(L, P)
plt.xlabel("Distance (km)")
plt.ylabel("Probability")
plt.title("Neutrino Oscillation Simulation")
plt.grid()

plt.show()
