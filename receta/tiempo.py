

# Funcion recibe como parametro argumento pizza
def calcular_tiempo(pizza):
        
        tiempo_base = 20
        
        # se cuentan los ingredientes y se agregan 2 minutos por cada uno
        tiempo_ingredientes = len(pizza["ingredientes"]) * 2
        
        
        # retorna tiempo total (suma)
        return tiempo_base + tiempo_ingredientes
