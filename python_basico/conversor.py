def converson(tipo_pesos, valor_dolar):
       pesos = input("Cuantos pesos " + tipo_pesos + " tienes?: ")
       pesos = float(pesos)
       dolares = pesos / valor_dolar
       dolares = round(dolares, 2)
       dolares = str(dolares)
       print("Tienes $" + dolares + " dolares")


menu = """
Bienvenido al converson de monedas 💰
1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    converson("colombianos", 3875)
elif opcion == 2:
    converson("argentinos", 65)
elif opcion == 3:
    converson("mexicanos", 19.86)
else:
    print("Ingresa una opcion correcta")
