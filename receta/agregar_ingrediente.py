def agregar_ingrediente(pizza):

    ingredientes_disponibles = ["Tomate", "Champiñones", "Aceituna", "Cebolla",    # Lista de ingredientes disponibles para agregar
                            "Pollo", "Jamón", "Carne", "Tocino", "Queso"]
    
    
    print("\nIngredientes disponibles:")                                # Muestra los ingredientes disponibles numerados
    for i, ing in enumerate(ingredientes_disponibles, 1):
        print(f"{i}. {ing}")
    
    try:
        
        opcion = int(input("\nSeleccione el ingrediente a agregar (1-9): ")) # Solicita seleccionar un ingrediente
        
        
        if 1 <= opcion <= 9:        # Valida que la opción esté dentro del rango válido
            ingrediente = ingredientes_disponibles[opcion - 1]
            
            
            if ingrediente not in pizza["ingredientes"]:      # Verifica si el ingrediente no está en la lista
                
                pizza["ingredientes"].append(ingrediente)       # Agrega el nuevo ingrediente a la lista
                print(f"\nSe agregó {ingrediente} a tu pizza")
            else:
                print("\nEste ingrediente ya está en tu pizza")
        else:
            print("\nOpción inválida")
    except ValueError:
        print("\nPor favor, ingrese un número válido")     # Maneja el error si el usuario ingresa un valor no numérico
    
    # Devuelve la pizza actualizada
    return pizza