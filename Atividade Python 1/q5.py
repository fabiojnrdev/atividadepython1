# Q5: Determine o valor final da variável check
a = 10
b = 5
c = 15
check = (a > b and c < b) or not (c==15)
print(check)
# A saída será False por conta das expressões lógicas.
# A expressão (a > b and c < b) é False porque c não é menor que b.
# A expressão not (c==15) é False porque c é igual a 15.