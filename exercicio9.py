soma = 0

for numero in range(1,10001):

    for i in range(1,numero):
        if numero % i == 0:
            soma += i
    if soma == numero:
        print(f"O número {numero} é perfeito")

    soma -= soma
