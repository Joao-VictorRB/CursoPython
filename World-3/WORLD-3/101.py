def Voto(ano_nasc):
    import datetime
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nasc

    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 16 >= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'     
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
        
      
ano_nasc = int(input('Digite o ano do seu nascimento: '))
print(Voto(ano_nasc))

# O código recebe o ano de nascimento do usuário, calcula sua idade com base no ano atual e determina a categoria de
# voto: VOTO NEGADO (menos de 18 anos), VOTO OBRIGATÓRIO (18 a 65 anos), ou VOTO OPCIONAL (acima de 65 anos). Ele usa a 
# biblioteca datetime para obter o ano atual e faz a verificação dentro da função Voto.


# The code receives the user's birth year, calculates their age based on the current year, and determines the voting 
# category: VOTO NEGADO (under 18), VOTO OBRIGATÓRIO (18 to 65), or VOTO OPCIONAL (over 65). It uses the datetime library
# to get the current year and performs the check within the Voto function.