def run():

    espada = 15.52
    escudo = 35.87
    armadura = 62.35
    casco = 50.50
    botas = 15.63
    power_up = 100 
    mapa = 10.85
    refinamiento_bronce = 15.89
    refinamiento_plata = 25.47
    refinamiento_oro = 35.24
    refinamiento_diamante = 45.89
    pocion_cura = 12.48
    pocion_mana = 13.74

    espada_bronce = espada + refinamiento_bronce
    espada_plata = espada + refinamiento_plata
    espada_oro = espada + refinamiento_oro
    espada_diamante = espada + refinamiento_diamante

    escudo_bronce = escudo + refinamiento_bronce
    escudo_plata = escudo + refinamiento_plata
    escudo_oro = escudo + refinamiento_oro
    escudo_diamante = escudo + refinamiento_diamante

    armadura_bronce = armadura + refinamiento_bronce
    armadura_plata = armadura + refinamiento_plata
    armadura_oro = armadura + refinamiento_oro
    armadura_diamante = armadura + refinamiento_diamante

    casco_bronce = casco + refinamiento_bronce
    casco_plata = casco + refinamiento_plata
    casco_oro = casco + refinamiento_oro
    casco_diamante = casco + refinamiento_diamante

    botas_bronce = botas + refinamiento_bronce
    botas_plata = botas + refinamiento_plata
    botas_oro = botas+ refinamiento_oro
    botas_diamante = botas + refinamiento_diamante

    # espada_up = espada + power_up

    equipamiento_bronce = espada_bronce + escudo_bronce + armadura_bronce + casco_bronce + botas_bronce
    equipamiento_plata = espada_plata + escudo_plata + armadura_plata + casco_plata + botas_plata
    equipamiento_oro = espada_oro + escudo_oro  + armadura_oro  + casco_oro  + botas_oro 
    equipamiento_diamante = espada_diamante + escudo_diamante  + armadura_diamante  + casco_diamante  + botas_diamante

    boleano = equipamiento_bronce < equipamiento_plata

    print("***********************************************************")
    print("Listas los objetos del equipamiento: Nombre y Valor")
    print("espada: ", espada)
    print("escudo: ", escudo)
    print("armadura: ", armadura)

    print("***********************************************************")
    print("Reforzamiento de armadura y arma")
    print("armadura de bronce", equipamiento_bronce)

    print("El precio de armadura de bronce es menor que armadura de plata: ", boleano )

    print("Cuanto vale comprar una armadura de diamante + pocion de cura y mana: ", equipamiento_diamante + pocion_cura + pocion_mana)

    print("Si tengo 40 puntos me alcanza para comprar las botas de diamante: ", botas_diamante <= 40)

    print("***********************************************************")
    print("No colocar mas de 5 objetos en la mochila")
    mochila = 0

    if pocion_cura + pocion_mana + mapa + power_up + power_up <= 200:
        mochila = pocion_cura + pocion_mana + mapa + power_up + power_up
        print("Para la opcion 1, el precio del equipamiento en mochila es menor a 200: ", mochila)
    elif pocion_cura + pocion_mana + mapa + refinamiento_diamante + power_up <= 200:
        mochila = pocion_cura + pocion_mana + mapa + refinamiento_diamante + power_up
        print("Para la opcion 2, el precio del equipamiento en mochila es menor a 200: ", mochila)
    else: 
        print("Ninguno de tus intentos fue exitoso")

    mochila_op = 0

    if pocion_cura + pocion_mana + refinamiento_diamante <= 200:
        mochila_op = pocion_cura + pocion_mana + refinamiento_diamante
        print("Esta opcion tambien es viable, Total precio: ", mochila_op)

            
    print("***********************************************************")
    print("Es tu día de suerte te regalo otra mochila pero solo puedes agregarle la superpocion que es pocion cura + pocion mana") 
    super_pocion = pocion_cura + pocion_mana 

    mochila_dos = 0

    while mochila_dos <= 200:
        mochila_dos += super_pocion
        print("El valor de la mochila dos es de: ", mochila_dos)

    mochila_dos -= super_pocion
    print("Nos pasamos del limite, restamos una super pocion y tenemos un valor de: ", mochila_dos)

    print("***********************************************************")

    print("La esfinge le hizo una actualización a tu mochila, porque solo podias conocer el valor de los objetos que tenias")
    print("Ahora sabras el objeto que tienes, la cantidad y su valor unitario, pero tu debes volver a llenar")

    mochila_actualizada = { 
        "pocion_cura" : {"cantidad" : 1, "valor_unitario" : pocion_cura},
        "pocion_mana" : {"cantidad" : 1, "valor_unitario" : pocion_mana},
        "mapa" : {"cantidad" : 1, "valor_unitario" : mapa},
        "refinamiento_diamante" : {"cantidad" : 1, "valor_unitario" : refinamiento_diamante},
        "power_up" : {"cantidad" : 1, "valor_unitario" : power_up}
    }

    mochila_dos_actualizada = {
        "super_pocion" : {"cantidad" : 7, "valor_superpocion" : super_pocion*7}
    }
        
    print("Mochila actualizada: ",mochila_actualizada)
    print("Mochila dos actualizada:", mochila_dos_actualizada)

    print("***********************************************************")

    print("En esta aventura te van a acompañar 8 integrantes más, y te han pedido que le armes una mochila igual a la tuya y la coloques en el vehiculo")

    vehiculo = [{}] * 7

    for compartimiento in range (7):
        vehiculo[compartimiento] = {
            "pocion_cura" : {"cantidad" : 1, "valor_unitario" : pocion_cura},
            "pocion_mana" : {"cantidad" : 1, "valor_unitario" : pocion_mana},
            "mapa" : {"cantidad" : 1, "valor_unitario" : mapa},
            "refinamiento_diamante" : {"cantidad" : 1, "valor_unitario" : refinamiento_diamante},
            "power_up" : {"cantidad" : 1, "valor_unitario" : power_up}
        }
        print("Acabas de armar la mochila para el compartimiento: ", compartimiento + 1)

    
    for mochila in vehiculo:
        print(mochila)

    # Agregamos dos espadas, dos escudos y una superpocion a los primeros 4 primeros integrantes 

    print("***********************************************************")
    print("Agregamos dos espadas, dos escudos y una superpocion a los primeros 4 primeros integrantes: ")

    def agregar_elemento_mochila():
        for compartimiento in range(4):
            vehiculo[compartimiento] = {
                "pocion_cura" : {"cantidad" : 1, "valor_unitario" : pocion_cura},
                "pocion_mana" : {"cantidad" : 1, "valor_unitario" : pocion_mana},
                "mapa" : {"cantidad" : 1, "valor_unitario" : mapa},
                "refinamiento_diamante" : {"cantidad" : 1, "valor_unitario" : refinamiento_diamante},
                "power_up" : {"cantidad" : 1, "valor_unitario" : power_up},
                "espada" : {"cantidad" : 2, "valor_unitario" : espada},
                "escudo" : {"cantidad" : 2, "valor_unitario" : escudo},
                "super_pocion" : {"cantidad" : 1, "valor_unitario" : super_pocion}
            }

        imprimir(vehiculo)
        calcular_total_elementos(vehiculo)

    def calcular_total_elementos(vehiculo):
        total_elementos_mochila = {}

        print("Calculo elementos en mochila")
        for mochila in vehiculo:
            for elemento, detalle in mochila.items():
                if elemento in total_elementos_mochila:
                    total_elementos_mochila[elemento] += detalle["cantidad"]
                else:
                    total_elementos_mochila[elemento] = detalle["cantidad"]

        print(total_elementos_mochila)

    def imprimir (estructura):
        for objeto in estructura:
            print(objeto)
        

    agregar_elemento_mochila()
    

if __name__ == "__main__":
    run()
    