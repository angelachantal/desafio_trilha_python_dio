#O desafio consiste em adicionar à função contar_caracteres um dicionário vazio chamado contador para armazenar as contagens de caracteres. Vamos iterar através de cada caractere na string string. Para cada caractere, verifique se ele já está presente no dicionário contador. Se estiver, incremente o valor associado a essa chave. Caso contrário, adicione a chave ao dicionário com valor inicial 1. Neste dicionário, as chaves são os caracteres presentes na string e os valores correspondem à contagem de vezes que cada caractere aparece.

# Entrada: A função espera receber uma única string como entrada. Neste desafio, consideramos como casos de teste apenas strings textuais.

#Saída: A função retorna um dicionário onde cada chave é um caractere presente na string de entrada e o valor associado a cada chave é a quantidade de vezes que o caractere ocorre na string.

def contar_caracteres(string):
#Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.:
    contador = {}
#Itere através de cada caractere na string string.
    for chave in string:
        #Para cada caractere, verifique se ele já está presente no dicionário contador:
        if chave in contador:
            contador[chave] += 1
        else:
            contador[chave] = 1
    return contador

def main():
# Solicita entrada do usuário
    entrada = input()
    resultado = contar_caracteres(entrada)
    print(resultado)

if __name__ == '__main__':
    main()
