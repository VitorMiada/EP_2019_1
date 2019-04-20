
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
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
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
            "descricao":  "Você chega na sala Sebastião Camargo. /n Ihh! Você entrou no meio de uma aula do sétimo semestre de economia.",
        "opções": {
            "voltar": "Sair de fininho e fingir que nada aconteceu",
            "disfarce": "Colocar sua fantasia de economista e fingir que você pertence ao grupo",
            "ousadia": "Falar que você é da GV e veio fazer uma consultoria"
            }
        },
        "n": {
            "titulo": "L3",
            "descricao" : "Você chega no L3. Os fornos para calibrar sua termorresistência estão todos nas bancadas.",
            "opções": {
                "exemplar": "Ser um bom aluno e acabar seu relatório",
                "desonesto": "Descalibrar todos os fornos"
            }    
        }
            }
           
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual
inventario = []
def batalha():
    vida = 100
    print ("A new foe has appeard")
    golpes = input("O que deseja fazer: Jogar um chinelo (#entre 5 a 15 de vida), Dialogo (#entre 10 e 12), Usar um item, Cabecada (#entre 20 e 30)")# a ser desenvolvido
    while vida > 0:
        if golpes =="Jogar um chinelo":
            vida-=10#random
            print (vida)
        if golpes =="Dialogo":
            vida -=11#random
            print (vida)
        if golpes == "Usar item":
            print (inventario)# a ser desenvolvido
            print (vida)
        if golpes == "Cabecada":
            vida -=25#random
            print (vida)
            
        


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


# Programa principal.
if __name__ == "__main__":
    main()
