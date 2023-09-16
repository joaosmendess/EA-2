def obter_sugestao(clima, hora, horas_livres):
    # Matriz de sugestões com base no clima e na hora
     sugestoes = {
        "chuvoso": {
            "manhã": "Leia um livro",
            "tarde": "Assista a um filme",
            "noite": "Ouça música relaxante"
        },
        "ensolarado": {
            "manhã": "Faça uma caminhada",
            "tarde": "Vá nadar",
            "noite": "Contemple as estrelas"
        },
        "nublado": {
            "manhã": "Faça yoga",
            "tarde": "Visite um museu",
            "noite": "Prepare um chá e relaxe"
        }
    }
     

     atividade = sugestoes.get(clima, {}).get(hora, "Descanse")
     tempo_sugerido = horas_livres / 2

     return f"{atividade} por {tempo_sugerido} horas."


def main():
    continuar = "sim"
    while continuar == "sim":
        # Entrada de dados
        clima = input("Qual o clima? (chuvoso, ensolarado, nublado):")
        hora = input("Qual a hora do dia? (manhã, tarde, noite):")
        horas_livres = float(input("Quantas horas você tem livres agora?"))
        
        sugestao = obter_sugestao(clima, hora, horas_livres)
        print(sugestao)
        
        # Pergunta se o usuário quer continuar
        continuar = input("Deseja continuar? (sim/não) ").lower()

main()