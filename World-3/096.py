def área(largura, comprimento):
    area_terreno = largura * comprimento
    print(f'A área de um terreno {largura} X {comprimento}: {area_terreno} m²')


largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))

área(largura, comprimento)

# O código define uma função chamada área que calcula a área de um terreno retangular com base na largura e no comprimento
# fornecidos. O usuário é solicitado a inserir os valores de largura e comprimento via teclado, e a função exibe a área
# calculada no formato "A área de um terreno largura X comprimento: área m²".


# The code defines a function called área that calculates the area of a rectangular plot based on the given width and 
# length. The user is prompted to input the width and length values via the keyboard, and the function displays the
# calculated area in the format "The area of a plot width X length: area m²".