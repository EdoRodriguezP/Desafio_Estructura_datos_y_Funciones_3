from receta.base_pizza import crear_base
from receta.tipo_masa import selec_masa
from receta.tipo_salsa import selec_salsa
from receta.agregar_ingrediente import agregar_ingrediente
from receta.eliminar_ingrediente import eliminar_ingrediente
from receta.mostrar_pizza import mostrar_pizza
from receta.tiempo import calcular_tiempo

def menu_principal():
    
    # Crea un diccionario base para la pizza llamando a la función crear_base
    pizza = crear_base()
    
    # Bucle principal que mantiene ejecucion del programa
    while True:
        
        # Se muestran opciones enumeradas
        print("\n*** MENÚ PIZZERÍA ***")
        print("1. Cambiar tipo de masa")
        print("2. Cambiar tipo de salsa")
        print("3. Agregar ingrediente")
        print("4. Eliminar ingrediente")
        print("5. Ver pizza actual")
        print("6. Confirmar orden")
        print("7. Salir")
        

        try:
            # Solicita una opcion y la convierte en entero
            opcion = int(input("\nSeleccione una opción (1-7): "))
            
            # Se usa una serie de condicionales if-elif para manejar las diferentes opciones
            if opcion == 1:
                selec_masa(pizza)
            elif opcion == 2:
                selec_salsa(pizza)
            elif opcion == 3:
                agregar_ingrediente(pizza)
            elif opcion == 4:
                eliminar_ingrediente(pizza)
            elif opcion == 5:
                mostrar_pizza(pizza)
                
            # opcion para confirmar pedido
            elif opcion == 6:
                #Se trae el argumento calcular tiempo y se asigna a  tiempo total
                tiempo_total = calcular_tiempo(pizza)
                print(f"\nTiempo estimado de preparación: {tiempo_total} minutos")
                
                #se imprime pizza a traves de mostrar_pizza
                mostrar_pizza(pizza)
                
                # Se solicita confirmacion de orden con manejo de if
                confirmar = input("\n¿Desea confirmar su orden? (s/n): ").lower()
                if confirmar == 's':
                    print("\n¡Orden confirmada!")
                    break
            # Opcion para salir, imprime y realiza quiebre de bucle
            elif opcion == 7:
                print("\n¡Gracias por visitarnos!")
                break
            else:
                print("\nOpción inválida")
        except ValueError:
            print("\nPor favor, ingrese un número válido")

if __name__ == "__main__":
    menu_principal()