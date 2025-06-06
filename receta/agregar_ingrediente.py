

# Funcion recibe como parametro argumento pizza
def agregar_ingrediente(pizza):
    
    # Lista de ingredientes disponibles para agregar
    ingredientes_disponibles = ["Tomate", "Champiñones", "Aceituna", "Cebolla",    
                            "Pollo", "Jamón", "Carne", "Tocino", "Queso"]
    
    # Muestra los ingredientes disponibles numerados
    print("\nIngredientes disponibles:")                                
    for i, ing in enumerate(ingredientes_disponibles, 1):
        print(f"{i}. {ing}")
    
    try:
        
        # Solicita seleccionar un ingrediente
        opcion = int(input("\nSeleccione el ingrediente a agregar (1-9): ")) 
        
        # Valida que la opción esté dentro del rango válido
        if 1 <= opcion <= 9:        
            ingrediente = ingredientes_disponibles[opcion - 1]
            
            # Verifica si el ingrediente no está en la lista
            if ingrediente not in pizza["ingredientes"]: 
                 
                # Agrega el nuevo ingrediente a la lista
                pizza["ingredientes"].append(ingrediente)
                print(f"\nSe agregó {ingrediente} a tu pizza")
            else:
                print("\nEste ingrediente ya está en tu pizza")
        else:
            print("\nOpción inválida")
            
    # Maneja el error si el usuario ingresa un valor no numérico
    except ValueError:
        print("\nPor favor, ingrese un número válido")     
    
    # Devuelve la pizza actualizada
    return pizza