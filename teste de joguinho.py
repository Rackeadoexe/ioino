from itertools import repeat
import msvcrt
def iniciar_jogo():   
    print ("para inicar o jogo pressione enter.")
    tecla = msvcrt.getche()
    print ("Jogo iniciado")
    print ("OBJETIVO: Encontrar vilareijo")
    
    direção= input("Escolha uma das direções (norte/sul/leste/oeste)").lower()
    
    if direção == "norte":
        print ("você encontrou um poço, Vai descer ?")
        escolha = input("Descer? (s/n)").lower()
        
        if escolha=="s":
         print ("você cai e morre!")
        else:
         print ("Você foi consciente, parabens.")
    
    elif direção=="sul":
        print ("Você morreu a caminho do sul")
    
    elif direção=="leste":
        print ("Você encontrou o vilareijo, e retornou a sua casa.")
    
    elif direção=="oeste":
        print ("você se encontrou com um lobo, O que você faz (correr/lutar/tentar espantar)")
        ação = input(" O que você faz?").lower()
        
        if ação == "correr":
            print("você consegue fugir e encontrar o vilarejo")
        
        elif ação == "lutar":
            print("Sua força não se compara a do lobo e ele te mata")
        
        elif ação == "espantar":
            print ("Você o espanta com sucesso, deseja continuar a oeste ou retornar ?")
    
            ação = input ("Deseja retornar ou continuar?").lower()
            if ação == "retornar":
             print("você retorna em segurança ao vilareijo")
            else:
             print("Você pisa em falso e cai do penhasco")
             from itertools import repeat
import msvcrt
def iniciar_jogo():   
    print ("para inicar o jogo pressione enter.")
    tecla = msvcrt.getche()
    print ("Jogo iniciado")
    print ("OBJETIVO: Encontrar vilareijo")
    
    direcao= input("Escolha uma das direções (norte/sul/leste/oeste)").lower()
    
    if direcao == "norte":
        print ("você encontrou um poço, Vai descer ?")
        escolha = input("Descer? (s/n)").lower()
        
        if escolha=="s":
         print ("você cai e morre!")
        else:
         print ("Você foi consciente, parabens.")
    
    elif direcao=="sul":
        print ("Você morreu a caminho do sul")
    
    elif direcao=="leste":
        print ("Você encontrou o vilareijo, e retornou a sua casa.")
    
    elif direcao=="oeste":
        print ("você se encontrou com um lobo, O que você faz (correr/lutar/tentar espantar)")
        ação = input(" O que você faz?").lower()
        
        if ação == "correr":
            print("você consegue fugir e encontrar o vilarejo")
        
        elif ação == "lutar":
            print("Sua força não se compara a do lobo e ele te mata")
        
        elif ação == "espantar":
            print ("Você o espanta com sucesso, deseja continuar a oeste ou retornar ?")
    
            ação = input ("Deseja retornar ou continuar?").lower()
            if ação == "retornar":
             print("você retorna em segurança ao vilareijo")
            else:
             print("Você pisa em falso e cai do penhasco")
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