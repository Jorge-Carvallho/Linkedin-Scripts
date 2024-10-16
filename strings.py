# Imutabilidade
# Uma vez criada, a string não pode ser alterada diretamente.
minha_string = 'Python'
print('String original:', minha_string)
print('-' * 50)

# Tentativa de modificação (não vai funcionar):
# Em vez disso, criamos uma nova string:
nova_string = 'J' + minha_string[1:]
print('Nova string após modificação:', nova_string)
print('-' * 50)

# Métodos úteis 
string_exemplo = 'Aprendendo Python!'
print('Em maiúsculas:', string_exemplo.upper())
print('Substituindo "Python" por "Programação":', string_exemplo.replace('Python', 'Programação'))
print('Separando palavras:', string_exemplo.split())
print('-' * 50)

# Formatação e Interpolação 
nome = 'Elon'
linguagem = 'Python'
print(f'Olá, {nome}, você está aprendendo {linguagem}!')  
print('-' * 50)

# Suporte para slices 
minha_string = 'Manipulação de strings'
print('Slice [0:11] = ', minha_string[0:11])
print('-' * 50) 

# Curiosidade 
# Toda string em Python é um objeto da classe str, que possui várias funcionalidades para manipulação de texto.
print('Classe de uma string:', type(minha_string))
print('-' * 50)

print('Strings são objetos poderosos e otimizados em Python!')
