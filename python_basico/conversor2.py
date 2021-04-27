dolares = input("Cuantos dolares tienes: ?")
dolares = float(dolares)
valor_mxpesos = 19.86
mx_pesos = round((valor_mxpesos * dolares), 2) //Redondeando a dos decimales el resultado de la conversion
mx_pesos = str(mx_pesos)
print("Tienes $" + mx_pesos + " pesos mexicanos")
