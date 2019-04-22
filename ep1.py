# Alunos:
# - aluno Vitor Kenzo Fujiwara Miada, sophiaks@al.insper.edu.br
# - aluno B: Sophia Kerber Shigueoka, vitorkfm@al.insper.edu.br
import random
inventario = {}
pontos_carisma = {
    "carisma": 10
}
aliados = []

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "\nSaguão do perigo",
            "descricao": "Você esta no saguão de entrada do Insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "\nAndar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguão de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "\nO guardião",
            "descricao": "Você foi até a porta da sala do professor, porém existem golens guardiões ligados a uma protoboard. "
                         "Você vai falar com o golem. Ele te empurra para trás e não te deixa entrar na sala "
                         "Você precisa de mais itens.",
            "opcoes": {
                "inicio": "Voltar para o saguão"
            }
        },
        "biblioteca": {
            "titulo": "\nCaverna da tranquilidade",
            "descricao": "Você está na biblioteca. Você vai falar com a bibliotecaria e ela misteriosamente diz: It's dangerous to go alone, TAKE THIS!!. \n Você recebeu o livro 'O golem' ",
            "opcoes": {
                "aquario": "Pegar um aquário"
            }
        },
        "aquario": {
            "titulo": "\nSala do sonho",
            "descricao": "Você entrou em um aquário e acabou pegando no sono, tendo um sonho no qual não era possivel acordar sem responder uma pergunta: o teletransporte é possível?",
            "opcoes": {
                "s": "sim",
                "n": "não"
            }
        },
        "s": {
            "titulo": "\nSebastião Camargo",
            "descricao": "Parece que sua resposta estava correta. Você acorda na frente da sala Sebastião Camargo e entra nela. Ihh! Você entrou no meio de uma aula de NatDes.",
            "opcoes": {
                "voltar": "Sair de fininho e fingir que nada aconteceu",
                "disfarce": "Colocar o seu protótipo na cabeça e sair da sala",
                "ousadia": "Falar que você é o verdadeiro Vitor Macul"
            }
        },
        "n": {
            "titulo": "\nL3",
            "descricao": "Sua resposta estava errada. O teletransporte é possível! Você acorda no L3. Os fornos para calibrar sua termorresistência estão todos nas bancadas.",
            "opcoes": {
                "exemplar": "Ser um bom aluno e acabar seu relatório",
                "desonesto": "Descalibrar todos os fornos"
            }
        },
        "exemplar": {
            "titulo": "\nParceria com o Carlinhos",
            "descricao": "Voce fez perfeitamente seu relatório. Ao explicar sua situação ao Carlos, ele te ajuda, te dando uma termorresistência. Você pega o elevador e vai para o quinto andar. ",
            "opcoes": {
                "5": "Ir para o quinto andar"
            }
        },
        "desonesto": {
            "titulo": "\nO rei mago de InstruMed",
            "descricao": "Ao descalibrar todos dos fornos, o Mago Carlinhos te desafia para um duelo.",
            "opcoes": {
                "lutar2": "Lute com o Rei Mago!!"
            }
        },
        "lutar1": {
            "titulo": "\nIda ao elevador",
            "descricao": "Apás a luta você vai para o elevador",
            "opcoes": {
                "1": "Primeiro andar",
                "2": "Segundo andar",
                "3": "Terceiro andar",
                "4": "Quarto andar",
                "5": "Quinto andar"
            }
        },
        "voltar": {
            "titulo": "\nPego de surpresa",
            "descricao": "Você tentou fugir da sala mas o professor te pegou! \n LUTE COM ELE! \n(observação: não lute com seu professor, isso é so um joguinho!)",
            "opcoes": {
                "lutar1": "lute com o professor"
            }

        },
        "disfarce": {
            "titulo": "\nO mestre do disfarce",
            "descricao": "Ao colocar seu protótipo na cabeça, voce percebe que ele serve como uma capa de invisibilidade. Voce ganhou o Protótipo e foi para o quinto andar.",
            "opcoes": {
                "5": "Ir para a o quinto andar"
            }
        },
        "ousadia": {
            "titulo": "\nNot so ousado",
            "descricao": "Ao dizer que você era o verdadeiro Vitor Macul, todos riem e o verdadeiro Vitor Macul te expulsa da aula. \n Você retornou para a frente da sala.",
            "opcoes": {
                "s": "Voltar para voltar pra frente da sala"
            }
        },
        "lutar2": {
            "titulo": "\nO elevador",
            "descricao": "Após a luta você vai para o elevador.",
            "opcoes": {
                "elevador": "Chamar o elevador",
                "aquario": "Voltar pro aquario"
            }
        },
        "elevador": {
            "titulo": "\nO Elevador macabro",
            "descricao": "Você entra no elevador. Para qual andar você deseja ir?",
            "opcoes": {
                "1": "primeiro andar",
                "2": "segundo andar",
                "3": "terceiro andar",
                "4": "quarto andar",
                "5": "quinto andar"
            }
        },
        "1": {
            "titulo": "\nO primeiro andar",
            "descricao": "Você chega no primeiro andar e se incomoda com alguma coisa....",
            "opcoes": {
                "nerdbox": "Entrar no NerdBox",
                "elevador": "Voltar para o elevador"
            }
        },
        "nerdbox": {
            "titulo": "\nA caixa da depressão",
            "descricao": "Ao adentrar no NerdBox, você encontra o Pelicano. Ele diz que ja tentou alterar a data do EP, mas falhou miseravelmente. Porém, diz acreditar em você, e te dá a espada da modelagem",
            "opcoes": {
                "elevador": "Ir para o elevador"
            }
        },
        "2": {
            "titulo": "\nO segundo andar",
            "descricao": "Você chega no segundo andar e avista o Fernando de GDE",
            "opcoes": {
                    "falar": "Falar com o Fernando",
                    "elevador": "Voltar para o elevador"
            }
        },
        "falar": {
            "titulo": "Humanas na veia",
            "descricao": "Você fala com o Fernando de GDE. Ele te informa que tentou falar com o Raul sobre o EP\ne para te ajudar, te ensina a ser mais convincente no seu diálogo.\nVocê ganhou 4 pontos de carisma!",
            "opcoes": {
                "elevador": "Ir para o elevador"
            }
        },
        "3": {
            "titulo": "\nMelhor amigo, pior inimigo",
                      "descricao": "O seu amigo/inimigo Lucas Fukada acabou hackeando o elevador. Você não pode ir pro terceiro andar",
                      "opcoes": {
                          "elevador": "Voltar para o elevador"
                      }
        },
        "4": {
            "titulo": "\nMelhor amigo, pior inimigo",
            "descricao": "O seu amigo/inimigo Lucas Fukada acabou hackeando o elevador. Você não pode ir pro quarto andar",
                      "opcoes": {
                          "elevador": "Voltar para o elevador"
                      }
        },
        "5": {
            "titulo": "\nO refeitorio",
            "descricao": "Você acabou de chegar no restaurante e acha um arduíno (não se sabe porque está lá). Você recebeu o arduino!",
            "opcoes": {
                "entidades": "Você irá para as salas das entidades",
                "quadra": "Você irá para a quadra"
            }
        },
        "quadra": {
            "titulo": "\nRefúgio dos atletas",
            "descricao": "Você consegue ver que há alguém no meio da quadra \ne que alguém deixou uma bola de futebol perto do portão.",
                "opcoes":{
                    "pegar bola": "Você pega a bola de futebol.",
                    "conversa": "Você se aproxima da pessoa que está no meio da quadra e tenta iniciar uma conversa.",
                    "5": "Você volta para o quinto andar"
                }
        },
        "conversa": {
            "título": "\nUm estranho familiar",
            "descricao": "Ao se aproximar, você percebe que a pessoa está com um computador na mão \n e está fazendo o EP de última hora.",
            "opcoes": {
                "ajuda": "Você decide ser solidário e ajuda a pessoa no EP",
                "convencer": "Você tenta convencer a pessoa e que o Raul vai adiar a entrega de todos os EPs",
                "5": "Você deixa a pessoa em paz e volta para o quinto andar"
            }
        },
        "ajuda": {
            "titulo": "\nTodos no mesmo barco",
            "descricao": "Você ajuda seu colega. Você ganhou carisma e um aliado!",
            "opcoes":{
                "5": "Você volta para o quinto andar."
            }
        },
        "pegar bola": {
            "título": "\nUma pessoa correta?",
            "descricao": "Você pega a bola. Pode levá-la para casa ou devolvê-la na atlética.\nA bola foi adicionada ao seu inventário.",
            "opcoes": {
                "entidades": "Ir para a sala de entidades"
            }
        },
        "quadra 2": {
            "titulo": "\nRefúgio dos atletas",
            "descricao": "Você consegue ver que há alguém no meio da quadra.",
                "opcoes":{
                    "conversa": "Você se aproxima da pessoa que está no meio da quadra e tenta iniciar uma conversa.",
                    "5": "Você volta para o quinto andar"
                }
        },
        "convencer": {
            "titulo": "\nConfiança",
            "descricao": "Você tenta convencer a pessoa, mas ela acha que você está mentindo. Você perdeu três pontos de carisma.",
            "opcoes": {
                "entidades": "Ir para a sala de entidades"
            }
        },
        "entidades": {
            "titulo": "\nOs ninjas assassinos",
            "descricao": "Você está andando pela salas das entidades e se sente vigiado. Não tem ninguém lá, apenas você, ou era o que você achava... \n Do nada surge um ninja veterano te desafiando para uma luta",
            "opcoes": {
                "lutar3": "Lutar com o ninja",
                "fugir": "Escapar do ninja",
                "classy":"Educadamente pedir um segundo para entrar na sala de entidades."
            }
        },
        "classy":{
            "título": "\nA sala da confusão",
            "descricao": "Você está na sala das entidades. Há algumas pessoas da atlética.",
            "opcoes": {
                "bola": "Você devolve a bola para os membros da atlética.",
                "entidades": "Como prometido, você volta para lutar com o ninja"
            }
        },
        "bola": {
            "opcoes": {
                "entidades": "Você volta para sala de entidades"
            }
        },
        "fugir": {
            "titulo": "\nNão escaparás!!",
            "descricao": "Você tenta fugir mas os ninjas não te deixam escapar",
            "opcoes": {
                "lutar4": "Lutar contra o ninja"
            }
        },
        "lutar4": {
            "titulo": "\nHonra do ninja",
            "descricao": "Após vencer o ninja, ele o leva para o covil do Raul. \n Agora você precisa enfrentar os golens!!",
            "opcoes": {
                "lutar5": "Lutar contra os golens"
            }
        },
        "lutar5": {
            "titulo": "\nO fim se aproxima...",
            "descricao": "Você consegue ver o Raul",
            "opcoes": {
               "luta_final": "Luta meu!"
           } 
        },
        "luta_final": {
            "titulo": "A sobrevivência do mais forte"
            "descricao": "O RAUL TE ATACA"
        }
    }

    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

#---Função para batalhas com os professores---#
def batalha1():
    sua_vida = 100
    vida_do_inimigo = 100
    print("\nVida do inimigo: {0}".format(vida_do_inimigo))
    print("Sua vida: {0}".format(sua_vida))
    print("\nA NEW FOE HAS APPEARED")

    while vida_do_inimigo > 0 and sua_vida > 0:
        golpes = input("O que deseja fazer: Jogar um chinelo (entre 20 a 35 de dano) \n Dialogo (depende das suas habilidades persuasivas) \n Usar item \n Cabecada (entre 20 e 30 de dano)\n ")
        if golpes == "Jogar um chinelo":
            n = random.randint(20, 35)
            dano = n
            vida_do_inimigo -= dano
            print("\nVida do inimigo: {0}".format(vida_do_inimigo))
            print("Sua vida: {0}".format(sua_vida))

            #---Inimigo começa a atacar se tiver menos de 70 de vida---#
            if vida_do_inimigo < 70:
                a = random.randint(1, 2)
                if a == 2:
                    n = random.randint(10, 50)
                    dano = n
                    sua_vida -= dano
                    print(
                        "O inimigo te bateu!. Sua vida agora é {0}".format(sua_vida))

            #---Derrotou o inimigo---#
            if vida_do_inimigo <= 0:
                print("Parabéns, você derrotou seu oponente!!!")
                print("Sua vida: {0}".format(sua_vida))
                
        
        #---Escolheu item---#
        if golpes == "Usar item":
            print(inventario)
            a = input("Que item você quer usar?\n")
            if a == 'arduino':
                print("\nO arduino só pode ser utilizado uma vez")
                b = input(
                    "\nVocê tem certeza que quer utilizá-la? (responda sim ou nao)")
                if b == 'sim':
                    print("\nVocê usou a porta de 5V para recuperar sua vida!")
                    inventario["arduino"] = 0
                    sua_vida = 100
                elif b == 'não':
                    print("\nEscolha outro item")
            if a == 'livro O Golem':
                print("\nO livro do Golem não foi efetivo")
            if a == 'termorresistencia':
                print("\nA termorresistência só pode ser utilizada uma vez")
                c = input(
                    "\nVocê tem certeza que quer utilizá-la? (responda sim ou nao)")
                if c == 'sim':
                    print(
                        "Você usou o fio da sua termorresistência para imobilizar seu inimigo e ganhou a batalha")
                    inventario["termorresistencia"] = 0
                if c == 'nao':
                    print(inventario)
                else:
                    print("Escolha inválida")
               
        #===Escolheu diálogo---#
        if golpes == "Dialogo":
            for v in pontos_carisma.values():
                if v >= 12:
                    n = random.randint(30,40)
                    dano = n
                    vida_do_inimigo -= dano
                    print("\nVida do inimigo: {0}".format(vida_do_inimigo))
                    print("Sua vida: {0}".format(sua_vida))
                if v < 12:
                    n = random.randint(10,25)
                    dano = n
                    vida_do_inimigo -= dano
                    print("\nVida do inimigo: {0}".format(vida_do_inimigo))
                    print("Sua vida: {0}".format(sua_vida))

            
            #---Inimigo começa a atacar se tiver menos de 70 de vida---#
            if vida_do_inimigo < 70:
                a = random.randint(1, 2)
                if a == 2:
                    n = random.randint(10, 30)
                    dano = n
                    sua_vida -= dano
                    print("O inimigo te bateu!. Sua vida agora é {0}".format(sua_vida))
                    
            #---Derrotou o oponente---#        
            if vida_do_inimigo <= 0:
                print("Parabéns, você derrotou seu oponente!!!")
                print("Sua vida: {0}".format(sua_vida))
           #---Perdeu o jogo---#     
            if sua_vida <= 0:
                print("Você morreu!")
                
        #===Escolheu cabeçada---#
        if golpes == "Cabecada":
            n = random.randint(20, 30)
            dano = n
            vida_do_inimigo -= dano
            print("\nVida do inimigo: {0}".format(vida_do_inimigo))
            print("Sua vida: {0}".format(sua_vida))
            
            #---Inimigo começa a atacar se tiver menos de 70 de vida---#
            if vida_do_inimigo < 70:
                a = random.randint(1, 2)
                if a == 2:
                    n = random.randint(10, 60)
                    dano = n
                    sua_vida -= dano
                    print("O inimigo te bateu!. Sua vida agora é {0}".format(sua_vida))
                    
            #---Derrotou o inimigo---#        
            if vida_do_inimigo <= 0:
                print("Parabéns, você derrotou o professor!!!")
                print("Sua vida: {0}".format(sua_vida))
            #---Perdeu o jogo---#
            if sua_vida <= 0:
                print("Você morreu!\nSe você souber o nome de alguma sala no Insper, é possível se teletransportar e voltar a jogar.\nCaso o contrário, você perdeu!")


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa ideia: vou só jogar um pouquinho e assistir um episódio de Netflix"
          "Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
          "na entrada do Insper, e quer procurar o professor para pedir um "
          "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        for v in cenario_atual.values():
            print(v)

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            escolha = input("Escolha uma opção \n")
            while escolha not in cenarios:
                print("\nação inválida")
                escolha = input("Escolha uma opção \n")

            if escolha in opcoes:
                nome_cenario_atual = escolha

            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
                print("Você morreu!")
        if escolha == "biblioteca":
            inventario['livro O Golem'] = 1
        if escolha == "5":
            if "arduino" not in inventario:
                inventario["arduino"] = 1
            elif "arduino" in inventario:
                cenarios["5"]["descricao"] = "Você voltou para o restaurante."
            print("Você comeu um salgado e recuperou sua vida!")
        if escolha == "disfarce":
            if "Prototipo" not in inventario:
                inventario["Protótipo"] = 1
        if escolha == "exemplar":
            inventario["Termorresistencia"] = 1
            aliados.append("Carlos")
        if escolha == "Oferecer ajuda":
            inventario["Aliados"] = 1
        if escolha == "pegar bola":
            inventario["Bola de futebol"] = 1
        if escolha == "conversa":
            for v in pontos_carisma.values():
                v -= 3
                print("Você tem {0} de carisma".format(v))
        if escolha == "classy":
            for v in pontos_carisma.values():
                v += 2
                print("Você tem {0} de carisma".format(v))
        if escolha == "bola":
            aliados.append("MembrodaAtlética_1")
            aliados.append("MembrodaAtlética_2")
            aliados.append("MembrodaAtlética_3")
            print("Você tem {0} de carisma".format(v))
            print("Você ganhou mais três aliados!")
            print("Seus aliados: {0}".format(aliados))
            for v in pontos_carisma.values():
                v += 2
                print("Você tem {0} de carisma".format(v))
            inventario["Bola de futebol"] = 0
        if escolha == "3":
            with open('arquivo.txt', 'r') as arquivo:
                conteudo = arquivo.read()
                print(conteudo)
        if escolha == "4":
            with open('arquivo.txt', 'r') as arquivo:
                conteudo = arquivo.read()
                print(conteudo)
        if escolha == "nerdbox":
            inventario["Espada da modelagem"] = 1 
            aliados.append("Pelicano")
            print("Seus aliados: {0}".format(aliados))
        if escolha == "falar":
            for v in pontos_carisma.values():
                v += 2
                print("Você tem {0} de carisma".format(v))
        if escolha == "ajuda":
            aliados.append("Amigo do EP")
            print("Seus aliados: {0}".format(aliados))

        #--- Escolhas da luta ---#
        if escolha == "lutar1":
            batalha1()
        if escolha == "lutar2":
            batalha1()
        if escolha == "lutar3":
            batalha1()
        if escolha == "lutar4":
            batalha1()
        if escolha == "luta_final"
            batalha1()

# Programa principal.
if __name__ == "__main__":
    main()