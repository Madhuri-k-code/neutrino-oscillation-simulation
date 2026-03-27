import numpy as np
import matplotlib.pyplot as plt

# Parameters
theta = np.pi / 4
dm2 = 2.4e-3
E = 1.0

# Decoherence parameter
gamma = 0.001

# Distance range
L = np.linspace(0, 1000, 500)

# Standard oscillation
P_standard = (np.sin(2*theta)**2) * (np.sin(1.27 * dm2 * L / E)**2)

# Oscillation with decoherence
P_decoherence = (np.sin(2*theta)**2) * np.exp(-gamma * L) * (np.sin(1.27 * dm2 * L / E)**2)

# Plot
plt.plot(L, P_standard, label="Standard Oscillation")
plt.plot(L, P_decoherence, label="With Decoherence")

plt.xlabel("Distance (km)")
plt.ylabel("Probability")
plt.title("Neutrino Oscillation with Decoherence")
plt.legend()
plt.grid()

plt.show()
