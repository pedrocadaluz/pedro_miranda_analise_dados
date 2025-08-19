import matplotlib.pyplot as plt

# Dados dos ciclos
anos = ['1996', '1997']
ciclo_operacional = [109, 181]
ciclo_financeiro = [62, 112]

# Criação do gráfico
plt.figure(figsize=(8, 5))
plt.plot(anos, ciclo_operacional, marker='o', label='Ciclo Operacional')
plt.plot(anos, ciclo_financeiro, marker='s', label='Ciclo Financeiro')
plt.title('Evolução dos Ciclos (1996-1997)')
plt.xlabel('Ano')
plt.ylabel('Dias')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()  