from time import sleep
from random import randint

print('{:-^80}'.format(' {}JOKENPO{} '.format('\033[1;33m', '\033[m')))
print('')
print('Qual sua jogada? ')
print('')
print('{:-^80}'.format(' {}OPÇÕES{} -'.format('\033[1;33m', '\033[m')))

print('''
[ 0 ] PEDRA.
[ 1 ] PAPEL.
[ 2 ] TESOURA. ''')
print('')
jogada = int(input('Dígite sua Opção: '))

if 2 >= jogada >= 0:
    print('')
    print(('{:-^80}'.format(' {}VAMOS JOGAR!!!{} '.format('\033[1;33m', '\033[m'))))
    print('')
    print('{}JO{}'.format('\033[1;31m', '\033[m')), sleep(1)
    print('{}KEN{}'.format('\033[1;31m', '\033[m')), sleep(1)
    print('{}PO!!!{}'.format('\033[1;31m', '\033[m'))
    print('')
    print('-'*70)
    itens = ('Pedra', 'Papel', 'Tesoura'.format('\033[1;35m', '\033[m'))
    computador = randint(0, 2)
    print('')
    print('Você Jogou {}{}{}.'.format('\033[1;32m', itens[jogada], '\033[m'))
    print('')
    print('Eu joguei {}{}{}.'.format('\033[1;31m', itens[computador], '\033[m'))

    if computador == 0:
        print('')
        if jogada == 0:
            print('{}EMPATAMOS!!! (-_-){}'.format('\033[1;33m', '\033[m'))
        elif jogada == 1:
            print('{}GANHOU!!! (-_-){}'.format('\033[1;32m', '\033[m'))
        elif jogada == 2:
            print('{}PERDEU!!! (; w ;){}'.format('\033[1;31m', '\033[m'))

    elif computador == 1:
        print('')
        if jogada == 0:
            print('{}PERDEU!!! (; w ;){}'.format('\033[1;31m', '\033[m'))
        elif jogada == 1:
            print('{}EMPATAMOS!!! (-_-){}'.format('\033[1;33m', '\033[m'))
        elif jogada == 2:
            print('{}GANHOU!!! (-_-){}'.format('\033[1;32m', '\033[m'))

    elif computador == 2:
        print('')
        if jogada == 0:
            print('{}GANHOU!!! (-_-){}'.format('\033[1;32m', '\033[m'))
        elif jogada == 1:
            print('{}PERDEU!!! (; w ;){}'.format('\033[1;31m', '\033[m'))
        elif jogada == 2:
            print('{}EMPATAMOS!!! (-_-){}'.format('\033[1;33m', '\033[m'))

else:
    print('-'*70)
    print('')
    print('{}Jogada Inválida. Tente Novamente.{}'.format('\033[1;31m', '\033[m'))
print('')
print('-' * 70)
