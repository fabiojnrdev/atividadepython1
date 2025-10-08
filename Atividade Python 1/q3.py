''' Q3: Explique por que o seguinte código resultará em um erro de
TypeError e sugira a correção.'''

'''
Dados:
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
soma = num1 + num2
print(soma)'''

# O código até executa, mas o resultado é concatenação de strings, não a soma de um inteiro de fato.
# A correção seria converter as entradas para inteiros, e depois disso a soma seria feita corretamente:
def main():
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo número: "))
    soma = num1 + num2
    print(soma)
if __name__ == "__main__":
    main()
# A função main criada é a forma correta de estrutura desse código.