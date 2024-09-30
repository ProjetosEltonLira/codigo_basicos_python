import json 

# Dados é uma string
dados = """ 
    {
        "nome": "Nome da Pessoa",
        "endereco": "Rua buriti 134",
        "cpf" :"123.345.987-90",
        "casado": true, 
        "imoveis": [
            "casa",
            "sítio"
        ],
        "idade": 65       
    }   
"""
pessoa = json.loads(dados) #Converte uma String em Json usando a biblioteca


print(dados)
print(type(dados))

print(pessoa)
print(type(pessoa))
print(pessoa['nome'],pessoa['endereco'])


#transformar uma dicionario em Json
info = {'qtd_ec2': 5, 'type_ec2': 't3a.micro', 'ligado': True}
info_json = json.dumps(info)

print(info)
print(type(info))

print(info_json)
print(type(info_json))





