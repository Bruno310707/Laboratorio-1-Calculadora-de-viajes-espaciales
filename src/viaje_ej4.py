distancia_km = 225000000
for i in range(10000, 50001):
    velocidad_kmh= i
    tiempo_horas = distancia_km / velocidad_kmh
    tiempo_dias = tiempo_horas / 24
    if i%10000==0:
        print(f"Velocidad= {i} km/h -> Tiempo: {tiempo_dias} dias")
   
