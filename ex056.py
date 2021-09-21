"""Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""
soma = 0
media = 0
cont_idade_m = 0
idade_h = 0
nome_h = 0
for c in range(1, 5):
    print('{}-={}'.format('\033[1;33m', '\033[m') * 35)
    nome = str(input('Dígite o seu Nome: ')).strip().upper()
    print('''{}Selecione as Opções:{}
{}[ 1 ]{} Masculino
{}[ 2 ]{} Feminino'''.format('\033[1;31m', '\033[m', '\033[1;34m', '\033[m', '\033[1;34m', '\033[m'))
    sexo = int(input('Dígite seu Sexo: '))
    idade = int(input('Dígite sua Idade: '))

    if sexo == 1 and idade > idade_h:
        idade_h = idade
        nome_h = nome

    else:
        if sexo == 2 and idade < 20:
            cont_idade_m += 1

    soma += idade
    media = soma / c

print('{}-={}'.format('\033[1;33m', '\033[m') * 35)
print('{:^75}'.format('{}ANÁLISE DE DADOS{}'.format('\033[1;31m', '\033[m')))
print('{}-={}'.format('\033[1;33m', '\033[m') * 35)
print('')
print('De acordo com os dados coletados a {}MÉDIA DE IDADE DO GRUPO{} é\n'
      'de {}{:.1f}{} anos.'.format('\033[1;34m',
                                   '\033[m',
                                   '\033[1;34m',
                                   media, '\033[m'))
print('')
print('De acordo com os dados coletados, {}{}{} mulher(es) possui(uem)\n'
      'menos de 20 anos de idade.'.format('\033[1;34m', cont_idade_m, '\033[m'))
print('')
print('O {}{}{} é o homem mais velho com {}{}{} anos de idade.'.format('\033[1;32m', nome_h, '\033[m',
                                                                       '\033[1;34m', idade_h, '\033[m'))
print('')
print('{}-={}'.format('\033[1;33m', '\033[m') * 35)
