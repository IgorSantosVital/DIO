from datetime import date

# # TODO: Crie a Classe Veiculo e armazene sua marca, modelo e ano como atributos:
# class Veiculo:
#   # TODO: Implemente o método verificar_antiguidade e calcule a diferença entre o ano atual e o ano do veículo:
#     def __init__(self, marca, modelo, ano):
#       self.marca = marca
#       self.modelo = modelo
#       self.ano = ano

#     def verificar_antiguidade(self):
#       ano_atual = date.today().year
#       idade = ano_atual - self.ano
#       if idade > 20:
#         antiguidade = "Veículo antigo"
#       else:
#         antiguidade = "Veículo novo"
          
#       return antiguidade
    
    

# # Entrada direta
# marca = input().strip()
# modelo = input().strip()
# ano = int(input().strip())

# # Instanciando o objeto e verificando a antiguidade
# veiculo = Veiculo(marca, modelo, ano)
# print(veiculo.verificar_antiguidade())


class Pedido: 
    def __init__(self): 
        self.itens = []   
    
    # Cria um método para adicionar o preço do item
    def adicionar_item(self, preco):
        self.itens.append(preco)
          
    # Cria um método para calcular o total dos itens
    def calcular_total(self):
        return sum(self.itens)
        

quantidade_pedidos = int(input().strip())

pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)  # separa o nome do item e o preço
    pedido.adicionar_item(float(preco))   # adiciona o preço convertido para float

# Exibe o total formatado com duas casas decimais
print(f"Total: R$ {pedido.calcular_total():.2f}")
