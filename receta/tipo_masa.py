
# Funcion recibe como parametro argumento pizza
def selec_masa(pizza):
    
    # Se crea lista masas 
    masas = ["Masa Tradicional", "Masa Delgada", "Masa con Bordes de Queso"]
    print("\nTipos de masa disponibles:")
    
    # Se itera sobre masa comenzando en 1 se imprime en orden
    for i, masa in enumerate(masas, 1):  
        print(f"{i}. {masa}")
    
    try:
        # Se solicita el ingreso de una opcion
        opcion = int(input("\nSeleccione el tipo de masa (1-3): "))
        
        # si opcion es valida 
        if 1 <= opcion <= 3:
            
            # Asigna la masa seleccionada al diccionario usano la clave base
            pizza["base"] = masas[opcion - 1]
            print(f"Base de {pizza['base']} agregada correctamente...")
        else:
            print("Opción no válida")
            
    # Maneja el error si el usuario ingresa un valor no numérico
    except ValueError:
        print("\nPor favor, ingrese un número válido")
    
    return pizza