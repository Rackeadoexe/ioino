def iniciar_jogo():   
    play= input("para inicar o jogo pressione enter.")
    print ("Jogo iniciado")
    print ("OBJETIVO: Levar comida ao vilarejo")
    espada = False
    jogando=True
    carne=False
    corda=False
    carta=False
    voltar=True 

    while jogando==True:   
        direcao= input("Você está na encruzilhada, escolha uma das direções (norte/sul/leste/oeste)").lower()
        voltar=True   
        if direcao == "norte":
            while voltar==True:
                
                print ("você encontrou um poço, Vai descer ?")
                escolha = input("Descer? (s/n)").lower()
                
                if escolha=="s":                
                    if corda==True:
                        print("Você desce o poço com cautela e encontra dois caminhos")
                        ação=input("deseja seguir pela direita, pela esquerda ou voltar ?")
                        
                        if ação=="esquerda":
                            print("O túnel segue profundamente, sem sinal de saida, você vai o mais fundo que pode antes de desmaiar por falta de oxigênio e morrer pela mesma causa.")
                            jogando=False
                            voltar=False
                            
                        elif ação=="direita":
                            print("Você sente a brisa vindo, ao seguir a diante, se depara com a saída do túnel, ao olhar ao redor após sair, nota que está no pé do penhasco, a sua frente há uma placa que aponta a direçãp da cidade mais próxima.")
                            ação=input("deseja seguir a estrada ou retornar a encruzilhada?(seguir/retornar)").lower()
                            if ação=="seguir":
                                print("Você chega a cidade, e decide por la viver, com suas habilidades você se torna um grande caçador, vivendo de forma pacifíca até sua morte.")
                                jogando=False
                                voltar=False
                            elif ação=="retornar":
                                print("Você retorna a encruzilhada")
                                voltar=False

                        elif ação=="voltar":
                            print("Você volta para a frente do poço.")
                            voltar=False

                    elif corda==False:
                        print ("você cai e morre!")
                        jogando = False
                        voltar = False            
                elif escolha =="n":
                    print ("Você foi consciente e retornou a encruzilhada.")
                    voltar=False
    
        elif direcao=="sul":
            ação = input("Você encontra uma cabana abandonada, perto de uma trilha floresta adentro, com uma placa pendurada escrita posto militar, na entrada há uma espada bem conservada, pegar ? (sim/não) ").lower()
            if ação == "sim":
                espada = True
                print("você pega a espada!")  
            ação = input("deseja retornar, adentrar na floresta adiante e seguir a trilha ou não seguir a trilha, porém, adentrar a floresta ?(retornar/seguir/entrar)").lower()
            
            if ação=="retornar":
                print("Você retorna a encruzilhada")
            
            elif ação == "seguir":
                print("Você segue a trilha e encontra uma árvore com uma corda pendurada em um galho robusto, ao pé da árvore há uma carta com o remetente sendo Rose.")
                ação = input("Você deseja ler a carta ?(s/n)").lower()
            
                if ação=="s":
                    print("Na carta está escrito o seguinte. -Rose, minha querida, espero que você encontre isso, mesmo que dependa do acaso para tal fato, não conseguirei voltar, não sei nem se tenho forças para isso, nossas tropas foram destroçadas. Queria passar mais tempo contigo, porém, isso será impossível, irei tomar a ultima medida que me cabe para não cair na mão do inimigo. Com amor, Josef. (você pega a carta para entregar a Rose)")
                    carta=True
                    ação=input("Você deseja pegar a corda ?(s/n)")
                    if ação=="s":
                        print("Você pega a corda e decide que é melhor retornar a encruzilhada")
                        corda=True
                    else:
                        print("Não há mais nada o que checar aqui, você volta a encruzilhada.")
            
                elif ação=="n":
                    print("Você pega a carta para entregar a Rose.")
                    carta=True
                    ação=input("Você deseja pegar a corda ?(s/n)")
                    if ação=="s":
                        print("Você pega a corda e decide que é melhor retornar a encruzilhada")
                        corda=True
                    else:
                        print("Não há mais nada o que checar aqui, você volta a encruzilhada.")
            
            elif ação=="entrar":
                print("Você se perde floresta adentro e morre de exaustão.")
                jogando=False        

        elif direcao=="leste":
            if carne==True:
                print("Você traz a carne ao vilarejo, todos celembram e preparam um banquete, você descansa após a caçada.")
                if carta==True:
                    print("Você entrega a carta a Rose, a qual agradece em lágrimas após finalmente receber a paz, mesmo que acompanhada de luto, de saber o que aconteceu com seu marido(bônus de item)")
                    jogando=False
            
            elif carne==False:
                print("Você ainda não cumpriu com o objetivo, você retorna a encruzilhada.")

        elif direcao=="oeste":
            print ("você se encontrou com um lobo, O que você faz (correr/lutar/tentar/espantar)")
            ação = input(" O que você faz?").lower()
        
            if ação == "correr":
                print("você consegue fugir até a encruzilhada, o lobo não demonstra interesse em te perseguir")
                
            elif ação == "lutar":
                if espada == True:
                    print("Você mata o lobo com a espada, pega sua carne e se depara com um grande precipicio ")
                    carne=True
                    
                    ação = input("deseja retornar ou tentar descer ?(retornar/descer)")
                    if ação=="descer":
                        if corda==False:
                            print("Ao tentar descer, você pisa em uma das pedras soltas do penhasco e escorrega para a sua morte.")
                            jogando=False     
                        if corda==True:
                            print("Você tenta descer a corda pelo penhasco, porém ele é bem maior que a corda, você desiste da ideia de tentar desce-lo e retorna a encruzilhada.")       
                    elif ação=="retornar":
                       print("Você retorna a encruzilhada.") 
                    
                elif espada == False:
                    print("Sua força não se compara a do lobo e ele te mata")
                    jogando = False
        
            elif ação == "espantar":
                print ("Você o espanta com sucesso, deseja continuar a oeste ou retornar ?")
    
                ação = input ("Deseja retornar ou continuar?").lower()
                if ação == "continuar":
                    print("Você pisa em falso e cai do penhasco")
                    jogando = False
                elif ação=="retornar":
                    print("você retorna com segurança ao inicio.")
        
            else:
                print("Ação inválida. O lobo não esperou e te atacou.")
                jogando=False
        else:
            print("Ação Invalida, você não faz nada")              
        
