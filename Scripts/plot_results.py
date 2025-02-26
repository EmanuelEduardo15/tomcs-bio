import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Carregar dados
data = pd.read_csv('../data/migration_velocities.csv')
R = data['Radius (µm)']
v_exp = data['Velocity (µm/min)']
err = data['Error']

# Modelo TOMCS
def tomcs_velocity(R, k=0.47, n=1.02):
    return k * R**n

R_fit = np.linspace(0.4, 2.1, 100)
v_fit = tomcs_velocity(R_fit)

# Plot
plt.figure(figsize=(6, 4), dpi=300)
plt.errorbar(R, v_exp, yerr=err, fmt='ko', label='Dados Experimentais')
plt.plot(R_fit, v_fit, 'r-', label='Ajuste TOMCS')
plt.xlabel('Raio de Curvatura (µm)', fontsize=12)
plt.ylabel('Velocidade (µm/min)', fontsize=12)
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.savefig('../figures/metastasis_curves.png', bbox_inches='tight')
plt.show()
