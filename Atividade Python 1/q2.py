'''Escreva o código usando uma f-string para produzir a seguinte saída,
utilizando as variáveis fornecidas.
Dados:
nome = "João"
saldo = 1500.758'''

nome = "João"
saldo = 1500.758
'''Saida esperada: Olá, João. Seu saldo é 1500.76.'''
print(f"Olá, {nome}. Seu saldo é {saldo:.2f}.")
'''Utilizada a f-string para formatar a saída, limitando o saldo a duas casas decimais.
A f-string foi usada também para inserir a variável nome diretamente na string.
Por conta de tudo isso, a saída ficou exatamente como esperado.'''

