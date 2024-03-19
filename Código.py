import numpy as np
import matplotlib.pyplot as plt

def pontos_dentro_circunferencia_e_figura(n):
    # Gerar n pontos (x, y), com x e y entre -1 e 1
    pontos = np.random.uniform(-1, 1, (n, 2))
    
    # Calcular a distância ao quadrado do centro (0, 0)
    distancias_ao_quadrado = pontos[:, 0]**2 + pontos[:, 1]**2
    dentro = distancias_ao_quadrado <= 1

    # Calcular a proporção de pontos dentro da circunferência
    proporcao_dentro = np.sum(dentro) / n
    
    # Estimar o valor de pi
    pi_estimado = 4 * proporcao_dentro
    
    # Calcular a diferença entre a estimativa e o valor real de pi
    diferenca_para_pi = 100*np.abs(pi_estimado - np.pi)/np.pi

    passou = 0
    n_passou = 0

    print(f"Estimativa de pi: {pi_estimado}")
    print(f"Diferença para o valor real de pi: {diferenca_para_pi}%")
    if (diferenca_para_pi > 0.05):
        print(f"Passou do permitido")
    else:
        print(f"Erro dentro do permitido")  
n = 26666667  # n obtido pela desigualdade de Chebyshev
m = 10000
conta  = 0
while(conta < m):
    pontos_dentro_circunferencia_e_figura(n)
    conta = conta+1
    