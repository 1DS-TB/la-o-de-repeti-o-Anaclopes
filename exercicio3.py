numero = int(input("Insira um número: "))

if numero < 0:
    print("INVALIDO")
else:
    for numb in range(1,11):
        mult = numero * numb
        print(f"{numero} x {numb} = {mult}")
