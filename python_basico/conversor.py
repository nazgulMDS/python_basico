pesos = input("Cuantos pesos mexicanos tienes?: ")
pesos = float(pesos)
valor_dolar = 19.86
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dolares")
