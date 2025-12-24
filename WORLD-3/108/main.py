import moeda

p = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.padraoMonetario(p)} é {moeda.padraoMonetario(moeda.metade(p))}')
print(f'O dobro de {moeda.padraoMonetario(p)} é {moeda.padraoMonetario(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.padraoMonetario(moeda.aumentar(p,10))}')
