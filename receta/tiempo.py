def calcular_tiempo(pizza):
        tiempo_base = 20
        tiempo_ingredientes = len(pizza["ingredientes"]) * 2
        return tiempo_base + tiempo_ingredientes
