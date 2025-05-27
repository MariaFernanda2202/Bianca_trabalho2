import numpy as np

# ATIVIDADE 1
# Equivalente ao: matriz_1 <- matrix(1:10)
matriz_1 = np.array(range(1, 11)).reshape(-1, 1)
print("matriz_1:")
print(matriz_1)

# ATIVIDADE 2
# Equivalente ao: matriz_2 <- matrix(data = 1:10, nrow = 5, ncol = 2, byrow = FALSE)
# Por padrão, NumPy preenche por linha, então para preencher por coluna usamos 'order='F''
matriz_2 = np.array(range(1, 11)).reshape(5, 2, order='F')
print("\nmatriz_2:")
print(matriz_2)


##lembrar de dar (pip instal numpy) para funcionar

# ATIVIDADE 3

a11 = int(input('Qual seria o a11? '))
a12 = int(input('Qual seria o a12? '))
a21 = int(input('Qual seria o a21? '))
a22 = int(input('Qual seria o a22? '))
MatrizA = np.array([[a11, a12],[a21, a22]])
Transposta = MatrizA.T
resultado = np.dot(MatrizA, Transposta)
determinante = np.linalg.det(resultado)
print("Determinante do A x At:")
print(round(determinante))