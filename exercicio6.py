numero = int(input("Digite quantos termos você deseja: "))
A = 0
B = 1
C = 1
fibonnaci = []

while C <= numero:
    fibonnaci.append(C)
    C = A + B
    A = B
    B = C
print(fibonnaci)