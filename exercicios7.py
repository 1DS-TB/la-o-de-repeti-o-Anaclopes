Numero = int(input("Insira um número: "))

if Numero <1:
    print("Inválido")
else:
    for linha in range(1, Numero+1): #responsável por percorrer cada linha
        for cada in range (linha): # para cada for, uma linha
            print("x ", end=" ")
        print(" ") # usei para pular as linhas
