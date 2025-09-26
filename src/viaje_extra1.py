x=int(input("Introduce la distancia total en km: "))
for i in range(0,x+1, 150000):
    y=0
    if x - i != 0 and i!=0:
        y+=1
        print("Parada en el km", i)
        print("Total de paradas para repostar: ", y)
