distancia_km = int(input("Escribe una distancia en km"))
velocidad_kmh = int(input("Escribe una velocidad "))
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
print(f"Tardarías {tiempo_dias} días en llegar.")
edad= int(input("Dime tu edad "))
nivel_fisico= int(input("Dime tu nivel físico "))
while (nivel_fisico< 1 or nivel_fisico>10):
    nivel_fisico= int(input("No seas tonto.Dime tu nivel físico entre 1 y 10 "))

if edad<18:
    print("Debe ser mayor de edad")
elif nivel_fisico< 5:
    print("Debes estar en forma")
else:
    print("¡Listo para despegar!")