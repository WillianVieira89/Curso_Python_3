nome = input('Qual é o seu nome? ')
idade = input('Qual é a sua idade? ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Sua idade é {idade}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome tem espaços')
    else:
        print('Seu nome NÃO tem espaços')

    print('Seu nome tem ' f'{len(nome)}'  ' letras')
    print('A primeira letra do seu nome é ' f'{nome[0]}')
    print('A ultima letra do seu nome é ' f'{nome[-1]}')
else:
    print('Desculpe voce deixou campos vazios')
    