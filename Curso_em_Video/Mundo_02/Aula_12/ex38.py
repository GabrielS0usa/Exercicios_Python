print('Digite dois números e eu vou te falar o maior.')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print(f'O primeiro número é o maior.')
elif n2 > n1:
    print(f'O segundo número é o maior.')
elif n1 == n2:
    print('Não tem um número maior, os dois são iguais.')