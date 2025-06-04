def eliminar_ingrediente(pizza):
        if not pizza["ingredientes"]:                # Verifica si hay elementos para eliminar
            print("\nNo hay ingredientes para eliminar")
            return
        
        print("\nIngredientes actuales:")
        for i, ing in enumerate(pizza["ingredientes"], 1):   # Muestra lista enumerada de los elementos actuales de la lista
            print(f"{i}. {ing}")
        try:
            opcion = int(input("\nSeleccione el ingrediente a eliminar: ")) # Se solicita ingresar el numero del ingrediente a borrar
            if 1 <= opcion <= len(pizza["ingredientes"]):                    # Valida que la opcion este en la lista
                ingrediente = pizza["ingredientes"].pop(opcion - 1)           # Elimina el ingrediente y lo guarda en una variable
                print(f"\nSe eliminó {ingrediente} de tu pizza")
            else:
                print("\nOpción inválida")
        except ValueError:
            print("\nPor favor, ingrese un número válido")   # Maneja el error si el usuario ingresa un valor no numérico
        return pizza   # Devuelve la pizza actualizada