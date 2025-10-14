''' Q6: Crie um programa que solicite ao usuário
a. Duas notas(float)
b. Dois pesos(int)
O programa deve calcular e imprimir a média ponderada das notas.
Fórmula: media = (n1*p1) + (n2*p2) / (p1 + p2)
'''

def main():
    n1 = float(input("Digite a primeira nota: "))
    p1 = int(input("Digite o peso da primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    p2 = int(input("Digite o peso da segunda nota: "))

    media = (n1 * p1 + n2 * p2) / (p1 + p2)

    print(f"A média ponderada é: {media:.2f}")

if __name__ == "__main__":
    main()
''' O usuário digita a 
primeira nota e em seguida 
o peso da mesma, e assim segue na segunda nota
Após a entrada dos dados, o cálulo da média é feito de acordo com
a fórmula dada e o
resultado é exibido com duas casas decimais.'''
