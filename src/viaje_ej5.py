x="s"
while(x=="s"):
    distancia_km = int(input("Escribe una distancia en km"))
    velocidad_kmh = int(input("Escribe una velocidad "))
    tiempo_horas = distancia_km // velocidad_kmh
    tiempo_dias = tiempo_horas // 24
    print(f"Tardarías {tiempo_dias} días en llegar.")
    x= "a"
    while(x != "s" and x!="n"):
         x= str(input("¿Quieres hacer otra simulación? (s/n) "))

    
