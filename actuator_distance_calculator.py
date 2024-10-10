import numpy as np
import matplotlib.pyplot as plt

# parameters
E = 25.0 * 1e6  # Young's modulus in Pascals
nu = 0.45   # Poisson's ratio
n_L = 1     # Longitudinal wave number, constant in this case
C_f = 1     # Constant factor

# Displacement calculation function
def displacement(P, n_w, s, h, D_m):
    # Calculate spring constant
    K_ax = (E / (2 * (1 - nu**2))) * (np.pi * D_m * s**3 / h**3) * (n_L / n_w) * (1 / C_f)
    # Calculate effective area
    A_eff = np.pi * (D_m / 2) ** 2
    # Calculate displacement
    d = P * A_eff / K_ax
    
    return d * 1e3  # Return displacement in mm

# Pressure values in Pascals
pressures = np.arange(0, 201, 10) * 1e3  # Pressure from 0kPa to 200kPa with interval 10kPa

# Given parameter values
corrugation_num = 2   # number of chambers
corrugation_height = 7.5 * 1e-3  # Corrugation height in meters
wall_thickness = 1.6 * 1e-3  # Wall thickness in meters
mean_diameter = 16.3 * 1e-3  # Mean diameter in meters

# Loop over wall thicknesses and plot displacement for each one
analytical_displacements = displacement(pressures,
                             corrugation_num,  # Use first corrugation number
                             wall_thickness,
                             corrugation_height,  # Use first corrugation height
                             mean_diameter)  # Use first mean diameter


simulated_displacements = [
    0, 0.8168573738, 1.633714748, 2.450572121, 3.267429495, 4.084286869,
    4.901144243, 5.718001617, 6.53485899, 7.351716364, 8.168573738,
    8.985431112, 9.802288486, 10.61914586, 11.43600323, 12.25286061,
    13.06971798, 13.88657535, 14.70343273, 15.5202901, 16.33714748
]

experimental_pressures = [0, 20, 32, 42, 51, 61, 70, 80, 90, 100, 115, 120, 131, 142, 149, 162, 171, 180, 191, 200]
experimental_displacements = [0, 1, 1.9, 2.3, 2.7, 3.4, 3.8, 4.2, 4.4, 4.8, 5.5, 5.7, 6, 6.5, 6.8, 7.2, 7.5, 7.8, 8.3, 8.6]

# Plot setup
plt.figure(figsize=(8, 6))
plt.plot(pressures / 1e3, analytical_displacements, label='Analytical', linestyle='-', marker='o')
plt.plot(pressures / 1e3, simulated_displacements, label='Simulated', linestyle='-', marker='o')
plt.plot(experimental_pressures, experimental_displacements, label='Experimental', linestyle='-', marker='o')


# Plot labels and title
plt.xlabel('Pressure (kPa)', fontsize=12)
plt.ylabel('Displacement (mm)', fontsize=12)
plt.title('Displacement vs Pressure for Linear Actuator', fontsize=14)
plt.grid(True)
plt.legend()
plt.tight_layout()  # Ensure everything fits nicely
plt.show()
