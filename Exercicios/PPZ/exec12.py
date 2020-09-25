# 1. Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os
# valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero,
# isósceles ou escaleno.

a = int(input('Lado a: '))
b = int(input('Lado b: '))
c = int(input('Lado c: '))
if a > b + c or b > a + c or c > a + b:
    print('Não pode ser um triângulo')
    print('Um dos lados é maior que a soma dos outros')
elif a == b == c:
    print('Equilátero')
elif a == b or b == c or a == c:
    print('Isósceles')
else:
    print('Escaleno')
