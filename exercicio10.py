num1 = int(input("Digite o primeiro intervalo: "))
num2 = int(input("Digite o segundo intervalo: "))

if num1 <= 0 or num2 <= 0:
    print("Inválido")
else:
    for i in range (num1, num2):
        i2 = str(i**2)
        tamanho = len(i2)

        if i < 10:
            if i == 9 or i == 1:
                print(f"O número {i} é um número Kaprekar.")

        elif tamanho % 2 != 0 or i == 9 or i == 1:
            metade = tamanho // 2
            lDireita = tamanho - metade
            lEsquerda = tamanho - lDireita

            direita = int(i2[-lDireita:])
            esquerda = int(i2[:lEsquerda])

            if direita + esquerda == i:
                print(f"O número {i} é um número Kaprekar.")

        else:

            metade = tamanho // 2
            lDireita = tamanho - metade
            lEsquerda = tamanho - lDireita

            direita = int(i2[-lDireita:])
            esquerda = int(i2[:lEsquerda])

            if direita + esquerda == i:
                print(f"O número {i} é um número Kaprekar.")

        metade = 0
        lDireita = 0
        lEsquerda = 0
