

# Funcion recibe como parametro argumento pizza
def selec_salsa(pizza):
        salsas = ["Salsa de Tomate", "Salsa Alfredo", "Salsa Barbecue", "Salsa Pesto"]
        print("\nTipos de salsa disponibles:")
        for i, salsa in enumerate(salsas, 1):
            print(f"{i}. {salsa}")
        try:
            opcion = int(input("\nSeleccione el tipo de salsa (1-4): "))
            if 1 <= opcion <= 4:
                pizza["salsa"] = salsas[opcion - 1]
                print(f"\nHas seleccionado: {pizza['salsa']}")
            else:
                print("\nOpción inválida")
        except ValueError:
            print("\nPor favor, ingrese un número válido")
            
        return pizza