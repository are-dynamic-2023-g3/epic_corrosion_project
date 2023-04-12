import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import solve_ivp

def rusting(y, t, k1, k2):
    iron, fe2, oxygen, water = y

    # Anodic reaction: Fe --> Fe2+ + 2e
    r_anodic = k1 * iron * oxygen**(1/2) * (1 - fe2/iron)

    # Cathodic reaction: O2 + 4e + 2H2O --> 4OH-
    r_cathodic = k2 * oxygen * water**(1/2) * (1 - fe2/iron)

    # Differential equations
    d_iron = -r_anodic
    d_fe2 = r_anodic - r_cathodic
    d_oxygen = -r_cathodic
    d_water = r_cathodic

    return [d_iron, d_fe2, d_oxygen, d_water]
  
# Initial conditions
y0 = [1, 0, 1, 0.5]

# Time points to evaluate
t = np.linspace(0, 10, 1000)

# Parameters
k1 = 0.08
k2 = 0.06

sol = odeint(rusting, y0, t, args=(k1, k2))

# Plot the results
plt.plot(t, sol[:, 0], label='Iron')
plt.plot(t, sol[:, 1], label='Fe2+')
plt.plot(t, sol[:, 2], label='Oxygen')
plt.plot(t, sol[:, 3], label='Water')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.show()

#Butler Volmer 
# Constants
R = 8.314 # J/mol-K
F = 96485 # C/mol

# Initial conditions
oxygen_initial = 0.7 # mol/m^3
rust_initial = 0.3 # mol/m^3
water = 100 # mol/m^3
T = 298 # K

# Equilibrium potentials
E0_anodic = -0.44 # V
E0_cathodic = -0.14 # V
i0_anodic = 5.87e-6 # A/m^2
i0_cathodic = 1.27e-6 # A/m^2
alpha_anodic = 0.5
alpha_cathodic = 0.5
fe2 = 10**(-1.82) # mol/m^3, concentration of Fe2+ ions at equilibrium
E_eq_anodic = E0_anodic - R*T/(4*F) * np.log(1/fe2)
E_eq_cathodic = E0_cathodic + R*T/(4*F) * np.log(oxygen_initial/water**(1/2))

# Reaction rates
def butler_volmer_anodic(i0, alpha, E, E_eq):
    i = i0 * (np.exp(alpha * F * (E - E_eq) / (R * T)) - np.exp(-(1 - alpha) * F * (E - E_eq) / (R * T)))
    return i

def butler_volmer_cathodic(i0, alpha, E, E_eq):
    i = i0 * (np.exp(-(1 - alpha) * F * (E - E_eq) / (R * T)) - np.exp(alpha * F * (E - E_eq) / (R * T)))
    return i
  
# Rusting function
def rustingbv(t, y, water):
    oxygen, rust = y
    E = R*T/(2*F) * np.log(np.maximum(oxygen, 1e-12)/water**(1/2))
    i_anodic = butler_volmer_anodic(i0_anodic, alpha_anodic, E, E_eq_anodic)
    i_cathodic = butler_volmer_cathodic(i0_cathodic, alpha_cathodic, E, E_eq_cathodic)
    rust_rate = i_anodic - i_cathodic
    d_oxygen = -rust_rate
    d_rust = rust_rate
    return [d_oxygen, d_rust]
  
# Simulation
t_final = 100 # seconds
dt = 0.1 # seconds
t_span = [0, t_final]
t_eval = np.arange(0, t_final, dt)
y0 = [oxygen_initial, rust_initial]

sol = solve_ivp(rustingbv, t_span, y0, t_eval=t_eval, args=(water,))

# Plot simulation results
plt.plot(sol.t, sol.y[0], label='Oxygen')
plt.plot(sol.t, sol.y[1], label='Rust')
plt.xlabel('Time (s)')
plt.ylabel('Concentration (mol/m^3)')
plt.legend()
plt.show()

# Anodic and cathodic reactions over time
fig, ax2 = plt.subplots()
E = np.linspace(E0_anodic, E0_cathodic, 1000)
i_anodic = butler_volmer_anodic(i0_anodic, alpha_anodic, E, E_eq_cathodic)
i_cathodic = butler_volmer_cathodic(i0_cathodic, alpha_cathodic, E, E_eq_anodic)
ax2.plot(E, i_anodic, 'r-', label='Anodic')
ax2.plot(E, i_cathodic, 'b-', label='Cathodic')
ax2.set_xlabel('Potential (V)')
ax2.set_ylabel('Current density (A/m^2)')
ax2.legend()

  
