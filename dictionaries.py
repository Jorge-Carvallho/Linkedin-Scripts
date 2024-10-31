# Exemplo de criação de um dicionário simples
idades = {
    'João': 28,
    'Maria': 32,
    'Pedro': 25
}
#Exibindo dicionário
print(idades)
print('-'* 60)

# Exibindo todas as chaves do dicionário
print('Chaves:', idades.keys())
print('-'* 60)
# Exibindo todos os valores do dicionário
print('Valores:', idades.values())
print('-'* 60)

# Exibindo cada par chave-valor como uma tupla
print('Pares chave-valor:', idades.items())
print('-'* 60)

# Acessando o valor associado a uma chave específica
idade_joao = idades.get('João')
print('Idade do João:', idade_joao)
print('-'* 60)

# Adicionando uma nova chave-valor ao dicionário
idades["Ana"] = 29
print('Novo dicionário com Ana:', idades)
print('-'* 60)

# Modificando um valor no dicionário
idades["Pedro"] = 26
print('Dicionário após modificar a idade do Pedro:', idades)
print('-'* 60)

# Removendo uma chave-valor do dicionário
del idades["Maria"]
print('Dicionário após remover Maria:', idades)
