def perfeito(n):
    soma = 0
    for val in range(1, n):
        if n % val == 0:
            soma += val

    if soma == n:
        return True
    else:
        return False

def exibe():
    n = int(input('Exibir perfeitos até o número: '))
    numeros_perfeitos = []

    for val in range(1, n + 1):
        if (perfeito(val)):
            numeros_perfeitos.append((val))
    print(f"Os números perfeitos entre 1 e 1000 são: {numeros_perfeitos}")

while True:
    exibe()