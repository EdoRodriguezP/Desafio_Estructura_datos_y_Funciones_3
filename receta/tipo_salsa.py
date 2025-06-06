

# Funcion recibe como parametro argumento pizza
def selec_salsa(pizza):
    
        # Se crea lista masas 
        salsas = ["Salsa de Tomate", "Salsa Alfredo", "Salsa Barbecue", "Salsa Pesto"]
        print("\nTipos de salsa disponibles:")
        
        # Se itera sobre masa comenzando en 1 se imprime en orden
        for i, salsa in enumerate(salsas, 1):
            print(f"{i}. {salsa}")
        try:
            
            # Se solicita el ingreso de una opcion
            opcion = int(input("\nSeleccione el tipo de salsa (1-4): "))
            
            # si opcion es valida 
            if 1 <= opcion <= 4:
                
                # Asigna la masa seleccionada al diccionario usano la clave base
                pizza["salsa"] = salsas[opcion - 1]
                print(f"\nHas seleccionado: {pizza['salsa']}")
            else:
                print("\nOpción inválida")
                
        # Maneja el error si el usuario ingresa un valor no numérico
        except ValueError:
            print("\nPor favor, ingrese un número válido")
            
        return pizza