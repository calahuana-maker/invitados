invitados = {}

def mostrar_menu():
    print('1. Registrar el nombre de un invitado, su género y carrera')
    print('2. Ver todos los nombres de los invitados')
    print('3. Eliminar el registro de un invitado')
    print('4. Ver un gráfico con géneros de los invitados')
    print('5. Ver un grafico con la carrera de los invitados')

def input_int(promt):
    while True:
        try:
            valor = int(input(promt))
            if valor > 0:
                return
            else:
                print('Valor invalido. Intente de nuevo')
        except ValueError:
            print('Valor invalido. Intente de nuevo')

def registrar():
    nombre = input('Ingrese el nombre del invitado: ')
    genero = input('Ingrese el género del invitado: ')
    carrera = input('Ingrese la carrera del invitado: ')

    invitados[nombre] = genero,carrera