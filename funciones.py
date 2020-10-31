from typing import Tuple
import aproximacion_soluciones as aps
import busqueda_binaria as bb
import enumeracion_exhaustiva as ee


def Menu():
    print("==================================")
    print("= Algorimo a utilizar            =")
    print("= 1.- Aproximacion de soluciones =")
    print("= 2.- Busqueda binaria           =")
    print("= 3.- Enumeracion exhaustiva     =")
    print("==================================")


fin = False
while fin != True:
    Menu()
    tipo_algoritmo = int(input("Que tipo de algoritomo desea usar: "))
    objetivo = int(input("Ingrese el numero a calcular: "))
    if tipo_algoritmo == 1:
        print(aps.aproximacionSoluciones(objetivo))
    elif tipo_algoritmo == 2:
        print(bb.busquedaBinaria(objetivo))
    elif tipo_algoritmo == 3:
        print(ee.enumeracionExhaustiva(objetivo))
    else:
        print(f'{tipo_algoritmo} no es un valor valido')
        break
    fin = bool(int(input("Desea calcular otro numero?[0->No/1->Si]: ")) == 0)