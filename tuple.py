# Criando tuplas de diferentes formas
tupla_sem_parenteses = 4, 5, 6  # Tupla sem parênteses
tupla1 = (1, 2, 3)               # Tupla com parênteses
tupla2 = (5,)                    # Tupla de um único elemento

# Exibindo as tuplas
print('Tupla sem parênteses:', tupla_sem_parenteses)
print('Tupla 1:', tupla1)
print('Tupla 2:', tupla2)
print('-'* 60)

# Verificando a imutabilidade
try:
    tupla1[0] = 10  # Tentativa de alterar um elemento da tupla
except TypeError as e:
    print('Erro:', e)
    
print('-'* 60)

# Usando métodos de tupla
tupla3 = (1, 2, 2, 3, 3, 3)
print('Contagem do número 2 na tupla3:','existem --> ', tupla3.count(2), 'números 2 na tupla3')
print('Índice do primeiro número 3 na tupla3:','índice --> ', tupla3.index(3))
print('-'* 60)

# Exemplos de tuplas com diferentes tipos de dados
tupla_mista = (1, 'Python', 3.14, (1, 2))
print('Tupla mista:', tupla_mista)

print('\nFique de olho e continue acompanhando! ')
