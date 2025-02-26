def calcular_puntuacion(puntos, bonus):
    if puntos >= 100 and bonus == True:
        return "Oro"
    elif puntos >= 100 and bonus == False:
        return "Plata"
    elif 50 <= puntos < 100 and bonus == True:
        return "Plata"
    else:
        return "Bronce"
