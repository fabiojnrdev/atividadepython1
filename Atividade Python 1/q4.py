'''Q4: Qual será o valor e o tipo de w no final da execução?'''
a = "3.5"
b = 2
w = int(float(a)) + b + 0.5
print(w)
'''Saída: 5.5
A variável 'a' é uma string que representa um número decimal (3.5).
A função float(a) converte a string 'a' em um número de ponto flutuante (3.5).
A função int(float(a)) converte o número de ponto flutuante (3.5) em um número inteiro (3), descendo a parte decimal.
Em seguida, somamos esse inteiro (3) com a variável 'b' (2) e 0.5.
Portanto, a soma é 3 + 2 + 0.5, que resulta em 5.5.'''
