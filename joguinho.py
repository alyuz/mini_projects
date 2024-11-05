import random

print("\nBem-vindo! Lembre-se que quando uma resposta for 'Sim' ou 'Não' \nvocê deve digitar apenas 'S' para Sim e 'N' para Não")
a = str(input("\nVamos lá, animado?: "))

while a == "N" or a == "n":
        a = str(input("Não tem essa opção, animado?: "))

if a == "S" or a == "s" :
        print("\nBeleza, já que você está animadasso, você pode jogar")
        print("\nO computador pensou em um numero entre 0 e 10, você é capaz de acertar?")
        num = int(input('Bota o número pra jogo: '))
        sorteio = random.randint(0, 10)

        while True:
            if num == sorteio:
                print('\nParabéns!, o numero pensando pelo computador foi {}, o mesmo do seu!!!'.format(sorteio))
                r = str(input("\nSerá que você acerta de novo? "))
                if r == "N" or r == "n":
                    print("\nOk, ok! Até a próxima amigão.")
                    break
                elif r == "S" or r == "s" :
                    print("\nOk, vamos lá!")
                    print("\nO computador pensou em um numero entre 0 e 10, qual é esse número?")
                    num = int(input('\nBota o número pra jogo: '))
                    sorteio = random.randint(0, 10)

            else:
                    print('\nQue pena, você não acertou, o numero pensando pelo computador foi {}, mas tenta de novo!'.format(sorteio))
                    b = str(input("É sério, vai tentar de novo? "))
                    if b == "N" or b == "n":
                        print("\nNão tem essa opção.")
                        print("\nO computador pensou em um numero entre 0 e 10, você é capaz de acertar?")

                    while b == "S" or b == "s" :
                        print("\nOk, vamos lá!")
                        print("\nO computador pensou em um numero entre 0 e 10, você é capaz de acertar?")
                        num = int(input('Bota o número pra jogo: '))
                        sorteio = random.randint(0, 10)