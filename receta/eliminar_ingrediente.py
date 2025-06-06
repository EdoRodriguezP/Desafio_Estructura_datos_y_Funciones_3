

# Funcion recibe como parametro argumento pizza
def eliminar_ingrediente(pizza):

        # Verifica si hay elementos para eliminar
        if not pizza["ingredientes"]:               
            print("\nNo hay ingredientes para eliminar")
            return
        
        # Muestra ingrtedientes acuales
        print("\nIngredientes actuales:")
        
        # Itera sobre lista para enumerar los elementos actuales de la lista y la muestra
        for i, ing in enumerate(pizza["ingredientes"], 1):   
            print(f"{i}. {ing}")
            
        try:
            
            # Se solicita ingresar el numero del ingrediente a borrar
            opcion = int(input("\nSeleccione el ingrediente a eliminar: ")) 
            
            # Valida que la opcion este en la lista
            if 1 <= opcion <= len(pizza["ingredientes"]):
                
                # Elimina el ingrediente y lo guarda en una variable            
                ingrediente = pizza["ingredientes"].pop(opcion - 1)           
                print(f"\nSe eliminó {ingrediente} de tu pizza")
            else:
                print("\nOpción inválida")
                
        # Maneja el error si el usuario ingresa un valor no numérico
        except ValueError:
            print("\nPor favor, ingrese un número válido") 
            
        # Devuelve la argumento pizza actualizada     
        return pizza 