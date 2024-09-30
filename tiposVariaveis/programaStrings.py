
nome = "Tony"
sobrenome = "Stark"

nome_completo = nome + " "+ sobrenome

print(nome)
print(sobrenome)
print(nome_completo)

mensagem = f"Meu nome é {nome} e meu sobre nome é {sobrenome}"
print(mensagem) 


versao = "ABC123"
print(versao)

versao += "10"
print(versao)


existe_nome = 'Tony' in mensagem
print(existe_nome)

print(mensagem[0]) #pega a primeira letra da mensagem

print(mensagem[0:6]) #pega um intervalo da frase

print("Lower "+'ABC'.lower())

print("Upper "+'abc'.upper())

print('abc'.find('b'))
print('abc'.replace('b','x'))