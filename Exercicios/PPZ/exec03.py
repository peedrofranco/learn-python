# 3) Escreva um programa que leia a quantidade de dias,
# horas, minutos e segundos do usuário. Calcule o total em segundos.

days = int(input("Informe a quantidade de dias: "))
hours = int(input("Informe a quantidade de horas: "))
minutes = int(input("Informe a quantidade de minutos: "))
seconds = int(input("Informe a quantidade de segundos: "))

dias = days * 24 * 60 * 60
horas = hours * 60 * 60
minutos = minutes * 60
result = dias + horas + minutos + seconds

print(f"{days}d, {hours}h, {minutes}min, {seconds}s => {result}s")
