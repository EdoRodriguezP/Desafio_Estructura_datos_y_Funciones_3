def selec_masa(pizza):
    masas = ["Masa Tradicional", "Masa Delgada", "Masa con Bordes de Queso"]
    print("\nTipos de masa disponibles:")
    for i, masa in enumerate(masas, 1):  # Comenzar enumeración desde 1
        print(f"{i}. {masa}")
    
    try:
        opcion = int(input("\nSeleccione el tipo de masa (1-3): "))
        if 1 <= opcion <= 3:
            pizza["base"] = masas[opcion - 1]
            print(f"Base de {pizza['base']} agregada correctamente...")
        else:
            print("Opción no válida")
    except ValueError:
        print("\nPor favor, ingrese un número válido")
    
    return pizza