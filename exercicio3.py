number = int(input("Insira um número: "))

if number < 0:
    print("INVALIDO")
else:
    for numb in range(1,11):
        mult= number*numb
        print(f"{number}x{numb}:", mult)
