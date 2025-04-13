import random

def_persona = 0
def_cpu = 0
hp = 0
acao_cpu = []
atq_persona = random.randint(1,50)
atq_cpu = random.randint(1,50)
def_persona = random.randint(1,50)
def_cpu = random.randint(1,50)


hp = random.randint(200,1000)

hp_cpu = int(hp)
hp_persona = int(hp)

print(hp_cpu)
print(hp_persona)





op = input("===============================Escolha o seu destino===============================\n 1- Iniciar\n 2- Sair\n")

print(op)
turno = 1
if op != 2:
    print("===============================Duelo de Titãs===============================")
    print(f"Você\n ATQ: {atq_persona}\n DEF: {def_persona}    HP: {hp_persona}\n")
    print(f"CPU\n ATQ: {atq_cpu}\n DEF: {def_cpu}    HP: {hp_cpu}")

while op != "2":
    print(f"\n====Turno {turno}====\n Seu HP: {hp_persona} | Oponente: {hp_cpu}\n")
    vez = input("Sua vez: [1] Atacar   [2] Curar")
    if vez == "1":
        atq_p = random.randint(1, atq_persona)
        dano_ap= abs(atq_p - def_cpu)
        hp_cpu -= dano_ap
        print(f"Você atacou! Inimigo perdeu {dano_ap} de hp")
    else:
        cura = random.randint(1,25)
        hp_persona += cura
        print(f"Você recuperou {cura} de hp")

    acao_cpu = random.choice(["Atacar", "Curar"])
    if acao_cpu == "Atacar":
        atq_c = random.randint(1, atq_cpu)
        dano_ac = abs(atq_c - def_persona) #ABS vai transformar números negativos em positivos
        hp_persona -= dano_ac
        print(f"Inimigo ataca! Você perdeu {dano_ac} de hp ")
    else:
        cura = random.randint(1,25)
        hp_cpu += cura
        print(f"Inimigo recuperou {cura} de vida! ")
    turno +=1
    if hp_cpu < 0:
        print("\n==========================O duelo acabou! Você venceu!!==========================")
        break
    elif hp_persona < 0:
        print("\n==========================O duelo acabou! Você não foi forte o suficiente para vencer!==========================")
        break
    else:
        continue



