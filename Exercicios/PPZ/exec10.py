# 10) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de
# cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a
# cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

cigarros = int(input('Cigarros por dia: '))
anos = int(input('Anos fumados: '))
total_cigarros = anos * 365 * cigarros
dias_perdidos = total_cigarros / 144
print(f'Você perdeu aproximadamente {dias_perdidos} dias')
