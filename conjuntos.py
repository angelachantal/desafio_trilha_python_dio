#Desenvolva uma função que receba duas listas de números inteiros separados por espaço e retorne uma lista contendo apenas os elementos que são comuns a ambas as listas, sem duplicatas.

#Função elementos_comuns:
# 1. Crie a função que converte cada elemento das listas lista1 e lista2 para inteiro usando map(int, lista) antes de convertê-los em conjuntos (set) e encontrar a interseção entre eles. Isso garante que tratemos os elementos corretamente como números inteiros e não como strings.

#Entrada: Duas listas de inteiros separados apenas por espaço, por exemplo: 1 2 3 4 e 3 4 5 6.

#Saída: Uma lista com os elementos comuns, por exemplo: [3, 4]. Caso a entrada seja diferente do esperado, retorne: "Entrada inválida."

def elementos_comuns(lista1, lista2):
    lista1 = map(int, lista1)
    lista2 = map(int, lista2)
    lista1 = set(lista1)
    lista2 = set(lista2)
   
    return list(lista1.intersection(lista2))

def main():
    # Leitura das listas
    lista1 = input().split()
    lista2 = input().split()

    # Verifica se todas os elementos das listas podem ser convertidos para inteiros
    if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2): 
        comuns = elementos_comuns (lista1, lista2)
        print(f"Elementos comuns às duas listas: {comuns}")
    else:
        print("Entrada inválida.")
        
if __name__ == '__main__':
    main()