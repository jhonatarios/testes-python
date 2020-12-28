import random

def menuNiveis():
    print('''
            #####   JOGO: ADVINHE O NUMERO  #####

            Escolha a dificuldade:

            (F) - Facil (1-16)
            (M) - Medio (1-32)
            (D) - Dificil (1-64)
            (E) - Extremo (1-256)

            ou digite "S" para sair do jogo
        ''')
    return str(input('Escolha uma opção: '))

nivelEscolhido = menuNiveis()

if nivelEscolhido == 'f' or nivelEscolhido == 'F':
    numero = random.randrange(1, 16)
    escolha = int(input("\nAdvinhe um numero de 1 a 16: "))

    while escolha != numero:
        if escolha < numero:
            print("\nNao foi dessa vez :(")
            escolha = int(input("Tente um numero maior:"))
        else:
            print("\nNao foi dessa vez :(")
            escolha = int(input("Tente um numero menor:"))

    print(f"\nVoce acertou! A escolha certa era {numero}")

if nivelEscolhido == 'm' or nivelEscolhido == 'M':
    numero = random.randrange(1, 32)
    escolha = int(input("\nAdvinhe um numero de 1 a 32: "))

    while escolha != numero:
        if escolha < numero:
            print("\nNao foi dessa vez :(")
            escolha = int(input("Tente um numero maior:"))
        else:
            print("\nNao foi dessa vez :(")
            escolha = int(input("Tente um numero menor:"))

    print(f"\nVoce acertou! A escolha certa era {numero}")

if nivelEscolhido == 'd' or nivelEscolhido == 'D':
    numero = random.randrange(1, 64)
    escolha = int(input("\nAdvinhe um numero de 1 a 64: "))

    while escolha != numero:
        if escolha < numero:
            print("\nNao foi dessa vez :(")
            escolha = int(input("Tente um numero maior:"))
        else:
            print("\nNao foi dessa vez :(")
            escolha = int(input("Tente um numero menor:"))

    print(f"\nVoce acertou! A escolha certa era {numero}")

if nivelEscolhido == 'e' or nivelEscolhido == 'E':
    numero = random.randrange(1, 256)
    escolha = int(input("\nAdvinhe um numero de 1 a 256: "))

    while escolha != numero:
        if escolha < numero:
            print("\nNao foi dessa vez :(")
            escolha = int(input("Tente um numero maior:"))
        else:
            print("\nNao foi dessa vez :(")
            escolha = int(input("Tente um numero menor:"))

    print(f"\nVoce acertou! A escolha certa era {numero}")

if nivelEscolhido == 's' or nivelEscolhido == 'S':
    print("\nAté uma proxima!")
    quit()


