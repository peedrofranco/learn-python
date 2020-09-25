# 2. Determine se um ano é bissexto. Verifique no Google como fazer isso...

a = int(input('Ano: '))
if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
    print('Bissexto')
else:
    print('Não é bissexto')
