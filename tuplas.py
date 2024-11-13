#Desenvolva uma função em Python que recebe uma tupla de números inteiros e retorna a soma de todos os elementos dessa tupla. A função deve ser capaz de lidar com tuplas de qualquer tamanho, contanto que todos os elementos sejam números inteiros. O objetivo é praticar a manipulação de tuplas e a utilização de funções em Python.

#A entrada para o seu programa será uma única linha de texto contendo vários números inteiros separados por espaços. Esses números devem ser lidos e convertidos para uma tupla de inteiros.
#1. Converta cada string na "lista_strings" em um número inteiro utilizando a função "int()".
#2. Use a função "map()" para aplicar a função "int()" a cada elemento da "lista_strings".
#3. Armazene o resultado em uma variável.

#Exiba a soma do valor calculado no formato: A soma dos elementos da tupla é: <soma>

def somar_tupla(numeros):
    tupla = map(int, numeros.split())
    
    return sum (tupla)
    
    #return sum(tupla)
    
def main():
  numeros = input()
  
  resultado = somar_tupla(numeros)
  print(f"A soma dos elementos da tupla é: {resultado}")
    
if __name__ == "__main__":
  main()