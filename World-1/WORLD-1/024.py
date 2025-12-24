print('Digite o nome de uma cidade: ',end='')
r = input().upper().split()

check = 'SANTO' in r [0]

print('A cidade começa com Santo: {}'.format(check))