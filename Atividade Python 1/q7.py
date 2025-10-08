'''Q7: Escreva um programa que receba um valor de tempo em minutos
(como int) e o converta para horas e minutos. O programa deve
imprimir o resultado formatado. Exemplo: Se o usuário digitar 150
minutos, a saída deve ser "2 horas e 30 minutos".'''

def main():
    total_minutos = int(input("Digite o tempo em minutos: "))

    horas = total_minutos // 60
    minutos = total_minutos % 60

    print(f"{horas} horas e {minutos} minutos")
if __name__ == "__main__":
    main()
''' O usuário insere um valor inteiro para representar 
os minutos, logo após isso, o cálculo de horas, 
que é  a divisão inteira por 60, e o dos minutos, que é o 
resto da divisão por 60, ambos realizados usando operadores aritiméticos.
''' 
'''Após os cálculos, o programa imprime
 o resultado no formato solicitado.'''