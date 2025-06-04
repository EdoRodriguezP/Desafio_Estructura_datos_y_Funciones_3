def mostrar_pizza(pizza):
        print("\nTu pizza actual:")
        print(f"Masa: {pizza["base"]}")
        print(f"Salsa: {pizza["salsa"]}")
        print("Ingredientes:", ", ".join(pizza["ingredientes"]))
        
