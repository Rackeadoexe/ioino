from game import iniciar_jogo


def main():

    while True:

        iniciar_jogo()

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()

        if jogar_novamente != "s":
            print("Obrigado por jogar!(sobreviveu mais aqui do que no jogo)")
            break


if __name__ == "__main__":
    main()