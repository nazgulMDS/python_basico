menu = """
Bienvenido al converson de monedas 💰
1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("Cuantos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3634.4
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 2:
    pesos = input("Cuantos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 93.29
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 3:
    pesos = input("Cuantos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 19.86
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
else:
    print("Ingresa una opcion correcta")
