import statistics
import csv 
import matplotlib.pyplot as plt
from datetime import datetime
#se extrae la informacion del archivo csv
work="SO.csv"
with open(work) as f:
    read=csv.reader(f)
    cabezera=next(read)
#se extrae todos los datos del archivo csv

    dates_so=[]
    so=[]
   
    for row in read:
        current_date_so=datetime.strptime(row[0],'%d/%m/%Y %H:%M')
        
        try:
            so_two=float(row[1])
            
        except ValueError:
            print(f"Missing data for {current_date_so}")
          
        else:
            dates_so.append(current_date_so)
            so.append(so_two)


cant_so=0
for i in dates_so:
    cant_so +=1
#hallando la lista de promedio anual para en los 9 años de registro:
#arreglo cant.datos
arreglo_cant_datos_anual_so=[]
#arreglo para datos de temperatura
promedio_datos_anual_so=[]
for a in range(2015,2020):
   #bucle para añadir informacion al  arreglo: 
    cant_datos_so=0
    suma_datos_so=0
    
    for i in range(0,cant_so):
        if dates_so[i].year==a:
            cant_datos_so +=1
            suma_datos_so=so[i]
            
    if cant_datos_so!= 0:
        suma_datos_so+=so[i]
        prom_datos_anual_so=suma_datos_so/cant_datos_so
        promedio_datos_anual_so.append(prom_datos_anual_so)
     
                    
#hallando la lista de promedio de PM_10
arreglo_cant_datos_mensuales_so=[]
#arreglos mensuales para la precipitacion
promedio_datos_mensuales_so=[]
for i in range(1,13):
    cant_datos_mensual_so=0
    suma_datos_mensual_so=0
    for a in range(0,cant_so):
        if dates_so[a].month==i:
          cant_datos_mensual_so+=1
          suma_datos_mensual_so=so[a]
          
    promedio_datos_so=suma_datos_mensual_so/cant_datos_mensual_so
    
    #agregamos los valores a las listas de las variables halladas
    arreglo_cant_datos_mensuales_so.append(cant_datos_mensual_so)
    promedio_datos_mensuales_so.append(promedio_datos_so)

promedio_datos_anual_so
year=[2016,2017]
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(year,promedio_datos_anual_so,linewidth=5,c="green")
ax.set_title("Promedio anual de NO2\n E.'Campo de Marte'",fontsize=40)
ax.set_xlabel("Años",fontsize=40)
ax.set_ylabel("NO2 (µg/m³)",fontsize=40)
ax.tick_params(axis="both",which="major",labelsize=50)
plt.show()

promedio_datos_mensuales_so
meses=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(meses,promedio_datos_mensuales_so,linewidth=5,c="black")
ax.set_title("Promedio estacional de NO2\n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Meses",fontsize=15)
ax.set_ylabel("NO2 (µg/m³)",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=15)
plt.show()



