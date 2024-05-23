"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número: ')
try:
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'impar'
    
    if par_impar:
        par_impar_texto = 'par'
        
    print(f'O número {numero_int} é {par_impar_texto}.')

except:
    print('Você não digitou um número inteiro!')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = input('Digite um horário (0-23): ')

try:
    horario = int(horario)
    
    if horario>=0 and horario<=11:
        print('Bom dia!')
    
    elif horario >= 12 and horario <= 17:
        print('Boa tarde!')
    
    elif horario >= 18 and horario <= 23:
        print('Boa noite!')

    else:
        print(f'Não conheço essa hora {horario}!')
    
except:
    print(f'{horario} não é um valor inteiro!')

    
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu nome: ')
if len(nome) <= 4:
    print(f'Seu nome {nome} tem um tamanho curto.')
elif len(nome) <= 6:    
    print(f'Seu nome {nome} tem um tamanho normal.') 
else:
    print(f'Seu nome {nome} tem um tamanho grande.')