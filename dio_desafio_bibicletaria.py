#João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. Criar um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida. Uma bicileta pode buzinar, parar e correr. Adicione esses comportamentos!
class Bicicleta:
    def __init__(self, nome, cor, modelo, ano, valor):
        self.nome = nome
        self.cor = cor
        self.modelo = modelo
        self.ano = int(ano)
        self.valor = float(valor)
    
    def buzinar(self):
        print('Trim trim...')
    
    def parar(self):
        print('Parando bicicleta...')
        print('Bicicleta parada.')
    
    def correr(self):
        print('Vrummm...')
        
    def __str__(self):
        return f'{self.nome}: {self.cor}, {self.modelo}, {self.ano}, R${self.valor:.2f}'
        
def main():
    bike_1 = Bicicleta('Bicicleta 1','vermelha', 'Caloi', 2019, 929.90) 
    bike_2 = Bicicleta('Bicicleta 2', 'azul', 'KWS', 2023, 879.50)
    
    print (f'{bike_1.nome}:\nCor - {bike_1.cor}, Marca - {bike_1.modelo}, Ano - {bike_1.ano}, Preço: R${bike_1.valor:.2f}')
    bike_1.buzinar()
    bike_1.parar()
    
    print (f'\n{bike_2}')
    #Bicicleta.correr(bike_2) é equivalente a bike_2.correr()
    Bicicleta.correr(bike_2)
    
if __name__ =='__main__':
    main()