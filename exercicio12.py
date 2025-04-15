import random

#Variáveis iniciais
hp = 0
acao_cpu = []
atq_persona = random.randint(1,50)
atq_cpu = random.randint(1,50)
def_persona = random.randint(1,50)
def_cpu = random.randint(1,50)
hp = random.randint(200,1000)
hp_cpu = int(hp)
hp_persona = int(hp)

#Variáveis Cache Hit
calc1 = hp * 0.3
i = 0
c = 0

#Jogador
calculo_hit1 = hp_persona * 0.25
cache_hitp = calculo_hit1

#Cpu
calculo_hit2 = hp_cpu * 0.25
cache_hitc = calculo_hit2


#Variáveis Buffer Overflow
b_overflow = 0
b_overflowc = 0

#Variáveis Tela azul
defc_original = def_cpu
defp_original = def_persona

#Jogador Tela azul
tela_azul = False
turnos_ta = 0

#Cpu Tela azul
tela_azulc = False
turnos_tac = 0


#Variáveis Loop infinito
perdeu_vez = False #Controlar a jogabilidade do computador
loop_persona = 0
persona_vez = False
loop_cpu = 0

#pocao última chance
reviver_persona = 0
ultima_chacep = False
reviver_cpu = 0
ultima_chacec = False

#-------------------------------------------------------------------------- Jogador x CPU ---------------------------------------------------------------------

op = input("===============================Escolha o seu destino===============================\n 1- Iniciar Solo\n 2- Iniciar Multiplayer\n 3- Sair")

print(op)
turno = 1
if op == "1":
    print("===============================Duelo de Titãs===============================")
    print(f"Você\n ATQ: {atq_persona}\n DEF: {def_persona}    HP: {hp_persona}\n")
    print(f"CPU\n ATQ: {atq_cpu}\n DEF: {def_cpu}    HP: {hp_cpu}")
else:
    print("===============================Duelo de Titãs===============================")
    print(f"Jogador 1\n ATQ: {atq_persona}\n DEF: {def_persona}    HP: {hp_persona}\n")
    print(f"Jogador 2\n ATQ: {atq_cpu}\n DEF: {def_cpu}    HP: {hp_cpu}")

while op != "2" and op != "3":
    print(f"\n========Turno {turno}========\n Seu HP: {hp_persona:.2f} | Oponente: {hp_cpu:.2f}\n")
    buff_a = input("Deseja adicionar algum Efeito de status?\n [1] Sim    [2] Não")
    pocoes = input("Deseja usar alguma poção?\n [1] Sim    [2] Não")
    efeito = ["1","2","3"]
    op_pocoes = ["1","2","3", "4"]

    if persona_vez:
        print("Você perdeu a vez por conta do loop infinito do inimigo")
        persona_vez = False
        loop_cpu +=1
    else:
        vez = input("\nSua vez: [1] Atacar   [2] Curar")
        if buff_a == "1":
            efeito = input(
                "\nQual efeito deseja usar?\n "
                "1 - Buffer Overflow: A cada turno, o personagem sofre dano equivalente a 5% do HP máximo\n "
                "2 - Loop infinito: O alvo perde a vez por 1 turno enquanto reinicia o sistema\n "
                "3 - Tela Azul: Reduz a defesa para 0 por 2 turnos")
        if pocoes == "1":
            op_pocoes = input("\n Qual poção deseja usar?\n"
                              "1- Poção da última chance\n"
                              "2- Poção de fúria: aumenta o ataque em 30% em 3 turnos\n"
                              "3- Poção Soro do Berserker – Dobra o dano, mas reduz defesa pela metade.\n"
                              "4- Poção da Rocha – Aumenta a defesa em 50% por 2 turnos.")
        if op_pocoes == "1" and hp_persona == 0:
            ultima_chacep = True
            reviver_persona = 1

        if efeito == "2" and not perdeu_vez:
            if loop_persona <= 1:
                perdeu_vez = True
                loop_persona +=1

        if efeito == "1" and b_overflow <= 0:
            dano_buffa = hp * 0.05
            hp_cpu -= dano_buffa
            b_overflow += 1
            print(f"Você atacou! Inimigo perdeu {dano_buffa:.2f} por conta do Buffer Overflow")
        else:
            if efeito == "3" and not tela_azul:
                print("Você ativou o efeito Tela Azul!")
                tela_usada= True
                turnos_ta = 2

            else:
                if vez == "1":
                    atq_p = random.randint(1, atq_persona)
                    c_critico = random.randint(1,100)
                    if turnos_ta > 0:
                        def_cpu = 0
                        hp_cpu -= atq_p
                        turnos_ta -= 1
                        print(f"Você atacou! Inimigo perdeu {atq_p} por conta do efeito Tela azul")
                    else:
                        if c_critico <= 10:
                            atq_p *= 2
                            dano_critico = abs(atq_p - def_cpu)
                            hp_cpu -= dano_critico
                            print(f"Dano crítico! seu ataque aumentou em 50%! Inimigo perdeu {dano_critico} de hp")
                        else:
                            dano_ap= abs(atq_p - def_cpu)
                            hp_cpu -= dano_ap
                            print(f"Você atacou! Inimigo perdeu {dano_ap} de hp")
                else:
                    cura = random.randint(1,25)
                    hp_persona += cura
                    if hp_persona > hp:
                        hp_persona = hp
                    print(f"Você recuperou {cura} de hp")

    if perdeu_vez:
        print("O inimigo perdeu a vez por causa do loop infinito")
        perdeu_vez = False
    else:
        efeito = random.choice(["1","2", "3"])
        op_pocoes = random.choice(["1", "2", "3", "4"])
        acao_cpu = random.choice(["Atacar", "Curar"])

        if op_pocoes == "1" and hp_cpu == 0:
            ultima_chacec = True
            reviver_cpu = 1
            print("O inimigo ativou a última chance")

        if efeito == "2" and not persona_vez:
            if loop_cpu <= 1:
                persona_vez = True
                loop_cpu += 1
                print("O inimigo ativou Loop Infinito! Você perderá a próxima vez.")

        if efeito == "1" and b_overflowc <= 0:
            dano_buffac = hp * 0.05
            hp_persona -= dano_buffac
            b_overflowc += 1
            print(f"Inimigo ataca! Você perdeu {dano_buffac:.2f} por conta do Buffer Overflow")
        else:
            if efeito == "3" and not tela_azulc:
                print("O inimigo ativou o efeito Tela Azul!")
                tela_azulc = True
                turnos_tac = 2
            else:
                if acao_cpu == "Atacar":
                    atq_c = random.randint(1, atq_cpu)
                    atq_critico = random.randint(1,100)
                    if turnos_tac > 0:
                        def_persona = 0
                        hp_persona -= atq_c
                        turnos_tac -= 1
                        print(f"Inimigo ataca! Você perdeu {atq_c} por conta do efeito Tela azul.")
                    else:
                        if atq_critico <= 10:
                            atq_c *= 2
                            dano_critico2 = abs(atq_c - def_persona)
                            hp_persona -= dano_critico2
                            print(f"Dano crítico! o ataque do inimigo aumentou em 50%! Você perdeu {dano_critico2} de hp")
                        else:
                            dano_ac = abs(atq_c - def_persona) #ABS vai transformar números negativos em positivos
                            hp_persona -= dano_ac
                            print(f"Inimigo ataca! Você perdeu {dano_ac:.2f} de hp ")
                else:
                    cura = random.randint(1,25)
                    hp_cpu += cura
                    if hp_cpu > hp:
                        hp_cpu = hp
                    print(f"Inimigo recuperou {cura} de vida! ")

    turno +=1
    if hp_persona < cache_hitp:
        if i <=0:
            opcao_cha = input("Deseja usar o Cache Hit? [1] Sim    [2] Não")
            if opcao_cha == "1":
                calculo_1 = hp * 0.3
                hp_persona += calculo_1
                print(f"Você usou o Cache hit e recuperou {calculo_1:.2f} de vida")
        i +=1
    if hp_cpu < cache_hitc:
        if c <=0:
            opcao_chc = random.choice(["Sim", "Não"])
            if opcao_chc == "Sim":
                calculo_2 = hp * 0.3
                hp_cpu += calculo_2
                print(f"O oponente usou o Cache hit e recuperou {calculo_2:.2f} de vida")
            c +=1
    if reviver_persona > 0:
        hp_persona = hp * 0,25
        reviver_persona -=1
        print("Você reviveu! Agora tem mais uma chance para vencer o duelo.")
    elif reviver_cpu > 0:
        hp_cpu = hp * 0,25
        reviver_cpu -=1
        print("Você reviveu! Agora tem mais uma chance para vencer o duelo.")

    if hp_cpu < 0:
        print("\n==========================O duelo acabou! Você venceu!!==========================")
        break
    elif hp_persona < 0:
        print("\n==========================O duelo acabou! Você não foi forte o suficiente para vencer!==========================")
        break
#--------------------------------------------------------------------------Efeitos--------------------------------------------------------------------------

#sistema_critico = Adicione uma chance de 10% de dar o dobro de dano OKKKKKKKKKKKKKKKKKKKKKKKKKKK
#buffer_overflow = Efeito: A cada turno, o personagem sofre dano equivalente a 5% do seu HP máximo OKKKKKKKKKKKKKKKKKKKKKK
#loop_infinito = Efeito: O alvo perde a vez por 1 turno enquanto "reinicia o sistema"  OKKKKKKKKKKKKKKKK
#tela_Azul = Reduz a defesa para 0 por 2 turnos -  tá mec OKKKKKKKKKKKKKKKK??
#cache_hit = Recupera 30% do HP máximo. Só pode ser usado quando HP está abaixo de 25%. OKKKKKKKKKKKKK
#--------------------------------------------------------------------------Poções--------------------------------------------------------------------------
#Poção da última chance: Ativa automaticamente ao morrer e restaura 25% da vida
#Poção de fúria: aumenta o ataque em 30% em 3 turnos
#Poção Soro do Berserker – Dobra o dano, mas reduz defesa pela metade.
#Poção da Rocha – Aumenta a defesa em 50% por 2 turnos.

#-------------------------------------------------------------------------- Multiplayer ---------------------------------------------------------------------

while op != "1" and op != "3":
    print(f"\n========Turno {turno}========\n Seu HP: {hp_persona:.2f} | Oponente: {hp_cpu:.2f}\n")
    buff_a = input("Jogador 1: Deseja adicionar algum Efeito de status?\n [1] Sim    [2] Não\n")
    efeito = ["1","2","3"]

    if persona_vez:
        print("Jogador 1 perdeu a vez por conta do loop infinito do inimigo")
        persona_vez = False
        loop_cpu +=1
    else:
        vez = input("\nJogador 1: [1] Atacar   [2] Curar")
        if buff_a == "1":
            efeito = input(
                "\nQual efeito deseja usar?\n "
                "1 - Buffer Overflow: A cada turno, o personagem sofre dano equivalente a 5% do HP máximo\n "
                "2 - Loop infinito: O alvo perde a vez por 1 turno enquanto reinicia o sistema\n "
                "3 - Tela Azul: Reduz a defesa para 0 por 2 turnos\n")
        if efeito == "2" and not perdeu_vez:
            if loop_persona <= 1:
                perdeu_vez = True
                loop_persona +=1

        if efeito == "1" and b_overflow <= 0:
            dano_buffa = hp * 0.05
            hp_cpu -= dano_buffa
            b_overflow += 1
            print(f"Jogador 1 atacou! Jogador 2 perdeu {dano_buffa:.2f} por conta do Buffer Overflow")
        else:
            if efeito == "3" and not tela_azul:
                print("Você ativou o efeito Tela Azul!")
                tela_usada= True
                turnos_ta = 2
            else:
                if vez == "1":
                    atq_p = random.randint(1, atq_persona)
                    c_critico = random.randint(1,100)
                    if turnos_ta > 0:
                        def_cpu = 0
                        hp_cpu -= atq_p
                        turnos_ta -= 1
                        print(f"Jogador 1 atacou! Jogador 2 perdeu {atq_p} por conta do efeito Tela azul")
                    else:
                        if c_critico <= 10:
                            atq_p *= 2
                            dano_critico = abs(atq_p - def_cpu)
                            hp_cpu -= dano_critico
                            print(f"Dano crítico! o ataque do Jogador 1 aumentou em 50%! Jogador 2 perdeu {dano_critico} de hp")
                        else:
                            dano_ap= abs(atq_p - def_cpu)
                            hp_cpu -= dano_ap
                            print(f"Jogador 1 atacou! Jogador 2 perdeu {dano_ap} de hp")
                else:
                    cura = random.randint(1,25)
                    hp_persona += cura
                    if hp_persona > hp:
                        hp_persona = hp
                    print(f"Jogador 1 recuperou {cura} de hp")

    if perdeu_vez:
        print("O Jogador 2 perdeu a vez por causa do loop infinito")
        perdeu_vez = False
    else:
        buff_a = input("Jogador 2: Deseja adicionar algum Efeito de status?\n [1] Sim    [2] Não\n")
        vez2 = input("\nJogador 2: [1] Atacar   [2] Curar")
        if buff_a == "1":
            efeito = input(
                "\nQual efeito deseja usar?\n "
                "1 - Buffer Overflow: A cada turno, o personagem sofre dano equivalente a 5% do HP máximo\n "
                "2 - Loop infinito: O alvo perde a vez por 1 turno enquanto reinicia o sistema\n "
                "3 - Tela Azul: Reduz a defesa para 0 por 2 turnos\n")

        if efeito == "2" and not persona_vez:
            if loop_cpu <= 1:
                persona_vez = True
                loop_cpu += 1
                print("O Jogador 2 ativou Loop Infinito! Jogador 1 perderá a próxima vez.")

        if efeito == "1" and b_overflowc <= 0:
            dano_buffac = hp * 0.05
            hp_persona -= dano_buffac
            b_overflowc += 1
            print(f"Jogador 2 ataca! Jogador 1 perdeu {dano_buffac:.2f} por conta do Buffer Overflow")
        else:
            if efeito == "3" and not tela_azulc:
                print("Jogador 2 ativou o efeito Tela Azul!")
                tela_azulc = True
                turnos_tac = 2
            else:
                if acao_cpu == "Atacar":
                    atq_c = random.randint(1, atq_cpu)
                    atq_critico = random.randint(1,100)
                    if turnos_tac > 0:
                        def_persona = 0
                        hp_persona -= atq_c
                        turnos_tac -= 1
                        print(f"Jogador 2 ataca! Jogador 1 perdeu {atq_c} por conta do efeito Tela azul.")
                    else:
                        if atq_critico <= 10:
                            atq_c *= 2
                            dano_critico2 = abs(atq_c - def_persona)
                            hp_persona -= dano_critico2
                            print(f"Dano crítico! o ataque do Jogador 2 aumentou em 50%! Você perdeu {dano_critico2} de hp")
                        else:
                            dano_ac = abs(atq_c - def_persona) #ABS vai transformar números negativos em positivos
                            hp_persona -= dano_ac
                            print(f"Jogador 2 ataca! Jogador 1 perdeu {dano_ac:.2f} de hp ")
                else:
                    cura = random.randint(1,25)
                    hp_cpu += cura
                    if hp_cpu > hp:
                        hp_cpu = hp
                    print(f"Jogador 2 recuperou {cura} de vida! ")
    turno +=1
    if hp_persona < cache_hitp:
        if i <=0:
            opcao_cha = input("Jogador 1: Deseja usar o Cache Hit? [1] Sim    [2] Não")
            if opcao_cha == "1":
                calculo_1 = hp * 0.3
                hp_persona += calculo_1
                print(f"Jogador 1 usou o Cache hit e recuperou {calculo_1:.2f} de vida")
        i +=1
    if hp_cpu < cache_hitc:
        if c <=0:
            opcao_chc = input("Jogador 2: Deseja usar o Cache Hit? [1] Sim    [2] Não")
            if opcao_chc == "Sim":
                calculo_2 = hp * 0.3
                hp_cpu += calculo_2
                print(f"Jogador 2 usou o Cache hit e recuperou {calculo_2:.2f} de vida")
            c +=1
    if hp_cpu < 0:
        print("\n==========================O duelo acabou! Jogador 1 venceu!!==========================")
        break
    elif hp_persona < 0:
        print("\n==========================O duelo acabou! Jogador 2 venceu!!==========================")
        break

