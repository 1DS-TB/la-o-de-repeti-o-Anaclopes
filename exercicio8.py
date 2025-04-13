divisor = int(input("Insira o número: "))
n = 1
serie_harmonica = []
soma = 0
while n <= divisor:
    serie_harmonica.append(f"1/{n}")
    serie = 1/n
    n +=1
    soma += serie
print(serie_harmonica)
print(f"Soma da série harmônica é: {soma:.2f}")