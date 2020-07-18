import statistics
import csv 
import matplotlib.pyplot as plt
from datetime import datetime
#se extrae la informacion del archivo csv
work="pp.csv"
#se extrae todos los datos del archivo csv para determinar cada variable:
#para Temperatura
with open(work) as f:
    read=csv.reader(f)
    cabezera=next(read)


    dates_t=[]
    temperatura=[]
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
        #para humedad
with open(work) as f: 
    dates_h=[]
    humedad=[]
       
    read=csv.reader(f)
    cabezera=next(read)
    for row in read:
        current_date_h=datetime.strptime(row[0],'%d/%m/%Y')                      
        try:
           
            h=float(row[3])
          
#codigo para eliminar datos vacios            
        except ValueError:
            print(f"Missing data for {current_date}")
#esos valores se añaden a las listas desde la linea 13 hasta la 19            
        else:
            dates_h.append(current_date_h)
              
            humedad.append(h)
        #para la precipitacion
with open(work) as f:
    read=csv.reader(f)
    cabezera=next(read)
#se extrae todos los datos del archivo csv

    dates_p=[]
    precipitacion=[]
    for row in read:
        current_date_p=datetime.strptime(row[0],'%d/%m/%Y')
        try:
            p=float(row[4])
          
          
        except ValueError:
            print(f"Missing data for {current_date_p}")
          
        else:
            dates_p.append(current_date_p)
            precipitacion.append(p)

cant_p=0
for i in dates_p:
    cant_p+=1

arreglo_cant_datos_anual_pp=[]
promedio_datos_anual_pp=[]
for a in range(2010,2020): 
    cant_datos_p=0
    suma_datos_pp=0
    for i in range(0,cant_p):
        if dates_p[i].year==a:      
            cant_datos_p+=1
    if cant_datos_p!= 0:
        suma_datos_pp+=precipitacion[i]
        prom_datos_anual_pp=suma_datos_pp/cant_datos_p
        promedio_datos_anual_pp.append(prom_datos_anual_pp)  
#hallando la lista de promedio para la prec.
arreglo_cant_datos_mensuales_p=[]
#arreglos mensuales para la precipitacion
promedio_datos_mensuales_p=[]
for i in range(1,13):
    cant_datos_mensual_p=0
    suma_datos_mensual_p=0    
    for a in range(0,cant_p):
        if dates_p[a].month==i:
          cant_datos_mensual_p+=1
          suma_datos_mensual_p+=precipitacion[a]
          
    promedio_datos_p=suma_datos_mensual_p/cant_datos_mensual_p
    
    #agregamos los valores a las listas de las variables halladas
    arreglo_cant_datos_mensuales_p.append(cant_datos_mensual_p)
    promedio_datos_mensuales_p.append(promedio_datos_p)
 #direccion del viento
with open(work) as f:
    direccion_viento=[]
    dates_dv=[]
    
    
    read=csv.reader(f)
    cabezera=next(read)
    for row in read:
        current_date_dv=datetime.strptime(row[0],'%d/%m/%Y') 
        try:
            
          
            d_v=float(row[5])
           
#codigo para eliminar datos vacios            
        except ValueError:
            print(f"Missing data for {current_date}")        
        else:
            dates_dv.append(current_date_dv)
            direccion_viento.append(d_v)
            
          #velocidad del viento
with open(work) as f:
    velocidad_viento=[]
    dates_vv=[]
    read=csv.reader(f)
    cabezera=next(read)
    for row in read:
        current_date_vv=datetime.strptime(row[0],'%d/%m/%Y') 
            
        try:
            v_v=float(row[6])

#codigo para eliminar datos vacios            
        except ValueError:
            print(f"Missing data for {current_date}")
#esos valores se añaden a las listas desde la linea 13 hasta la 19            
        else:
            dates_vv.append(current_date_vv)  
            velocidad_viento.append(v_v)

##########################################################################         
#bucle for para determinar la cantidad de datos "limpios" para cada variable
cant_t=0
for i in dates_t:
    cant_t+=1
    
cant_h=0
for i in dates_h:
    cant_h+=1

cant_p=0
for i in dates_p:
    cant_p+=1

cant_dv=0
for i in dates_dv:
    cant_dv+=1
    
cant_vv=0
for i in dates_vv:
    cant_vv+=1

#hallando la lista de promedio anual para en los 9 años de registro:
#arreglo cant.datos
arreglo_cant_datos_anual_t=[]
arreglo_cant_datos_anual_h=[]
arreglo_cant_datos_anual_dv=[]
arreglo_cant_datos_anual_vv=[]
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
    cant_datos_t=0
    cant_datos_h=0
    cant_datos_dv=0
    cant_datos_vv=0
    cant_datos_p=0
    

    suma_datos_t=0
    suma_datos_h=0
    suma_datos_pp=0
    suma_datos_dv=0
    suma_datos_vv=0
    for i in range(0,cant_t):
        if dates_t[i].year==a:
            cant_datos_t+=1
            suma_datos_t+=temperatura[i]
    
            
    for i in range(0,cant_h):
        if dates_h[i].year==a:
            cant_datos_h+=1
            suma_datos_h+=humedad[i]
            
    for i in range(0,cant_dv):
        if dates_dv[i].year==a:
           
            cant_datos_dv+=1
            suma_datos_dv+=direccion_viento[i]
            
            
    for i in range(0,cant_vv):
        if dates_vv[i].year==a:
            
            cant_datos_vv+=1
            suma_datos_vv+=velocidad_viento[i]
          
            
            
    prom_datos_anual_t=suma_datos_t/cant_datos_t
    
    prom_datos_anual_h=suma_datos_h/cant_datos_h
    prom_datos_anual_dv=suma_datos_dv/cant_datos_dv
    prom_datos_anual_vv=suma_datos_vv/cant_datos_vv 
    #agregamos los valores a las listas de las variables halladas
    arreglo_cant_datos_anual_t.append(cant_datos_t)
    arreglo_cant_datos_anual_h.append(cant_datos_h)
    arreglo_cant_datos_anual_dv.append(cant_datos_dv)
    arreglo_cant_datos_anual_vv.append(cant_datos_vv)
    
    
  
    promedio_datos_anual_t.append(prom_datos_anual_t)
    promedio_datos_anual_h.append(prom_datos_anual_h)
    promedio_datos_anual_dv.append(prom_datos_anual_dv)
    promedio_datos_anual_vv.append(prom_datos_anual_vv)

 #hallando la lista de promedio mensual
arreglo_cant_datos_mensuales_t=[]
arreglo_cant_datos_mensuales_h=[]
arreglo_cant_datos_mensuales_dv=[]
arreglo_cant_datos_mensuales_vv=[]
# #arreglos mensuales para la temperatura
promedio_datos_mensuales_t=[]
# #arreglos mensuales para la humedad
promedio_datos_mensuales_h=[]
# #arreglos mensuales para la direccion del viento
promedio_datos_mensuales_dv=[]
# ##arreglos mensuales para la velocidad del viento
promedio_datos_mensuales_vv=[]
# #bucle para añadir informacion al  arreglo: 
for i in range(1,13):
    cant_datos_mensual_t=0
    cant_datos_mensual_h=0
    cant_datos_mensual_dv=0
    cant_datos_mensual_vv=0
    ma=0
    me=1000
        
    suma_datos_mensual_t=0
    suma_datos_mensual_h=0
    suma_datos_mensual_dv=0
    suma_datos_mensual_vv=0
    
    
    
    for a in range(0,cant_t):
        if dates_t[a].month==i:
            cant_datos_mensual_t+=1
            suma_datos_mensual_t+=temperatura[a]
            
            if ma<temperatura[i]:
                ma=temperatura[i]
                
            if me>temperatura[i]:
                me=temperatura[i]
            
    for a in range(0,cant_h):
        if dates_h[a].month==i:
            cant_datos_mensual_h+=1
            suma_datos_mensual_h+=humedad[a]
            
            
    for a in range(0,cant_dv):
        if dates_dv[a].month==i:
            cant_datos_mensual_dv+=1
            suma_datos_mensual_dv+=direccion_viento[a]
            
            
    for a in range(0,cant_vv):
        if dates_vv[a].month==i:
            cant_datos_mensual_vv+=1
            suma_datos_mensual_vv+=temperatura[a]
          
    promedio_datos_t=suma_datos_mensual_t/cant_datos_mensual_t
    promedio_datos_h=suma_datos_mensual_h/cant_datos_mensual_h
    promedio_datos_dv=suma_datos_dv/cant_datos_mensual_dv
    promedio_datos_vv=suma_datos_vv/cant_datos_mensual_vv
    #agregamos los valores a las listas de las variables halladas
    arreglo_cant_datos_mensuales_t.append(cant_datos_mensual_t)
    arreglo_cant_datos_mensuales_h.append(cant_datos_mensual_h)
    arreglo_cant_datos_mensuales_dv.append(cant_datos_mensual_dv)
    arreglo_cant_datos_mensuales_vv.append(cant_datos_mensual_vv)
    
    
    
    promedio_datos_mensuales_t.append(promedio_datos_t)
    promedio_datos_mensuales_h.append(promedio_datos_h)
    promedio_datos_mensuales_dv.append(promedio_datos_dv)
    promedio_datos_mensuales_vv.append(promedio_datos_vv)

# #codigos para realizar el grafico anual de temperatura, humedad,dir.viento y vel.viento
# #codigo para realizar el grafico anual de temperatura
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
#################################################################################
prom_datos_anual_pp
year=[2014,2015,2016,2017,2018,2019]
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(year,promedio_datos_anual_pp,linewidth=5,c="yellow")
ax.set_title("Promedio anual de precipitación \n E.'Campor de Marte'",fontsize=20)
ax.set_ylabel("Precipitación (mm)",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=15)
ax.axis([2014,2019,0,2.5])
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

#codigo para realizar el grafico mesual de precipitacion
promedio_datos_mensuales_p
meses=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(meses,promedio_datos_mensuales_p,linewidth=5,c="green")
ax.set_title("Promedio estacional  de preciptación \n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Meses",fontsize=15)
ax.set_ylabel("Precipitación (mm)",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=15)
plt.show()

 #promedio y valores max y min, y desviacion estandar de la temperatura
promedio_por_mes_p=statistics.mean(promedio_datos_mensuales_p)
maximo_valor_p_mensual=max(promedio_datos_mensuales_p)
minimo_valor_p_mensual=min(promedio_datos_mensuales_p)
desv_standar_p=statistics.stdev(promedio_datos_mensuales_p)
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








     
