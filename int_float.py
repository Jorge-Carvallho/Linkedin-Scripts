# Exemplos práticos de int e float no Python

# Inteiros (int)
inteiro_positivo = 12345
inteiro_negativo = -10
print(f'Inteiro positivo: {inteiro_positivo}')
print(f'Inteiro negativo: {inteiro_negativo}')
print('-' * 50)

# Ponto flutuante (float)
ponto_flutuante_positivo = 3.14
ponto_flutuante_negativo = -0.08
print(f'Float positivo: {ponto_flutuante_positivo}')
print(f'Float negativo: {ponto_flutuante_negativo}')
print('-' * 50)

# Conversão entre int e float
numero_inteiro = 10
numero_convertido = float(numero_inteiro)  # Converte int para float
print(f'Convertendo int para float: {numero_inteiro} -> {numero_convertido}')
print('-' * 50)

numero_float = 9.99
numero_convertido = int(numero_float)  # Converte float para int
print(f'Convertendo float para int: {numero_float} -> {numero_convertido}')
print('-' * 50)

# Métodos úteis
# round(): Arredonda um número float
numero_arredondado = round(3.567)
print(f'Arredondando 3.567 =  {numero_arredondado}')
print('-' * 50)

# abs(): Retorna o valor absoluto de um número
valor_absoluto = abs(-10)
print(f'Valor absoluto de -10: {valor_absoluto}')
print('-' * 50)

# pow(): Calcula a potência de um número
potencia = pow(2, 3)
print(f'2 elevado a 3 = {potencia}')
print('-' * 50)

# divmod(): Retorna o quociente e o resto de uma divisão
quociente, resto = divmod(9, 4)
print(f'Divisão de 9 por 4: quociente = {quociente}, resto = {resto}')
print('-' * 50)

# Aviso sobre a precisão dos floats
print("Cuidado com a precisão dos floats! \nPara cálculos precisos, considere usar bibliotecas como 'decimal' ou 'fractions'.")
