from receta.crear_base import crear_base
from receta.selec_masa import selec_masa
from receta.selec_salsa import selec_salsa
from receta.agregar_ingrediente import agregar_ingrediente
from receta.eliminar_ingrediente import eliminar_ingrediente
from receta.mostrar_selec import mostrar_ingredientes
from receta.tiempo import calcular_tiempo

def menu_principal():
    pizza = crear_base()
    while True:
        print("\n*** MENÚ PIZZERÍA ***")
        print("1. Cambiar tipo de masa")
        print("2. Cambiar tipo de salsa")
        print("3. Agregar ingrediente")
        print("4. Eliminar ingrediente")
        print("5. Ver pizza actual")
        print("6. Confirmar orden")
        print("7. Salir")
        print(pizza)

        try:
            opcion = int(input("\nSeleccione una opción (1-7): "))
            if opcion == 1:
                selec_masa(pizza)
            elif opcion == 2:
                selec_salsa(pizza)
            elif opcion == 3:
                agregar_ingrediente(pizza)
            elif opcion == 4:
                eliminar_ingrediente(pizza)
            elif opcion == 5:
                mostrar_ingredientes(pizza)
            elif opcion == 6:
                tiempo_total = calcular_tiempo(pizza)
                print(f"\nTiempo estimado de preparación: {tiempo_total} minutos")
                mostrar_ingredientes(pizza)
                confirmar = input("\n¿Desea confirmar su orden? (s/n): ").lower()
                if confirmar == 's':
                    print("\n¡Orden confirmada! Gracias por su compra.")
                    break
            elif opcion == 7:
                print("\n¡Gracias por visitarnos!")
                break
            else:
                print("\nOpción inválida")
        except ValueError:
            print("\nPor favor, ingrese un número válido")

if __name__ == "__main__":
    menu_principal()