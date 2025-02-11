class Produto:
    def __init__(self,nome,preco,quantidade):
        """Inicializando um produto com nome, preço e quantidade"""
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        """Calcula o valor total do produto"""
        return self.preco * self.quantidade
    def exibir_info(self):
        """Exibe as informações do produto formatadas"""
        return f'Produto: {self.nome} | Preço unitário: R$ {self.preco:.2f} | Quantidade: {self.quantidade} | Total: R$ {self.calcular_total():.2f} '
                
produto1 = Produto('Arroz', 5.50, 3)        # Produto, valor unitário, quantidade
produto2 = Produto('Café', 16.50, 2)        # Café está caro 
produto3 = Produto('Picanha', 89.90, 1)     # Picanhazinha pra o final de semana
produto4 = Produto('Leite em pó', 10.90, 1) # CCGL 200 g

print(produto1.exibir_info())
print(produto2.exibir_info())
print(produto3.exibir_info())
print(produto4.exibir_info())
