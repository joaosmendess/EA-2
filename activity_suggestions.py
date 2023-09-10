def main (): 
    continuar= "sim"



    while continuar=="sim":
        #Entrada de dados 
        clima = input("qual o clima ? (chuvoso, ensolarado, nublado):")
        hora = input ("Qual a hora do dia? (manhã, tarde, noite):")
        horas_livres = float(input("quantas horas você tem livres agora?"))
 
          # Calcula o tempo sugerido para a atividade
        tempo_sugerido = horas_livres / 2  # supondo que use metade do tempo livre
        
        # Sugestões com base no clima e hora
        if clima == "chuvoso":
            if hora == "manhã":
                print(f"Leia um livro por {tempo_sugerido} horas.")
            elif hora == "tarde":
                print(f"Assista a um filme por {tempo_sugerido} horas.")
            else:
                print(f"Ouça música relaxante por {tempo_sugerido} horas.")

        elif clima == "ensolarado":
            if hora == "manhã":
                print(f"Faça uma caminhada por {tempo_sugerido} horas.")
            elif hora == "tarde":
                print(f"Vá nadar por {tempo_sugerido} horas.")
            else:
                print(f"Contemple as estrelas por {tempo_sugerido} horas.")

        else:  # assumindo nublado
            if hora == "manhã":
                print(f"Faça yoga por {tempo_sugerido} horas.")
            elif hora == "tarde":
                print(f"Visite um museu por {tempo_sugerido} horas.")
            else:
                print(f"Prepare um chá e relaxe por {tempo_sugerido} horas.")
        
        # Pergunta se o usuário quer continuar
        continuar = input("Deseja continuar? (sim/não) ").lower()

main()