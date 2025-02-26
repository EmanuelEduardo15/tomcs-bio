import numpy as np

def tomcs_velocity(R, k=0.47, n=1.02):
    """
    Calcula a velocidade celular usando o modelo TOMCS.
    
    Parâmetros:
    R (float ou array): Raio de curvatura (µm).
    k (float): Constante de proporcionalidade.
    n (float): Expoente de ajuste.
    
    Retorna:
    v (float ou array): Velocidade (µm/min).
    """
    return k * R**n

# Exemplo de uso
R = np.array([0.5, 1.0, 1.5, 2.0])
v = tomcs_velocity(R)
print("Velocidades previstas:", v)
