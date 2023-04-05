print('Vamos calcular a sua média de notas.')
nome = str(input('Qual é o seu nome? ')).title()
n1 = float(input('Digite a nota n1: '))
n2 = float(input('Digite a nota n2: '))
med = (n1 + n2) / 2
if med < 5.0:
    print(f'{nome} você tirou {med:.1f} está reprovado!')
elif med >= 5.0 and med <= 6.9:
    print(f'{nome} você tirou {med:.1f} está de recuperação!')
elif med >= 7.0:
    print(f'{nome} voc ê tirou {med:.1f} está aprovado!')