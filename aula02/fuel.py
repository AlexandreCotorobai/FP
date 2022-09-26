litros = float(input('Quantos litros para abastecer? '))

if litros <= 40:
    custo = litros * 1.40
else:
    custo = (litros * 1.40) * 0.9

print(custo)