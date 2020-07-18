import statistics
import csv 
import matplotlib.pyplot as plt
from datetime import datetime
#se extrae la informacion del archivo csv
work="pp.csv"
with open(work) as f:
    read=csv.reader(f)
    cabezera=next(read)
#se extrae todos los datos del archivo csv

    dates_t=[]
    temperatura=[]
    humedad=[]
    
    direccion_viento=[]
    velocidad_viento=[]
    
#se ubica cada variable para cada fila
    for row in read:
        current_date=datetime.strptime(row[0],'%d/%m/%Y')
        try:
            t=float(row[2])
            
#codigo para eliminar datos vacios            
        except ValueError:
            print(f"Missing data for {current_date}")
#esos valores se añaden a las listas desde la linea 13 hasta la 19            
        else:
            dates_t.append(current_date)
            temperatura.append(t)   
        current_date2=datetime.strptime(row[0],'%d/%m/%Y')                      
        try:
           
            h=float(row[3])
          
#codigo para eliminar datos vacios            
        except ValueError:
            print(f"Missing data for {current_date}")
#esos valores se añaden a las listas desde la linea 13 hasta la 19            
        else:
            dates.append(current_date)
              
            humedad.append(h)
        
        try:
            
          
            d_v=float(row[5])
           
#codigo para eliminar datos vacios            
        except ValueError:
            print(f"Missing data for {current_date}")
#esos valores se añaden a las listas desde la linea 13 hasta la 19            
        else:
            dates.append(current_date)
            direccion_viento.append(d_v)
            
            
        try:
            v_v=float(row[6])
            
             
#codigo para eliminar datos vacios            
        except ValueError:
            print(f"Missing data for {current_date}")
#esos valores se añaden a las listas desde la linea 13 hasta la 19            
        else:
            dates.append(current_date)            
            velocidad_viento.append(v_v)
         
#bucle for para determinar la cantidad de datos "limpios"
cant=0
for i in dates:
    cant +=1
#hallando la lista de promedio anual para en los 9 años de registro:
#arreglo cant.datos
arreglo_cant_datos_anual=[]
#arreglo para datos de temperatura
promedio_datos_anual_t=[]
#arreglo para datos de humedad
promedio_datos_anual_h=[]
#arreglo para datos de direccion del viento
promedio_datos_anual_dv=[]
#arreglo para datos de velocidad del viento
promedio_datos_anual_vv=[]
#hallando la lista de promedio anual durante los 9 años de registro
for a in range(2010,2020):
   #bucle para añadir informacion al  arreglo: 
    cant_datos=0
    suma_datos_t=0
    suma_datos_h=0
    suma_datos_p=0
    suma_datos_dv=0
    suma_datos_vv=0
    for i in range(0,cant):
        if dates[i].year==a:
            cant_datos+=1
            suma_datos_t+=temperatura[i]
            suma_datos_h+=humedad[i]
           
            suma_datos_dv+=direccion_viento[i]
            suma_datos_vv+=velocidad_viento[i]
    prom_datos_anual_t=suma_datos_t/cant_datos
    prom_datos_anual_h=suma_datos_h/cant_datos
    prom_datos_anual_dv=suma_datos_dv/cant_datos
    prom_datos_anual_vv=suma_datos_vv/cant_datos      
    #agregamos los valores a las listas de las variables halladas
    arreglo_cant_datos_anual.append(cant_datos)
    promedio_datos_anual_t.append(prom_datos_anual_t)
    promedio_datos_anual_h.append(prom_datos_anual_h)
    promedio_datos_anual_dv.append(prom_datos_anual_dv)
    promedio_datos_anual_vv.append(prom_datos_anual_vv)
            

#hallando la lista de promedio mensual
arreglo_cant_datos_mensuales=[]
#arreglos mensuales para la temperatura
promedio_datos_mensuales_t=[]
#arreglos mensuales para la humedad
promedio_datos_mensuales_h=[]
#arreglos mensuales para la direccion del viento
promedio_datos_mensuales_dv=[]
##arreglos mensuales para la velocidad del viento
promedio_datos_mensuales_vv=[]
#bucle para añadir informacion al  arreglo: 
for i in range(1,13):
    cant_datos_mensual=0
    suma_datos_mensual_t=0
    suma_datos_mensual_h=0
    suma_datos_mensual_dv=0
    suma_datos_mensual_vv=0
    for a in range(0,cant):
        if dates[a].month==i:
          cant_datos_mensual+=1
          suma_datos_mensual_t+=temperatura[a]
          suma_datos_mensual_h+=humedad[a]
          suma_datos_mensual_dv+=direccion_viento[a]
          suma_datos_mensual_vv+=velocidad_viento[a]
    promedio_datos_t=suma_datos_mensual_t/cant_datos_mensual
    promedio_datos_h=suma_datos_mensual_h/cant_datos_mensual
    promedio_datos_dv=suma_datos_dv/cant_datos_mensual
    promedio_datos_vv=suma_datos_vv/cant_datos_mensual
    #agregamos los valores a las listas de las variables halladas
    arreglo_cant_datos_mensuales.append(cant_datos_mensual)
    promedio_datos_mensuales_t.append(promedio_datos_t)
    promedio_datos_mensuales_h.append(promedio_datos_h)
    promedio_datos_mensuales_dv.append(promedio_datos_dv)
    promedio_datos_mensuales_vv.append(promedio_datos_vv)

#codigos para realizar el grafico anual de temperatura, humedad,dir.viento y vel.viento
#codigo para realizar el grafico anual de temperatura
promedio_datos_anual_t
year=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]      
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(year,promedio_datos_anual_t,linewidth=5,c="green")
ax.set_title("Promedio anual de temperatura \n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Años",fontsize=15)
ax.set_ylabel("Temperatura °C",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=15)
ax.axis([2010,2019,18,22])
plt.show()
#codigo para realizar el grafico anual de  humedad
promedio_datos_anual_h
year=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]   
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(year,promedio_datos_anual_h,linewidth=5,c="red")
ax.set_title("Promedio anual de humedad \n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Años",fontsize=20)
ax.set_ylabel("Humedad % ",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=15)
ax.axis([2010,2019,75,84])
plt.show()
#codigo para realizar el grafico anual de direccion del viento
promedio_datos_anual_dv
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(year,promedio_datos_anual_dv,linewidth=5,c="black")
ax.set_title("Promedio anual de direccion del viento\n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Años",fontsize=20)
ax.set_ylabel("Dirección del viento(°)",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=15)
ax.axis([2010,2019,215,228])
plt.show()
#codigo para realizar el grafico anual de la velocidad del viento
promedio_datos_anual_vv
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(year,promedio_datos_anual_vv,linewidth=5,c="red")
ax.set_title("Promedio anual de velocidad del viento\n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Años",fontsize=20)
ax.set_ylabel("Velocidad del viento(m/s)",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=15)
ax.axis([2010,2019,0.5,2.5])
plt.show()

#codigospara realizar el grafico mensual  de temperatura, humedad,dir.viento y vel.viento
#codigo para realizar el grafico mesual de temperatura
t_mens=promedio_datos_mensuales_t
meses=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(meses,t_mens,linewidth=5,c="black")
ax.set_title("Promedio estacional de temperatura \n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Meses",fontsize=15)
ax.set_ylabel("Temperatura °C",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=15)
plt.show()

#codigo para realizar el grafico mesual de humedad
promedio_datos_mensuales_h
meses=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(meses,promedio_datos_mensuales_h,linewidth=5,c="green")
ax.set_title("Promedio estacional  de humedad\n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Meses",fontsize=15)
ax.set_ylabel("Humedad %",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=15)
plt.show()

#codigo para realizar el grafico mesual de direccion del viento
promedio_datos_mensuales_dv
meses=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(meses,promedio_datos_mensuales_dv,linewidth=5,c="yellow")
ax.set_title("Promedio estacional de dirección del viento \n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Meses",fontsize=15)
ax.set_ylabel("Dirección del viento (°)",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=15)
plt.show()

#codigo para realizar el grafico mesual de velocidad del viento
promedio_datos_mensuales_vv
meses=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(meses,promedio_datos_mensuales_vv,linewidth=5,c="brown")
ax.set_title("Promedio estacional de velocidad del viento\n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Meses",fontsize=15)
ax.set_ylabel("Velocidad del viento (m/s)",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=15)
plt.show()

#codigo para hallar el promedio,maximo y minimo de temperatura por año
#promedio y valores max y min, y desviacion estandar de la temperatura
promedio_por_año_t=statistics.mean( promedio_datos_anual_t)
maximo_valor_t_anual=max(promedio_datos_anual_t)
minimo_valor_t_anual=min(promedio_datos_anual_t)
desv_standar_t=statistics.stdev(promedio_datos_anual_t)

#promedio y valores max y min, y desviacion estandar de humedad
promedio_por_año_h=statistics.mean(promedio_datos_anual_h)
maximo_valor_h_anual=max(promedio_datos_anual_h)
minimo_valor_h_anual=min(promedio_datos_anual_h)
desv_standar_h=statistics.stdev(promedio_datos_anual_h)

#promedio y valores max y min, y desviacion estandar de direccion del viento
promedio_por_año_dv=statistics.mean(promedio_datos_anual_dv)
maximo_valor_dv_anual=max(promedio_datos_anual_dv)
minimo_Valor_dv_anual=min(promedio_datos_anual_dv)
desv_standar_dv=statistics.stdev(promedio_datos_anual_dv)

#promedio y valores max y min, y desviacion estandar de la velocidad del viento
promedio_por_año_vv=statistics.mean(promedio_datos_anual_vv)
maximo_valor_vv_anual=max(promedio_datos_anual_vv)
minimo_Valor_vv_anual=min(promedio_datos_anual_vv)
desv_standar_vv=statistics.stdev(promedio_datos_anual_vv)

##################################################################################################
#codigo para hallar el promedio,maximo y minimo de temperatura por mes
#promedio y valores max y min, y desviacion estandar de la temperatura
promedio_por_mes_t=statistics.mean(promedio_datos_mensuales_t)
maximo_valor_t_mensual=max(promedio_datos_mensuales_t)
minimo_valor_t_mensual=min(promedio_datos_mensuales_t)
desv_standar_t=statistics.stdev(promedio_datos_mensuales_t)

#promedio y valores max y min, y desviacion estandar de la humedad
promedio_por_mes_h=statistics.mean(promedio_datos_mensuales_h)
maximo_valor_h_mensual=max(promedio_datos_mensuales_h)
minimo_valor_h_mensual=min(promedio_datos_mensuales_h)
desv_standar_h=statistics.stdev(promedio_datos_mensuales_h)

#promedio y valores max y min, y desviacion estandar de la direccion del viento
promedio_por_mes_dv=statistics.mean(promedio_datos_mensuales_dv)
maximo_valor_dv_mensual=max(promedio_datos_mensuales_dv)
minimo_valor_dv_mensual=min(promedio_datos_mensuales_dv)
desv_standar_dv=statistics.stdev(promedio_datos_mensuales_dv)

#promedio y valores max y min, y desviacion estandar de la velocidad del viento
promedio_por_mes_vv=statistics.mean(promedio_datos_mensuales_vv)
maximo_valor_vv_mensual=max(promedio_datos_mensuales_vv)
minimo_valor_vv_mensual=min(promedio_datos_mensuales_vv)
desv_standar_vv=statistics.stdev(promedio_datos_mensuales_vv)








     
