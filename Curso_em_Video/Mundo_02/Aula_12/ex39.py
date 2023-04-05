from datetime import date

nome = str(input('Olá! Qual o seu nome? ')).title()
nac = int(input(f'Em que ano você nasceu {nome}? '))
ano = date.today().year
idade = ano - nac
if idade < 18:
    print(f'{nome} você ainda vai se alistar.')
    print(f'Falta {18 - idade} anos.')
elif idade == 18:
    print(f'{nome} está na hora de se alistar.')
elif idade > 18:
    print(f'{nome} já passou do tempo de alistamento a {idade - 18} anos.')