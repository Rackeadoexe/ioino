import msvcrt
def iniciar_jogo():   
    play= input("para inicar o jogo pressione enter.")
    print ("Jogo iniciado")
    print ("OBJETIVO: Levar comida ao vilareijo")
    espada = False
    jogando=True
    carne=False
    while jogando==True:   
        direcao= input("Você se encontra em uma encruzilhada, escolha uma das direções (norte/sul/leste/oeste)").lower()
    
        if direcao == "norte":
            print ("você encontrou um poço, Vai descer ?")
            escolha = input("Descer? (s/n)").lower()
        
            if escolha=="s":
                print ("você cai e morre!")
                jogando = False
            else:
                print ("Você foi consciente e retornou a encruzilhada.")
    
        elif direcao=="sul":
            ação = input("Você encontra uma cabana abandonada, perto de uma floresta densa, com uma placa pendurada escrita posto militar, na entrada há uma espada bem conservada, pegar ? (sim/não) ").lower()
            if ação == "sim":
                espada = True
                print("você pega a espada!") 
        
            ação = input("deseja retornar ou adentrar na floresta adiante?(retornar/prosseguir)")
            if ação=="retornar":
                print("Você retorna a encruzilhada")
            elif ação == "prosseguir":
                print("Você se perde na floresta e morre por exaustão.")
                jogando = False

        elif direcao=="leste":
            if carne==True:
                print("Você traz a carne ao vilareijo, todos celembram e preparam um banquete, você descansa após a caçada.")
                jogando=False
            elif carne==False:
                print("Você ainda não cumpriu com o objetivo, você retorna a encruzilhada.")

        elif direcao=="oeste":
            print ("você se encontrou com um lobo, O que você faz (correr/lutar/tentar espantar)")
            ação = input(" O que você faz?").lower()
        
            if ação == "correr":
                print("você consegue fugir até a encruzilhada, o lobo não demonstra interesse em te perseguir")
                
            elif ação == "lutar":
                if espada == True:
                    print("Você mata o lobo com a espada, pega sua carne e se depara com um grande precipicio ")
                    carne=True
                    
                    ação = input("deseja retornar ou tentar descer ?(retornar/descer)")
                    if ação=="descer":
                        print("Ao tentar descer, você pisa em uma das pedras soltas do penhasco e escorrega para a sua morte.")
                        jogando=False     
                        
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

        else:
            print("Direção inválida. Você ficou parado até morrer de fome.")  
        
while True:
    iniciar_jogo()
    
    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    
    if jogar_novamente != "s":
        print("Obrigado por jogar! (sobreviveu mais aqui do que no jogo)")
        break      
