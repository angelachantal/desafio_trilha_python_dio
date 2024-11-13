 #João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode: buzinar, parar e correr.

class Bicicleta:
    def __init__(self, modelo, cor, ano, valor):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print ('Fom! Fom!')

    def parar(self):
        print ('Bicicleta parada')

    def correr(self):
        print ('Vrumm!')

def main():
    modelo = None
    cor = None
    ano = None
    valor = None
    bicicleta1 = Bicicleta (input('Modelo: '), input('Cor: '), input('Ano: '), input('Valor: '))

    print (bicicleta1.modelo, bicicleta1.cor, bicicleta1.ano, bicicleta1.valor)

    acao = input ('O que a bibicleta faz? (B - buzinar, P - parar, C - correr) ').upper()
    if acao == 'B':
        bicicleta1.buzinar()
    elif acao == 'P':
        bicicleta1.parar()
    elif acao == 'C':
        bicicleta1.correr()
    else:
        print ("Ação inválida")
               
if __name__ == '__main__':
    main()