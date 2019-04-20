
# Alunos:
# - aluno Vitor Kenzo Fujiwara Miada, sophiaks@al.insper.edu.br
# - aluno B: Sophia Kerber Shigueoka, vitorkfm@al.insper.edu.br


def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O guardião",
            "descricao": "Voce foi até a porta da sala do professor, porém existem golens guardiões ligados a uma protoboard. "
                         "Voce vai falar com o golem e ele te empurra para tras não deixando voce entrar na sala "
                         "Voce precisa de mais itens.",
            "opcoes": {
                "inicio": "Voltar para o saguão"
            }
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca. Voce vai falar com a bibliotecaria e ela misteriosamente diz: It's dangerous to go alone, TAKE THIS!!. Voce recebeu o livro O golem ",
            "opcoes": {
                
                "aquario": "Pegar um aquario"
            }
        },
        "aquario": {
            "titulo": "Sala do sonho",
            "descricao": "Voce entrou em um aquario e acabou pegando no sono tendo um sonho no qual nao era possivel sair dele sem responder a grande pergunta: sim ou não?",
            "opcoes": {
                "s": "sim",
                "n": "nao"
            }
        },
        "s": {
            "titulo": "Sebastião Camargo",
            "descricao": "Você acorda na frente da sala Sebastião Camargo e entra nela. Ihh! Você entrou no meio de uma aula de NatDes.",
            "opcoes": {
                "voltar": "Sair de fininho e fingir que nada aconteceu",
                "disfarce": "Colocar o seu protótipo na cabeça e sair da sala",
                "ousadia": "Falar que você é o verdadeiro Vitor Macul"
            }
        },
        "n": {
            "titulo": "L3",
            "descricao" : "Você acorda no L3. Os fornos para calibrar sua termorresistência estão todos nas bancadas.",
            "opcoes": {
                "exemplar": "Ser um bom aluno e acabar seu relatório",
                "desonesto": "Descalibrar todos os fornos"
            }    
        },
        "exemplar": {
                   "titulo": "Parceria com o Carlinhos",
                   "descricao": "Voce fez prefeitamente seu relatorio. Ao explicar sua situação ao Carlos, ele te ajuda, dando uma termorresistência. Voce pegou o elevador e foi para o quinto andar. ",
                   "opcoes": {
                        "5": "Ir para o quinto andar"
                    }
                 },
        "desonesto": {
                    "titulo": "O rei mago de InstruMed",
                    "descricao": "Ao descalibrar todos dos fornos, o Mago Carlinhos te desafia para um duelo.",
                    "opcoes":{
                            "lutar2": "Lute com o Rei Mago!!"
                            }
                    },
                    "lutar2":{
                            "titulo": "Ida ao elevador",
                            "descricao": "Apos a luta vc vai para o elevador",
                            "opcoes":{
                                    "1": "Primeiro andar",
                                    "2": "Segundo andar",
                                    "3": "Terceiro andar",
                                    "4": "Quarto andar",
                                    "5": "Quinto andar"
                                    }
                            },
        "voltar": {
                "titulo": "Pego de surpresa",
                "descricao" : "Voce tentou fugir da sala mas o professor te pegou!. LUTE COM ELE!!(obs: nao lute com seu professor isso é so um joguinho ;)",
                "opcoes": {
                        "lutar1": "lute com o professor"
            }
                       
        },
        "disfarce": {
                   "titulo": "O mestre do disfarce",
                   "descricao": "Ao colocar seu protótipo na cabeça, voce percbe que ele serve como uma capa de invisibilidade. Voce ganhou o Protótipo. Voce foi para o quinto andar.",
                   "opcoes":{
                           "5": "Ir para a o quinto andar"
                           }
                   },
        "ousadia": {
                "titulo": " Not so ousado",
                "descricao": "Ao dizer que voce era o verdadeiro Vitor Macul, todos riem e o verdadeiro Vitor Macul te expulsa da aula. Voce retornou para a frente da sala.",
                "opcoes":{
                        "s": "Voltar para voltar pra frente da sala"
                        }
                },
        "lutar1" :{
                "titulo":" O elevador",
                "descricao" : "Após a luta voce vai para o elevador.",
                "opcoes":{
                        "elevador": "Chamar o elevador" 
             }
        },
        "elevador": {
                "titulo": "O Elevador macabro",
                "descricao": "Voce entra no elevador. Qual andar voce deseja?",
                "opcoes":{
                        "1": "primeiro andar",
                        "2": "segundo andar",
                        "3": "terceiro andar",
                        "4": "quarto andar",
                        "5": "quinto andar"
                        }
                },
                "1":{
                    "titulo": "O primeiro andar",
                    "descricao": "Voce chega no primeiro andar e se incomoda com alguma coisa....",
                    "opcoes":{
                            "nerdbox": "Entrar no NerdBox",
                            "elevador": "Voltar para o elevador"
                            }
                    },
                    "nerdbox":{
                            "titulo": "A caixa da depressão",
                            "descricao": "Ao adentrar no NerdBox, voce encontra o Pelicano. Ele diz que ja tentou alterar a data do EP mas falhou mizeravelmente. Porém ele diz acreditar em voce entao ele te deu uma espada",
                            "opcoes": {
                                    "elevador": "Ir para o elevador"
                                    }
                            },
                    "2":{
                     "titulo": "O segundo andar",
                     "descricao": "Voce chega no segundo andar e avista o Fernando de GDE",
                     "opcoes": {
                             "falar": "Falar com o Fernando",
                             "elevador": "Voltar para o elevador"
                             }
                     },
                     "3": {
                      "titulo": "Melhor amigo, pior inimigo",
                      "descricao": "O seu amigo ou inimigo Fukada acabou hackeando o elevador. Ele esta indisponivel para ir pro terceiro andar",
                      "opcoes": {
                              "elevador": "Voltar para o elevador"
                              }
                      },
                      "4": {
                              "titulo": "Melhor amigo, pior inimigo",
                              "descricao": "O seu amigo ou inimigo Fukada acabou hackeando o elevador. Ele esta indisponivel para ir pro terceiro andar",
                      "opcoes": {
                              "elevador": "Voltar para o elevador"
                              }
                      },
                      "5": {
                              "titulo": "O refeitorio",
                              "descricao": "Voce acaba de chegar no restaurante e acha um arduino (nao se sabe porque esta lá). Voce recebeu o arduino!",
                              "opcoes":{
                                      "ficar": "Voce irá para as salas das entidades"
                                      }
                      },
                      "ficar": {
                              "titulo": "Os ninjas assassinos",
                              "descricao": "Voce esta andando pelas salas das entidades e se sente vigiado. Não tinha ninguem la apenas voce, era o que vc achava. Do nada surge um ninja veterano te desafiando para uma luta",
                              "opcoes": {
                                      "lutar": "Lutar com o ninja",
                                      "fugir": "Escapar do ninja"
                                      }
                      },
                      "fugir": {
                              "titulo": "Voce nao escapará!!",
                              "descricao": "Voce tentou fugir mas ninjas não deixam vc escapar",
                              "opcoes": {
                                      "lutar": "Lutar contra o ninja"
                                      }
                              },
                      "lutar": {
                              "titulo": "Honra do ninja",
                              "descricao":"Após vencer o ninja ele o leva para o covil do Raul. Agora voce precisa enfrentar os golens!!",
                              "opcoes": {
                                      "lutar4": "Lutar contra os golens"
                                      }
                              }        
                }
        
           
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual
inventario = []
def batalha():
    vida_do_inimigo  = 100
    sua_vida = 100
    print (vida_do_inimigo)
    print (sua_vida)
    print ("A new foe has appeard")
    
    while vida_do_inimigo > 0:
        golpes = input("O que deseja fazer: Jogar um chinelo (#entre 5 a 15 de vida), Dialogo (#entre 10 e 12), Usar um item, Cabecada (#entre 20 e 30)")# a ser desenvolvido
        if golpes == "Jogar um chinelo":
            vida_do_inimigo-=10#random
            
        if golpes == "Dialogo":
            vida_do_inimigo -=11
        

        
        if golpes == "Cabecada":
            vida_do_inimigo -=25#random
        print (vida_do_inimigo)
        
           
        if vida_do_inimigo <= 0:
            print ("Parabens voce derrotou o professor!!!")
    while vida_do_inimigo > 0:
        sua_vida -= 10#random entre 10 a 20
        print ("O inimigo te bateu!. Sua vida é" (sua_vida))
        
            
        


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
          "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
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
            
            escolha = input("Escolha uma opcao \n")
            while escolha not in cenarios:
                print ("ação invalida")
                escolha = input("Escolha uma opcao \n")

            if escolha in opcoes:
                nome_cenario_atual = escolha

                
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
                print("Você morreu!")
        if escolha  == "biblioteca":
            inventario.append('livro, O Golem')
        if escolha == "5":
            inventario.append("arduino")
        if escolha == "disfarce":
            inventario.append("Protótipo")
        if escolha == "exemplar":
            inventario.append("Termorresistencia")
            
        if escolha == "lutar1":            
            batalha()
        if escolha == "lutar2":
            batalha()
        if escolha == "lutar":
            batalha()
        if escolha == "lutar4":
            batalha()

# Programa principal.
if __name__ == "__main__":
    main()
