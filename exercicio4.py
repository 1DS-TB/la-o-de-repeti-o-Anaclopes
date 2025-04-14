numero = int(input("Insira o número que deseja calcular: "))
i = 1
nm = 1

if numero > 0:
    while i <= numero:
        nm *= i
        i+=1
elif numero < 0:
    print("INVALIDO")
    
elif numero == 0:
    nm == 1
print(nm)
