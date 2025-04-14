num = int(input("Insira um número inteiro positivo: "))
som = 0

if num < 0:
    print("INVALIDO")
else:
    num +=1
    while num > 1:
        num -= 1
        som+= num
print(som)
