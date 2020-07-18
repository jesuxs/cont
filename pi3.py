import statistics
import csv 
import matplotlib.pyplot as plt
from datetime import datetime

work="vientos.csv"
with open(work) as f:
    read=csv.reader(f)
    cabezera=next(read)


    dates_v=[]
    vientos=[]
    for row in read:
        current_date_v=datetime.strptime(row[3],'%d/%m/%Y')
        try:
            v=float(row[5])
          
          
        except ValueError:
            print(f"Missing data for {current_date_v}")
          
        else:
            dates_v.append(current_date_v)
            vientos.append(v)
            
cant_v=0
for i in dates_v:
    cant_v+=1

arreglo_cant_datos_anual_v=[]
promedio_datos_anual_v=[]
for a in range(1998,2019):
    #bucle para añadir informacion al  arreglo: 
    cant_datos_v=0   
    suma_datos_v=0
    for i in range(0,cant_v):
        if dates_v[i].year==a:
            cant_datos_v+=1
            suma_datos_v+=vientos[i]
            
            
    prom_datos_anual_v=suma_datos_v/cant_datos_v
 
    promedio_datos_anual_v.append(prom_datos_anual_v)
            
 
arreglo_cant_datos_mensuales_v=[]    
promedio_datos_mensuales_v=[]    
    
for i in range(1,13):
    cant_datos_mensual_v=0
    suma_datos_mensual_v=0    
    for a in range(0,cant_v):
        if dates_v[a].month==i:
          cant_datos_mensual_v+=1
          suma_datos_mensual_v+=vientos[a]
          
    promedio_datos_v=suma_datos_mensual_v/cant_datos_mensual_v
       
    arreglo_cant_datos_mensuales_v.append(cant_datos_mensual_v)
    promedio_datos_mensuales_v.append(promedio_datos_v)


promedio_datos_anual_v
year=[]
for i in range(1998,2019):
    i+=0
    year.append(i)

fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(year,promedio_datos_anual_v,linewidth=5,c="green")
ax.set_title("Promedido anual de la velocidad del viento",fontsize=20)
ax.set_xlabel("Años",fontsize=15)
ax.set_ylabel("velocidad (m/s)",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=19)
ax.axis([1998,2018,0,13])

plt.show()

promedio_datos_mensuales_v
meses=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(meses,promedio_datos_mensuales_v,linewidth=5,c="black")
ax.set_title("Promedio estacional de la velocidad del viento",fontsize=20)
ax.set_xlabel("Meses",fontsize=15)
ax.set_ylabel("velocidad (m/s)",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=15)
plt.show()


print(promedio_datos_anual_v)
print(promedio_datos_mensuales_v)
   
        