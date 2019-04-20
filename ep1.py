# Alunos:
# - aluno Vitor Kenzo Fujiwara Miada, sophiaks@al.insper.edu.br
# - aluno B: Sophia Kerber Shigueoka, vitorkfm@al.insper.edu.br
import random

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
            "descricao" : "Sua resposta estava errada. O teletransporte é possível! Você acorda no L3. Os fornos para calibrar sua termorresistência estão todos nas bancadas.",
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
                    "opcoes":{
                            "lutar1": "Lute com o Rei Mago!!"
                            }
                    },
                    "lutar":{
                            "titulo": "\nIda ao elevador",
                            "descricao": "Apás a luta você vai para o elevador",
                            "opcoes":{
                                    "1": "Primeiro andar",
                                    "2": "Segundo andar",
                                    "3": "Terceiro andar",
                                    "4": "Quarto andar",
                                    "5": "Quinto andar"
                                    }
                            },
        "voltar": {
                "titulo": "\nPego de surpresa",
                "descricao" : "Você tentou fugir da sala mas o professor te pegou! \n LUTE COM ELE! \n(observação: não lute com seu professor, isso é so um joguinho!)",
                "opcoes": {
                        "lutar1": "lute com o professor"
            }
                       
        },
        "disfarce": {
                   "titulo": "\nO mestre do disfarce",
                   "descricao": "Ao colocar seu protótipo na cabeça, voce percebe que ele serve como uma capa de invisibilidade. Voce ganhou o Protótipo e foi para o quinto andar.",
                   "opcoes":{
                           "5": "Ir para a o quinto andar"
                           }
                   },
        "ousadia": {
                "titulo": "\nNot so ousado",
                "descricao": "Ao dizer que você era o verdadeiro Vitor Macul, todos riem e o verdadeiro Vitor Macul te expulsa da aula. \n Você retornou para a frente da sala.",
                "opcoes":{
                        "s": "Voltar para voltar pra frente da sala"
                        }
                },
        "lutar1" :{
                "titulo":"\nO elevador",
                "descricao" : "Após a luta você vai para o elevador.",
                "opcoes":{
                        "elevador": "Chamar o elevador",
                        "aquario": "Voltar pro aquario"
             }
        },
        "elevador": {
                "titulo": "\nO Elevador macabro",
                "descricao": "Você entra no elevador. Para qual andar você deseja ir?",
                "opcoes":{
                        "1": "primeiro andar",
                        "2": "segundo andar",
                        "3": "terceiro andar",
                        "4": "quarto andar",
                        "5": "quinto andar"
                        }
                },
                "1":{
                    "titulo": "\nO primeiro andar",
                    "descricao": "Você chega no primeiro andar e se incomoda com alguma coisa....",
                    "opcoes":{
                            "nerdbox": "Entrar no NerdBox",
                            "elevador": "Voltar para o elevador"
                            }
                    },
                    "nerdbox":{
                            "titulo": "\nA caixa da depressão",
                            "descricao": "Ao adentrar no NerdBox, você encontra o Pelicano. Ele diz que ja tentou alterar a data do EP, mas falhou miseravelmente. Porém, diz acreditar em você, e te dá a espada da modelagem",
                            "opcoes": {
                                    "elevador": "Ir para o elevador"
                                    }
                            },
                    "2":{
                     "titulo": "\nO segundo andar",
                     "descricao": "Você chega no segundo andar e avista o Fernando de GDE",
                     "opcoes": {
                             "falar": "Falar com o Fernando",
                             "elevador": "Voltar para o elevador"
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
                              "descricao": "Você acabou de chegar no restaurante e acha um arduíno (não se sabe porque está lá). Você recebeu o arduino!\n Também come um salgado e recupera toda sua vida.",
                              "opcoes":{
                                      "ficar": "Voce irá para as salas das entidades"
                                      }
                      },
                      "ficar": {
                              "titulo": "\nOs ninjas assassinos",
                              "descricao": "Você está andando pelas salas das entidades e se sente vigiado. Não tem ninguém lá, apenas você, ou era o que você achava... \n Do nada surge um ninja veterano te desafiando para uma luta",
                              "opcoes": {
                                      "lutar": "Lutar com o ninja",
                                      "fugir": "Escapar do ninja"
                                      }
                      },
                      "fugir": {
                              "titulo": "\nNão escaparás!!",
                              "descricao": "Você tenta fugir mas os ninjas não te deixam escapar",
                              "opcoes": {
                                      "lutar": "Lutar contra o ninja"
                                      }
                              },
                      "lutar": {
                              "titulo": "\nHonra do ninja",
                              "descricao":"Após vencer o ninja, ele o leva para o covil do Raul. \n Agora você precisa enfrentar os golens!!",
                              "opcoes": {
                                      "lutar": "Lutar contra os golens"
                                      }
                              }        
                }
        
           
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual
inventario = []
def batalha(vida_do_inimigo, sua_vida):
    print ("\nVida do inimigo: {0}".format(vida_do_inimigo))
    print ("Sua vida: {0}".format(sua_vida))
    print ("\nA NEW FOE HAS APPEARED")
    
    while vida_do_inimigo > 0 and sua_vida > 0:
        golpes = input("O que deseja fazer: Jogar um chinelo (entre 20 a 35 de dano) \n Dialogo (depende das suas habilidades persuasivas) \n Usar item \n Cabecada (entre 20 e 30 de dano)\n")
        if golpes == "Jogar um chinelo":
            n = random.randint(20,35)
            dano = n
            vida_do_inimigo -= dano
            print("\nVida do inimigo: {0}".format(vida_do_inimigo))
            print("Sua vida: {0}".format(sua_vida))
           
            if vida_do_inimigo < 70:
                a = random.randint(1,2)
                if a == 2:
                    n = random.randint(10, 50)
                    dano = n
                    sua_vida -= dano
                    print ("O inimigo te bateu!. Sua vida agora é {0}".format(sua_vida))
            if vida_do_inimigo <= 0:
                print ("Parabéns, você derrotou seu oponente!!!")
                print("Sua vida: {0}".format(sua_vida))
                
            if sua_vida <= 0:
                print ("Você morreu!")
                
        if golpes == "Usar item":
            print(inventario)
            a = input("Que item você quer usar?\n")
            if a == 'arduino':
                print("\nO arduino só pode ser utilizado uma vez")
                b = input("\nVocê tem certeza que quer utilizá-la? (responda sim ou nao)")
                if b == 'sim':
                    print("\nVocê usou a porta de 5V para recuperar sua vida!")
                    del inventario[arduino]
                    sua_vida = 100
                elif b == 'não':
                    print("\nEscolha outro item")
            if a == 'livro O Golem':
                print("\nO livro do Golem não foi efetivo")
            if a == 'termorresistencia':
                print("\nA termorresistência só pode ser utilizada uma vez")
                c = input("\nVocê tem certeza que quer utilizá-la? (responda sim ou nao)")
                if c == 'sim':
                    print("Você usou o fio da sua termorresistência para imobilizar seu inimigo e ganhou a batalha")
                    del inventario[termorresistencia]
                if c == 'nao':
                    print(inventario)
                else:
                    print("Escolha inválida")
            
            
        if golpes == "Dialogo":
            n = random.randint(0, 70)
            dano = n
            vida_do_inimigo -= dano
            print("\nVida do inimigo: {0}".format(vida_do_inimigo))
            print("Sua vida: {0}".format(sua_vida))
            
            if vida_do_inimigo < 70:
                a = random.randint(1,2)
                if a == 2:
                    n = random.randint(10, 30)
                    dano = n
                    sua_vida -= dano
                    print ("O inimigo te bateu!. Sua vida agora é {0}".format(sua_vida))
            if vida_do_inimigo <= 0:
                print ("Parabéns, você derrotou seu oponente!!!")
                print("Sua vida: {0}".format(sua_vida))
               
            if sua_vida <= 0:
                print ("Você morreu!")
        if golpes == "Cabecada":
            n = random.randint(20, 30)
            dano = n
            vida_do_inimigo -= dano
            print("\nVida do inimigo: {0}".format(vida_do_inimigo))
            print("Sua vida: {0}".format(sua_vida))
            vida_atualizada = sua_vida
            if vida_do_inimigo < 70:
                a = random.randint(1,2)
                if a == 2:
                    n = random.randint(10, 30)
                    dano = n
                    sua_vida -= dano
                    print ("O inimigo te bateu!. Sua vida agora é {0}".format(sua_vida))
            if vida_do_inimigo <= 0:
                print ("Parabéns, você derrotou seu oponente!!!")
                print("Sua vida após a luta: {0}".format(sua_vida))
            
            if sua_vida <= 0:
                print ("Você morreu!\nSe você souber o nome de alguma sala no Insper, é possível se teletransportar e voltar a jogar.\nCaso o contrário, você perdeu!")
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
                print ("\nação inválida")
                escolha = input("Escolha uma opção \n")

            if escolha in opcoes:
                nome_cenario_atual = escolha

                
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
                print("Você morreu!")
        if escolha  == "biblioteca":
            inventario.append('livro O Golem')
        if escolha == "5":
            inventario.append("arduino")
        if escolha == "disfarce":
            inventario.append("Protótipo")
        if escolha == "exemplar":
            inventario.append("Termorresistencia")
            
        if escolha == "lutar1":            
            batalha(100, 100)
        if escolha == "lutar":
            batalha(vida_do_inimigo, sua_vida)

# Programa principal.
if __name__ == "__main__":
    main()