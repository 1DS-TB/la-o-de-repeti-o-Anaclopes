num = int(input("Digite um número: "))
divisor = 0

for i in range(1, num +1):
    if num % i == 0:
        divisor +=1

if divisor == 2:
    print(f"{num} é primo")
else:
    print(f"{num} não é primo")