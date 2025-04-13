def kaprekar(n):
    quadrado = n ** 2

    quadrado_str = str(quadrado)

    tamanho_d = len(str(n))

    parte_d = int(quadrado_str[-tamanho_d:]) if len(quadrado_str) > tamanho_d else 0

    parte_e = int(quadrado_str[:-tamanho_d]) if len(quadrado_str) > tamanho_d else 0

    soma = parte_d + parte_e

    return soma == n

inicial = int(input("Informe o primeiro número do intervalo: "))
final = int(input("Informe o último número do intervalo: "))

print(f"Os números de kaprekar entre o intevalo escolhido são: ")
for numero in range (inicial, final +1):
    if kaprekar(numero):
        print(numero)