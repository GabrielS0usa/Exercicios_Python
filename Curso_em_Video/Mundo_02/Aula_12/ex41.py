idade = int(input('Digite a idade do atleta: '))
if idade <= 9:
    print('É um atleta mirim')
elif idade > 9 and idade <= 14:
    print('É um atleta infantil')
elif idade > 14 and idade <= 19:
    print('É um atleta junior')
elif idade == 20:
    print('É um atleta sênior')
else:
    print('É um atleta master')