numero = int(input("Digite quantos termos você deseja: "))
A = 0
B = 1
C = 1
fibonnaci = []

if numero < 1:
    print("INVALIDO")
else:
    while C <= numero:
        fibonnaci.append(A)
        C = A + B
        A = B
        B = C
fibonnaci.append(A)
print(fibonnaci)
