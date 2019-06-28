from random import randint
from time import sleep
jokenpo = [
    'PEDRA',
    'PAPEL',
    'TESOURA'
]

while True:
    print()
    print('{:=^40}'.format(' \033[1;35mJOKÊNPO\033[m '))
    print('Suas opções:')
    for js, ls in enumerate(jokenpo):
        print(f'[ {js + 1} ]', ls)
    # computador suas jogadas
    computador = randint(0,2)
    # ######################
    # Jogador escolher sua jogada.
    jogador = int(input('Qual sua jogada? '))
    jogador -= 1
    print('\033[1;35mJO\033[m')
    sleep(1)
    print('\033[1;35mKEN\033[m')
    sleep(1)
    print('\033[1;35mPO!!!\033[m')
    sleep(0.6)
    print('=-' * 12)
    # #######################
    # ############# JOGADAS #################
    print(f'Computador jogou {jokenpo[computador]}')
    try:
        print(f'Jogador jogou {jokenpo[jogador]}')
    except IndexError:
        print()
        print('INVÁLIDO')
        print('Digite apenas o número que corresponde.')
        print()
        continue
    # #######################################
    print('=-' * 12)
    print()
    if computador == 0: # Computador jogou PEDRA
        if jogador == 0:
            print('\033[1;100m EMPATE \033[m')
        elif jogador == 1:
            print('\033[1;33m JOGADOR VENCEU \033[m 🏆 🎉')
        elif jogador == 2:
            print('\033[1;33m COMPUTADOR VENCEU \033[m 🏆 🎉')
        else:
            print('\033[31m JOGADA INVÁLIDA \033[m')  
    elif computador == 1:
        if jogador == 0:
            print('\033[1;33m COMPUTADOR VENCEU \033[m 🏆 🎉')
        elif jogador == 1:
            print('\033[1;100m EMPATE \033[m')
        elif jogador == 2:
            print('\033[1;33m JOGADOR VENCEU \033[m 🏆 🎉')
        else:
            print('\033[31m JOGADA INVÁLIDA \033[m')
    elif computador == 2: # Computador jogou TESOURA
        if jogador == 0:
            print('\033[1;33m JOGADOR VENCEU \033[m 🏆 🎉')
        elif jogador == 1:
            print('\033[1;33m COMPUTADOR VENCEU \033[m 🏆 🎉')
        elif jogador == 2:
            print('\033[1;100m EMPATE \033[m')
        else:
            print('\033[31m JOGADA INVÁLIDA \033[m')
    print()
    novo = str(input('Jogar novamente? [s/n] ')).lower()
    if novo in 's sim':
        continue
    elif novo in 'n nao':
        break
    