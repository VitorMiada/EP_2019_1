
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
            "descricao": "Voce esta na biblioteca. Voce vai falar com a bibliotecaria e ela misteriosamente diz: It's dangerous to come alone, TAKE THIS!!. Voce recebeu o livro O golem ",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
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
                   "descricao": "Voce fez prefeitamente seu relatorio. Ao explicar sua situação ao Carlos, ele te ajuda, dando uma termorresistência. Voce voltou para o saguão. ",
                   "opcoes": {
                        "inicio": "Voltar para o saguão de entrada"
                    }
                 },
        "desonesto": {
                    "titulo": "O rei mago de InstruMed",
                    "descricao": "Ao descalibrar todos dos fornos, o Mago Carlinhos te desafia para um duelo.",
                    "opcoes":{
                            "lutar2": "Lute com o Rei Mago!!"
                            }
                    },           
        "voltar": {
                "titulo": "Pego de surpresa",
                "descricao" : "Você tentou fugir da sala mas o professor te pegou!. LUTE COM ELE!!(obs: nao lute com seu professor isso é so um joguinho ;)",
                "opcoes": {
                        "lutar1": "lute com o professor"
            }
                       
        },
        "disfarce": {
                   "titulo": "O mestre do disfarce",
                   "descricao": "Ao colocar seu protótipo na cabeça, voce percbe que ele serve como uma capa de invisibilidade. Voce ganhou o Protótipo. Voce volta para o saguão.",
                   "opcoes":{
                           "inicio": "Voltar para o saguão de entrada"
                           }
                   },
        "ousadia": {
                "titulo": " Not so ousado",
                "descricao": "Ao dizer que voce era o verdadeiro Vitor Macul, todos riem e o verdadeiro Vitor Macul te expulsa da aula. Voce retornou para o saguão.",
                "opcoes":{
                        "inicio": "Voltar para o saguão de entrada"
                        }
                },
        "lutar1" :{
                "titulo":" De volta ao saguão",
                "descricao" : "Após a luta voce retorna ao saguão e descobre outro caminho.",
                "opcoes":{
                        "andar professor": "Tomar o elevador para o andar do professor",
                        "biblioteca": "Ir para a biblioteca",
                        "elevador": "Chamar o elevador" 
             }
        }
                }
        
           
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual
inventario = []
def batalha():
    vida  = 100
    print ('vida = 100')
    print ("A new foe has appeard")
    
    while vida > 0:
        golpes = input("O que deseja fazer: Jogar um chinelo (#entre 5 a 15 de vida), Dialogo (#entre 10 e 12), Usar um item, Cabecada (#entre 20 e 30)")# a ser desenvolvido
        if golpes =="Jogar um chinelo":
            vida-=10#random
            
        if golpes =="Dialogo":
            vida -=11
        
        if golpes == "Usar item":
            vida -= 10
            print (inventario)# a ser desenvolvido
        
        if golpes == "Cabecada":
            vida -=25#random
        print (vida)
        
           
        if vida <= 0:
            print ("Parabens voce derrotou o professor!!!")
        
            
        


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

        # Aluno A: substitua este comentário pelo código para imprimir
        # o cenário atual.
        for v in cenario_atual.values():
            print(v)

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            
            escolha = input("Escolha uma opcao \n")

            if escolha in opcoes:
                nome_cenario_atual = escolha

                
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
                print("Você morreu!")
        if escolha  == "biblioteca":
            inventario.append('livro, O Golem')
        if escolha == "lutar1":
            inventario.append("protótipo final")
            
        if escolha == "lutar1":            
            batalha()
        if escolha == "lutar2":
            batalha()

# Programa principal.
if __name__ == "__main__":
    main()
