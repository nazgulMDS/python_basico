import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegigo = int(input('Elige un numero del 1 al 100: '))
    while numero_elegigo != numero_aleatorio:
        if numero_elegigo < numero_aleatorio:
            print('Busca un numero mas grande')
        else:
            print('Busca un numero mas pequenio')
        numero_elegigo = int(input('Elige otro numero: '))
    print('Ganaste!')
    


if __name__ =='__main__':
    run()
