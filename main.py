import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import solve_ivp

def rusting(y, t, k1, k2):
    iron, fe2, oxygen, water = y

    # réaction anodique: Fe --> Fe2+ + 2e
    r_anodic = k1 * iron * oxygen**(1/2) * (1 - fe2/iron)

    # réaction cathodique: O2 + 4e + 2H2O --> 4OH-
    r_cathodic = k2 * oxygen * water**(1/2) * (1 - fe2/iron)

    # Les équations différentielles
    d_iron = -r_anodic
    d_fe2 = r_anodic - r_cathodic
    d_oxygen = -r_cathodic
    d_water = -r_cathodic

    return [d_iron, d_fe2, d_oxygen, d_water]Points de temps à évaluer
  
# Les conditions initiales
y0 = [1, 0, 1, 0.5] #ici, on définit les concentrations initiales

# Points de temps à évaluer
t = np.linspace(0, 10, 1000)

# les constantes de réaction
k1 = 0.08
k2 = 0.06

sol = odeint(rusting, y0, t, args=(k1, k2))#On résout les équations différentielles avec la fonction "odeint" de Scipy

# afficher les résultats à l'aide de matplotlib
plt.plot(t, sol[:, 0], label='Iron')
plt.plot(t, sol[:, 1], label='Fe2+')
plt.plot(t, sol[:, 2], label='Oxygen')
plt.plot(t, sol[:, 3], label='Water')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.show()

#Butler Volmer 
# Constantes
R = 8.314 # J/mol-K # constante des gaz parfaits 
F = 96485 # C/mol # constante de Faraday 

# Les conditions initiales
oxygen_initial = 0.7 # mol/m^3
rust_initial = 0.3 # mol/m^3
water = 100 # mol/m^3
T = 298 # K #temperature

#Potentiels d'équilibre
E0_anodic = -0.44 # V #potentiel d'équilibre anodique
E0_cathodic = -0.14 # V # potentiel d'équilibre cathodique 
i0_anodic = 5.87e-6 # A/m^2 #densité de courant cinétique d'échange anodique
i0_cathodic = 1.27e-6 # A/m^2 densité de courant cinétique d'échange cathodique
alpha_anodic = 0.5 #coefficient de transfert de charge pour l'échange anodique
alpha_cathodic = 0.5 #coefficient de transfert de charge pour l'échange cathodique
fe2 = 10**(-1.82) # mol/m^3 #concentration d'ions Fe2+ à l'équilibre 
E_eq_anodic = E0_anodic - R*T/(4*F) * np.log(1/fe2) # potentiel d'équilibre anodique ajusté en fonction de la concentration d'ions Fe2+ 
E_eq_cathodic = E0_cathodic + R*T/(4*F) * np.log(oxygen_initial/water**(1/2)) #potentiel d'équilibre  ajusté cathodique en fonction de la conentration initiale d'oxygène et d'eau 

# Réactions de Butler-Volmer

def butler_volmer_anodic(i0, alpha, E, E_eq):
    i = i0 * (np.exp(alpha * F * (E - E_eq) / (R * T)) - np.exp(-(1 - alpha) * F * (E - E_eq) / (R * T)))
    return i

def butler_volmer_cathodic(i0, alpha, E, E_eq):
    i = i0 * (np.exp(-(1 - alpha) * F * (E - E_eq) / (R * T)) - np.exp(alpha * F * (E - E_eq) / (R * T)))
    return i

# Fonction de rouille
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
t_final = 100 # secondes # temps final de simulation
dt = 0.1 # secondes #intervalle de temps 
t_span = [0, t_final] #plage de temps à simuler
t_eval = np.arange(0, t_final, dt)# points de temps à évaluer
y0 = [oxygen_initial, rust_initial] #conditions initiales pour l'oxygène et la rouille

sol = solve_ivp(rustingbv, t_span, y0, t_eval=t_eval, args=(water,)) # solution de l'équation différentielle pour l'évolution de la concentration d'oxygène et de rouille au fil du temps

# Affichage des résultats de la simulation
plt.plot(sol.t, sol.y[0], label='Oxygen')
plt.plot(sol.t, sol.y[1], label='Rust')
plt.xlabel('Time (s)')
plt.ylabel('Concentration (mol/m^3)')
plt.legend()
plt.show()

#Réactions anodiques et cathodiques au fil du temps
fig, ax2 = plt.subplots()
E = np.linspace(E0_anodic, E0_cathodic, 1000)
i_anodic = butler_volmer_anodic(i0_anodic, alpha_anodic, E, E_eq_cathodic)
i_cathodic = butler_volmer_cathodic(i0_cathodic, alpha_cathodic, E, E_eq_anodic)
ax2.plot(E, i_anodic, 'r-', label='Anodic')
ax2.plot(E, i_cathodic, 'b-', label='Cathodic')
ax2.set_xlabel('Potential (V)')
ax2.set_ylabel('Current density (A/m^2)')
ax2.legend()

  
