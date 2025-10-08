'''Q9: Crie um programa que peça ao usuário para digitar seu nome, peso
e altura. Calcule e imprima o nome e o IMC.'''

def main():
    nome = input("Digite seu nome: ")
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = peso / (altura ** 2)

    if imc < 18.5:
        return print(f"{nome}, seu IMC é {imc:.2f}. Você está com peso baixo.")
    elif 18.5 <= imc < 24.9:
        return print(f"{nome}, seu IMC é {imc:.2f}. Você está com peso normal.")
    elif 25 <= imc < 29.9:
        return print(f"{nome}, seu IMC é {imc:.2f}. Você está com sobrepeso.")
    elif 30 <= imc < 34.9:
        return print(f"{nome}, seu IMC é {imc:.2f}. Você está com obesidade grau I.")
    elif 35 <= imc < 39.9:
        return print(f"{nome}, seu IMC é {imc:.2f}. Você está com obesidade grau II.")
    else:
        return print(f"{nome}, seu IMC é {imc:.2f}. Você está com obesidade grau III.")
if __name__ == "__main__":
    main()
''' O programa começa solicitando ao usuário que insira seu nome, peso e altura.
O nome é armazenado como uma string, enquanto o peso e a altura são convertidos para float
para permitir cálculos precisos.

Em seguida, o IMC é calculado usando a fórmula: IMC = peso / (altura ** 2).
O programa então avalia o valor do IMC com a declaração if-elif-else para determinar a categoria de peso do usuário.
Dependendo do valor do IMC, o programa imprime uma mensagem personalizada,
com o nome do usuário, o valor do IMC formatado com duas casas decimais e a categoria de peso correspondente.'''