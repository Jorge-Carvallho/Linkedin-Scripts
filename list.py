# Exemplo prático de alguns métodos citados em listas.
minha_lista = [1, 'Python', 3.14, True]
print('Minha lista: ',minha_lista)
print('-'* 50)

# Adicionando um item ao final da lista (append)
minha_lista.append('Novo item')
print('Depois do append:', minha_lista)
print('-'* 50)

# Removendo a primeira ocorrência de um valor específico (remove)
minha_lista.remove(True)  # Remove o valor True
print('Depois do remove:', minha_lista)
print('-'* 50,)

# Removendo e retornando o último item da lista (pop)
ultimo_item = minha_lista.pop()
print('Depois do pop:', minha_lista)
print('Item removido:', ultimo_item)
print('-'* 50)

# Ordenando uma lista de números (sort)
numeros = [5, 3, 8, 1, 2]
print('Minha lista númerica desordenada:', numeros)
numeros.sort()
print('Lista ordenada:', numeros)
print('-'* 50)

# Invertendo a ordem dos elementos (reverse)
numeros.reverse()
print('Lista invertida:', numeros)
print('-'* 50)

# Obtendo a posição de um item na lista (index)
indice = minha_lista.index('Python')
print('Índice de "Python":', indice)
print('-'* 50)

# Inserindo um item em uma posição específica (insert)
# observação ----> minha_lista.insert(posicao, item) =  1ª é a posição do item, 2ª é o item
minha_lista.insert(1, 'Novo Elemento') #exemplo: indice 1 adicionar 'Novo Elemento'
print('Depois do insert:', minha_lista)
print('-'* 50)

# Adicionando os elementos de outra lista (extend)
outra_lista = [10, 20, 30]
print('Minha lista é essa:', minha_lista)
minha_lista.extend(outra_lista)
print('A outra lista é essa:', outra_lista)
print('Depois do extend:', minha_lista)
