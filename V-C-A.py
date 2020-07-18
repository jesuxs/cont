
import csv 
import matplotlib.pyplot as plt
from datetime import datetime
#se extrae la informacion del archivo csv
work="PMT.csv"
with open(work) as f:
    read=csv.reader(f)
    cabezera=next(read)
#se extrae todos los datos del archivo csv
    # rataza

    dates_pm_10=[]
    pm_10=[]
   
    for row in read:
        current_date_pm_10=datetime.strptime(row[0],'%d/%m/%Y %H:%M')
        
        try:
            pm_ten=float(row[1])
            
        except ValueError:
            print(f"Missing data for {current_date_pm_10}")
          
        else:
            dates_pm_10.append(current_date_pm_10)
            pm_10.append(pm_ten)
   
cant_pm_10=0
for i in dates_pm_10:
    cant_pm_10+=1
#hallando la lista de promedio anual para en los 9 años de registro:
#arreglo cant.datos
arreglo_cant_datos_anual_pm_10=[]
#arreglo para datos de temperatura
promedio_datos_anual_pm_10=[]
for a in range(2010,2020):
   #bucle para añadir informacion al  arreglo: 
    cant_datos_pm_10=0
    suma_datos_pm_10=0
    
    for i in range(0,cant_pm_10):
        if dates_pm_10[i].year==a:
            cant_datos_pm_10+=1
            suma_datos_pm_10+=pm_10[i]
                       
    prom_datos_anual_pm_10=suma_datos_pm_10/cant_datos_pm_10
       
    #agregamos los valores a las listas de las variables halladas
    arreglo_cant_datos_anual_pm_10.append(cant_datos_pm_10)
    promedio_datos_anual_pm_10.append(prom_datos_anual_pm_10)
   
    
#hallando la lista de promedio de PM_10
arreglo_cant_datos_mensuales_pm_10=[]
#arreglos mensuales para la precipitacion
promedio_datos_mensuales_pm_10=[]
for i in range(1,13):
    cant_datos_mensual_pm_10=0
    suma_datos_mensual_pm_10=0
    for a in range(0,cant_pm_10):
        if dates_pm_10[a].month==i:
          cant_datos_mensual_pm_10+=1
          suma_datos_mensual_pm_10+=pm_10[a]
          
    promedio_datos_pm_10=suma_datos_mensual_pm_10/cant_datos_mensual_pm_10
    
    #agregamos los valores a las listas de las variables halladas
    arreglo_cant_datos_mensuales_pm_10.append(cant_datos_mensual_pm_10)
    promedio_datos_mensuales_pm_10.append(promedio_datos_pm_10)

promedio_datos_anual_pm_10
year=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]      
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(year,promedio_datos_anual_pm_10,linewidth=5,c="green")
ax.set_title("Promedio anual de PM 10 \n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Años",fontsize=15)
ax.set_ylabel("PM 10 (µg/m³)",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=15)
ax.axis([2010,2019,20,50])
plt.show()

promedio_datos_mensuales_pm_10
meses=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(meses,promedio_datos_mensuales_pm_10,linewidth=5,c="black")
ax.set_title("Promedio estacional de PM 10 \n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Meses",fontsize=15)
ax.set_ylabel("PM 10 (µg/m³)",fontsize=15)
ax.tick_params(axis="both",which="major",labelsize=15)
plt.show()
          
work="PM2.csv"
with open(work) as f:
    read=csv.reader(f)
    cabezera=next(read)
#se extrae todos los datos del archivo csv

    dates_pm_2=[]
    pm_2=[]
   
    for row in read:
        current_date_pm_2=datetime.strptime(row[0],'%d/%m/%Y %H:%M')
        
        try:
            pm_two=float(row[1])
            
        except ValueError:
            print(f"Missing data for {current_date_pm_2}")
          
        else:
            dates_pm_2.append(current_date_pm_2)
            pm_2.append(pm_two)
   
cant_pm_2=0
for i in dates_pm_2:
    cant_pm_2+=1
#hallando la lista de promedio anual para en los 9 años de registro:
#arreglo cant.datos
arreglo_cant_datos_anual_pm_2=[]
#arreglo para datos de temperatura
promedio_datos_anual_pm_2=[]
for a in range(2014,2020):
   #bucle para añadir informacion al  arreglo: 
    cant_datos_pm_2=0
    suma_datos_pm_2=0
    
    for i in range(0,cant_pm_2):
        if dates_pm_2[i].year==a:
            cant_datos_pm_2+=1
            suma_datos_pm_2+=pm_2[i]
                       
    prom_datos_anual_pm_2=suma_datos_pm_2/cant_datos_pm_2
       
    #agregamos los valores a las listas de las variables halladas
    arreglo_cant_datos_anual_pm_2.append(cant_datos_pm_2)
    promedio_datos_anual_pm_2.append(prom_datos_anual_pm_2)
   
    

#hallando la lista de promedio de PM_10
arreglo_cant_datos_mensuales_pm_2=[]
#arreglos mensuales para la precipitacion
promedio_datos_mensuales_pm_2=[]
for i in range(1,13):
    cant_datos_mensual_pm_2=0
    suma_datos_mensual_pm_2=0
    for a in range(0,cant_pm_2):
        if dates_pm_2[a].month==i:
          cant_datos_mensual_pm_2+=1
          suma_datos_mensual_pm_2=pm_2[i]
          
    promedio_datos_pm_2=suma_datos_mensual_pm_2/cant_datos_mensual_pm_2
    
    #agregamos los valores a las listas de las variables halladas
    arreglo_cant_datos_mensuales_pm_2.append(cant_datos_mensual_pm_2)
    promedio_datos_mensuales_pm_2.append(promedio_datos_pm_2)

promedio_datos_anual_pm_2
year=[2014,2015,2016,2017,2018,2019]      
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(year,promedio_datos_anual_pm_2,linewidth=5,c="green")
ax.set_title("Promedio anual de PM 2\n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Meses",fontsize=15)
ax.set_ylabel("PM 2 (µg/m³)",fontsize=15)
ax.tick_params(axis="both",which="major",labelsize=15)
plt.show()

promedio_datos_mensuales_pm_2
meses=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(meses,promedio_datos_mensuales_pm_2,linewidth=5,c="black")
ax.set_title("Promedio estacional de PM 2.5\n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Meses",fontsize=15)
ax.set_ylabel("PM 2.5 (µg/m³)",fontsize=15)
ax.tick_params(axis="both",which="major",labelsize=15)
plt.show()      
    #####################################
work="CO.csv"
with open(work) as f:
    read=csv.reader(f)
    cabezera=next(read)
#se extrae todos los datos del archivo csv

    dates_co=[]
    pm_co=[]
   
    for row in read:
        current_date_co=datetime.strptime(row[0],'%d/%m/%Y %H:%M')
        
        try:
            pm_c=float(row[1])
            
        except ValueError:
            print(f"Missing data for {current_date_co}")
          
        else:
            dates_co.append(current_date_co)
            pm_co.append(pm_c)
   
cant_co=0
for i in dates_co:
    cant_co+=1
#hallando la lista de promedio anual para en los 9 años de registro:
#arreglo cant.datos
arreglo_cant_datos_anual_co=[]
#arreglo para datos de temperatura
promedio_datos_anual_co=[]
for a in range(2015,2020):
   #bucle para añadir informacion al  arreglo: 
    cant_datos_co=0
    suma_datos_co=0
    
    for i in range(0,cant_co):
        if dates_co[i].year==a:
            cant_datos_co+=1
            suma_datos_co=pm_co[i]
                       
    prom_datos_anual_co=suma_datos_co/cant_datos_co
       
    #agregamos los valores a las listas de las variables halladas
    arreglo_cant_datos_anual_co.append(cant_datos_co)
    promedio_datos_anual_co.append(prom_datos_anual_co)
   
    

#hallando la lista de promedio de PM_10
arreglo_cant_datos_mensuales_co=[]
#arreglos mensuales para la precipitacion
promedio_datos_mensuales_co=[]
for i in range(1,13):
    cant_datos_mensual_co=0
    suma_datos_mensual_co=0
    for a in range(0,cant_co):
        if dates_co[a].month==i:
          cant_datos_mensual_co+=1
          suma_datos_mensual_co=pm_co[a]
          
    promedio_datos_co=suma_datos_mensual_co/cant_datos_mensual_co
    
    #agregamos los valores a las listas de las variables halladas
    arreglo_cant_datos_mensuales_co.append(cant_datos_mensual_co)
    promedio_datos_mensuales_co.append(promedio_datos_co)

promedio_datos_anual_co
year=[2015,2016,2017,2018,2019]      
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(year,promedio_datos_anual_co,linewidth=5,c="green")
ax.set_title("Promedio anual de CO\n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Años",fontsize=15)
ax.set_ylabel("CO (µg/m³)",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=20)
plt.show()

promedio_datos_mensuales_co
meses=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(meses,promedio_datos_mensuales_co,linewidth=5,c="black")
ax.set_title("Promedio estacional de CO\n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Meses",fontsize=15)
ax.set_ylabel("CO (µg/m³)",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=15)
plt.show()

################################################
work="NO2.csv"
with open(work) as f:
    read=csv.reader(f)
    cabezera=next(read)
#se extrae todos los datos del archivo csv

    dates_no=[]
    no=[]
   
    for row in read:
        current_date_no=datetime.strptime(row[0],'%d/%m/%Y %H:%M')
        
        try:
            no_two=float(row[1])
            
        except ValueError:
            print(f"Missing data for {current_date_no}")
          
        else:
            dates_no.append(current_date_no)
            no.append(no_two)
   
cant_no=0
for i in dates_no:
    cant_no +=1
#hallando la lista de promedio anual para en los 9 años de registro:
#arreglo cant.datos
arreglo_cant_datos_anual_no=[]
#arreglo para datos de temperatura
promedio_datos_anual_no=[]
for a in range(2015,2020):
   #bucle para añadir informacion al  arreglo: 
    cant_datos_no=0
    suma_datos_no=0
    
    for i in range(0,cant_no):
        if dates_no[i].year==a:
            cant_datos_no+=1
            suma_datos_no=no[i]
                       
    prom_datos_anual_no=suma_datos_no/cant_datos_no
       
    #agregamos los valores a las listas de las variables halladas
    arreglo_cant_datos_anual_no.append(cant_datos_no)
    promedio_datos_anual_no.append(prom_datos_anual_no)
   

#hallando la lista de promedio de PM_10
arreglo_cant_datos_mensuales_no=[]
#arreglos mensuales para la precipitacion
promedio_datos_mensuales_no=[]
for i in range(1,13):
    cant_datos_mensual_no=0
    suma_datos_mensual_no=0
    for a in range(0,cant_no):
        if dates_no[a].month==i:
          cant_datos_mensual_no+=1
          suma_datos_mensual_no=no[a]
          
    promedio_datos_no=suma_datos_mensual_no/cant_datos_mensual_no
    
    #agregamos los valores a las listas de las variables halladas
    arreglo_cant_datos_mensuales_no.append(cant_datos_mensual_no)
    promedio_datos_mensuales_no.append(promedio_datos_no)

promedio_datos_anual_no
year=[2015,2016,2017,2018,2019]      
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(year,promedio_datos_anual_no,linewidth=5,c="green")
ax.set_title("Promedio anual de NO2\n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Años",fontsize=20)
ax.set_ylabel("NO2 (µg/m³)",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=20)
plt.show()

promedio_datos_mensuales_no
meses=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(meses,promedio_datos_mensuales_no,linewidth=5,c="black")
ax.set_title("Promedio estacional de NO2\n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Meses",fontsize=15)
ax.set_ylabel("NO2 (µg/m³)",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=15)
plt.show()

#########################################################################3
work="O3.csv"
with open(work) as f:
    read=csv.reader(f)
    cabezera=next(read)
#se extrae todos los datos del archivo csv

    dates_o=[]
    o=[]
   
    for row in read:
        current_date_o=datetime.strptime(row[0],'%d/%m/%Y %H:%M')
        
        try:
            o_3=float(row[1])
            
        except ValueError:
            print(f"Missing data for {current_date_o}")
          
        else:
            dates_o.append(current_date_o)
            o.append(o_3)
   
cant_o=0
for i in dates_o:
    cant_o +=1
#hallando la lista de promedio anual para en los 9 años de registro:
#arreglo cant.datos
arreglo_cant_datos_anual_o=[]
#arreglo para datos de temperatura
promedio_datos_anual_o=[]
for a in range(2015,2020):
   #bucle para añadir informacion al  arreglo: 
    cant_datos_o=0
    suma_datos_o=0
    
    for i in range(0,cant_o):
        if dates_o[i].year==a:
            cant_datos_o+=1
            suma_datos_o=o[i]
                       
    prom_datos_anual_o=suma_datos_o/cant_datos_o
       
    #agregamos los valores a las listas de las variables halladas
    arreglo_cant_datos_anual_o.append(cant_datos_o)
    promedio_datos_anual_o.append(prom_datos_anual_o)
   

#hallando la lista de promedio de PM_10
arreglo_cant_datos_mensuales_o=[]
#arreglos mensuales para la precipitacion
promedio_datos_mensuales_o=[]
for i in range(1,13):
    cant_datos_mensual_o=0
    suma_datos_mensual_o=0
    for a in range(0,cant_o):
        if dates_o[a].month==i:
          cant_datos_mensual_o+=1
          suma_datos_mensual_o=o[a]
          
    promedio_datos_o=suma_datos_mensual_o/cant_datos_mensual_o
    
    #agregamos los valores a las listas de las variables halladas
    arreglo_cant_datos_mensuales_o.append(cant_datos_mensual_o)
    promedio_datos_mensuales_o.append(promedio_datos_o)

promedio_datos_anual_o
year=[2015,2016,2017,2018,2019]      
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(year,promedio_datos_anual_o,linewidth=5,c="green")
ax.set_title("Promedio anual de O3\n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Años",fontsize=20)
ax.set_ylabel("O3 (µg/m³)",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=20)
ax.axis([2015,2019,0,0.015])
plt.show()

promedio_datos_mensuales_o
meses=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(meses,promedio_datos_mensuales_o,linewidth=5,c="black")
ax.set_title("Promedio estacional de O3\n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Meses",fontsize=15)
ax.set_ylabel("O3 (µg/m³)",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=15)
plt.show()

################################################################
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
