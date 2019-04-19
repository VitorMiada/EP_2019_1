# EP 2019-1: Escape Insper
#
# Alunos:
# - aluno A: Vitor Kenzo Fujiwara Miada, sophiaks@al.insper.edu.br
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
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


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


for k, v in cenarios["inicio"].items():
    print(v)
a = input('Para onde você quer ir?')
if a == "andar professor":
    for k, v in cenarios["andar professor"].items():
        print(v)
b = input('Para onde você quer ir?')
if b == "biblioteca":
    for k, v in cenarios["biblioteca"].items():
        print(v)


# Programa principal.
if __name__ == "__main__":
    main()

# teste:só pra ver se é este arquivo mesmo!
