produto = float(input('Digite o valor do produto: R$'))
print('-=- Selecione a forma de pagamento -=-')
print('''
1- À vista
2- À vista no cartão
3- 2x no cartão
4- 3x ou mais no cartão''')
print('-=-' * 20)
forma = float(input('Selecione uma opção de 1 a 4: '))
if forma == 1:
    desconto = produto * 10 / 100
    print(f'Com pagamento à vista fica R${produto - desconto:.2f} .')
elif forma == 2:
    desconto = produto * 5 / 100
    print(f'Com pagamento à vista no cartão fica R${produto - desconto:.2f} .')
elif forma == 3:
    print(f'Com o pagamento em 2x sem juros fica duas parcelas de R${produto / 3 :.2f} .')
elif forma == 4:
    vezes = int(input('Quantas vezes deseja dividir: '))
    juros = produto * 20 / 100
    produto = produto + juros
    print(f'Com o pagamento em {vezes}x ou mais vezes fica R${produto + juros:.2f} em {vezes}x de R${(produto + juros) / vezes:.2f} ')
else:
    print('\033[31mOpção invalida.\033[m')