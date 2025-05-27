import numpy as np

# atividade 1
# Equivalente ao: matriz_1 <- matrix(1:10)
matriz_1 = np.array(range(1, 11)).reshape(-1, 1)
print("matriz_1:")
print(matriz_1)


# atividade 2
# Equivalente ao: matriz_2 <- matrix(data = 1:10, nrow = 5, ncol = 2, byrow = FALSE)
# Por padrão, NumPy preenche por linha, então para preencher por coluna usamos 'order='F''
matriz_2 = np.array(range(1, 11)).reshape(5, 2, order='F')
print("\nmatriz_2:")
print(matriz_2)


# ativiade 3
# equivale matriz_3 <- matrix(data = c(0,1,2,3,4,5,6,7,8,9) , nrow = 5, ncol = 2, byrow = FALSE, dimnames = NULL) 
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

#atividade 4
#equivale matriz_4 <- matrix(data = c(0,1,2,3) , nrow = 2, ncol = 2, byrow = FALSE,dimnames = list(c("linha1","linha2"),c("coluna1","coluna2")))
a = float(input("Digite o numero de a11 (posição [0][0]): "))
b = float(input("Digite o numero de b12 (posição [0][1]): "))
c = float(input("Digite o numero de c21 (posição [1][0]): "))
d = float(input("Digite o numero de d22 (posição [1][1]): "))

matriz = np.array([[a, b],
                   [c, d]])

print("\nMatriz digitada:")
for linha in matriz:
    print(f"[ {linha[0]:.2f}  {linha[1]:.2f} ]")

determinante = np.linalg.det(matriz)
print("\nDeterminante:", f"{determinante:.2f}")

if determinante != 0:
    inversa = np.linalg.inv(matriz)
    print("\nMatriz Inversa:")
    for linha in inversa:

        linha_formatada = []
        for valor in linha:
            linha_formatada.append(f"{valor * determinante:.2f}")
        print(linha_formatada)
else:
    print("A matriz não é inversivel")

#atividade 5
#CRIANDO MATRIZES A PARTIR DE VETORES COM rbind() e cbind()
#rbind(): empilha vetores um embaixo do outro (linhas)
#cbind(): cola vetores lado a lado (colunas)




#atividade 6
#TRANSFORMANDO UM VETOR EM MATRIZ usando as.matrix
#equivale a matriz_7 <- as.matrix(vetor_1)
vetor = [1,3,5,7,9]
matriz = [[x] for x in vetor]
for linha in matriz:
    print(linha)

#atividade 7
#ALTERAR ELEMENTO DA MATRIZ: nomematriz[linha,coluna]<-valor que será alterado no elemento linha,coluna
#equivale a matriz_6[1,2]<-100 