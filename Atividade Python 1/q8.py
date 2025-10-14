'''Q8: Crie um programa que receba o preço total da compra (float) e o
valor pago pelo cliente (float). O programa deve calcular e imprimir o
troco devido ao cliente, formatado com duas casas decimais. Utilize
um operador aritmético para o cálculo.'''

def main():
    total = float(input("Digite o preço total da compra: "))
    pago = float(input("Digite o valor pago pelo cliente: "))

    troco = pago - total

    print(f"O troco devido ao cliente é: R$ {troco:.2f}")
if __name__ == "__main__":
    main()
''' O usuário insere o preço total da compra e o valor pago pelo cliente,
    ambos como números no formato float. Em seguida, o programa calcula o troco
    subtraindo o preço total do valor pago. Após o cálculo, o programa imprime o troco formatado com duas casas decimais,
    utilizando uma f-string para garantir a formatação correta.
'''

