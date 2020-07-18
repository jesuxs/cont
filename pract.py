import csv 
import matplotlib.pyplot as plt
from datetime import datetime
# #se extrae la informacion del archivo csv
# work="PMT.csv"
# with open(work) as f:
#     read=csv.reader(f)
#     cabezera=next(read)
# #se extrae todos los datos del archivo csv

#     dates_pm_10=[]
#     pm_10=[]
   
#     for row in read:
#         current_date_pm_10=datetime.strptime(row[0],'%d/%m/%Y %H:%M')
        
#         try:
#             pm_ten=float(row[1])
            
#         except ValueError:
#             print(f"Missing data for {current_date_pm_10}")
          
#         else:
#             dates_pm_10.append(current_date_pm_10)
#             pm_10.append(pm_ten)
   
# cant_pm_10=0
# for i in dates_pm_10:
#     cant_pm_10+=1
# #hallando la lista de promedio anual para en los 9 años de registro:
# #arreglo cant.datos
# arreglo_cant_datos_anual_pm_10=[]
# #arreglo para datos de temperatura
# promedio_datos_anual_pm_10=[]
# datos_menores_anuales_pm_10=[]
# datos_mayores_anuales_pm_10=[]
# for a in range(2010,2020):
#    #bucle para añadir informacion al  arreglo: 
#     cant_datos_pm_10=0
#     suma_datos_pm_10=0
#     ma=0
#     me=1000
    
#     for i in range(0,cant_pm_10):
#         if dates_pm_10[i].year==a:
#             cant_datos_pm_10+=1
#             suma_datos_pm_10+=pm_10[i]
#             if ma<pm_10[i]:
#                 ma=pm_10[i]
                
#             if me>pm_10[i]:
#                 me=pm_10[i]
                       
#     prom_datos_anual_pm_10=suma_datos_pm_10/cant_datos_pm_10
       
#     #agregamos los valores a las listas de las variables halladas
#     arreglo_cant_datos_anual_pm_10.append(cant_datos_pm_10)
#     promedio_datos_anual_pm_10.append(prom_datos_anual_pm_10)
#     datos_mayores_anuales_pm_10.append(ma)
#     datos_menores_anuales_pm_10.append(me)

# year=[]
# for a in range(2009,2019):
#     a=a+1
#     year.append(a)

# plt.style.use('seaborn')
# fig,ax=plt.subplots()

# ax.plot(year,datos_mayores_anuales_pm_10,c="blue",linewidth=5)
# ax.plot(year, promedio_datos_anual_pm_10,c="red",linewidth=5)
# ax.plot(year,datos_menores_anuales_pm_10,c="green",linewidth=5)
# ax.set_title("Promedio anual de PM 10 \n E.'Campo de Marte'",fontsize=20)
# ax.set_xlabel("Años",fontsize=15)
# ax.set_ylabel("PM 10 (µg/m³)",fontsize=20)
# ax.tick_params(axis="both",which="major",labelsize=15)
# ax.axis([2010,2019,0,400])


# plt.plot(datos_mayores_anuales_pm_10,label="Tmax")
# plt.plot(datos_menores_anuales_pm_10, label = "Tmin")
# plt.plot(promedio_datos_anual_pm_10, label = "Tprom")

# plt.legend()
# plt.show()           

   
#hallando la lista de promedio de PM_10
# arreglo_cant_datos_mensuales_pm_10=[]
# #arreglos mensuales para la precipitacion
# promedio_datos_mensuales_pm_10=[]
# promedio_datos_mensuales_pm_10=[]
# maximo_datos_mensuales_pm_10=[]
# minimo_datos_mensuales_pm_10=[]
# for i in range(1,13):
#     cant_datos_mensual_pm_10=0
#     suma_datos_mensual_pm_10=0
#     ma=0
#     me=1000 
#     for a in range(0,cant_pm_10):
#         if dates_pm_10[a].month==i:
#           cant_datos_mensual_pm_10+=1
#           suma_datos_mensual_pm_10+=pm_10[a]
#           if ma<pm_10[a]:
#                 ma=pm_10[a]
                
#           if me>pm_10[a]:
#                 me=pm_10[a]
          
#     promedio_datos_pm_10=suma_datos_mensual_pm_10/cant_datos_mensual_pm_10
    
#     #agregamos los valores a las listas de las variables halladas
#     arreglo_cant_datos_mensuales_pm_10.append(cant_datos_mensual_pm_10)
#     promedio_datos_mensuales_pm_10.append(promedio_datos_pm_10)
        
    
#     maximo_datos_mensuales_pm_10.append(ma)
#     minimo_datos_mensuales_pm_10.append(me)

# promedio_datos_mensuales_pm_10
# meses=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
# fig,ax=plt.subplots()
# plt.style.use("seaborn")
# ax.plot(meses,maximo_datos_mensuales_pm_10,linewidth=5,c="red")
# ax.plot(meses,promedio_datos_mensuales_pm_10,linewidth=5,c="blue")
# ax.plot(meses,minimo_datos_mensuales_pm_10,linewidth=5,c="green")


# ax.set_title("Promedio estacional de PM 10 \n E.'Campo de Marte'",fontsize=20)
# ax.set_xlabel("Meses",fontsize=15)
# ax.set_ylabel("PM 10 (µg/m³)",fontsize=15)
# ax.tick_params(axis="both",which="major",labelsize=15)

# plt.plot(promedio_datos_mensuales_pm_10,label = "PM10_prom")

# plt.plot(minimo_datos_mensuales_pm_10,label="PM10_Min")
# plt.plot(maximo_datos_mensuales_pm_10,label="PM10_Max")
# plt.legend()

# plt.show()

# work="PM2.csv"
# with open(work) as f:
#     read=csv.reader(f)
#     cabezera=next(read)
# #se extrae todos los datos del archivo csv

#     dates_pm_2=[]
#     pm_2=[]
   
#     for row in read:
#         current_date_pm_2=datetime.strptime(row[0],'%d/%m/%Y %H:%M')
        
#         try:
#             pm_two=float(row[1])
            
#         except ValueError:
#             print(f"Missing data for {current_date_pm_2}")
          
#         else:
#             dates_pm_2.append(current_date_pm_2)
#             pm_2.append(pm_two)
   
# cant_pm_2=0
# for i in dates_pm_2:
#     cant_pm_2+=1
# #hallando la lista de promedio anual para en los 9 años de registro:
# #arreglo cant.datos
# arreglo_cant_datos_anual_pm_2=[]
# #arreglo para datos de temperatura
# promedio_datos_anual_pm_2=[]
# datos_menores_anuales_pm_2=[]
# datos_mayores_anuales_pm_2=[]
# for a in range(2014,2020):
#    #bucle para añadir informacion al  arreglo: 
#     cant_datos_pm_2=0
#     suma_datos_pm_2=0
#     ma=0
#     me=1000
    
#     for i in range(0,cant_pm_2):
#         if dates_pm_2[i].year==a:
#             cant_datos_pm_2+=1
#             suma_datos_pm_2+=pm_2[i]
#             if ma<pm_2[i]:
#                 ma=pm_2[i]
                
#             if me>pm_2[i]:
#                 me=pm_2[i]
                       
#     prom_datos_anual_pm_2=suma_datos_pm_2/cant_datos_pm_2
       
#     #agregamos los valores a las listas de las variables halladas
#     arreglo_cant_datos_anual_pm_2.append(cant_datos_pm_2)
#     promedio_datos_anual_pm_2.append(prom_datos_anual_pm_2)
#     datos_mayores_anuales_pm_2.append(ma)
#     datos_menores_anuales_pm_2.append(me)


# year_2=[]
# for a in range(2013,2019):
#     a=a+1
#     year_2.append(a)
# print(year_2)

# plt.style.use('seaborn')
# fig,ax=plt.subplots()


# ax.plot(year_2,datos_mayores_anuales_pm_2,c="blue",linewidth=5)
# ax.plot(year_2, promedio_datos_anual_pm_2,c="red",linewidth=5)
# ax.plot(year_2,datos_menores_anuales_pm_2,c="green",linewidth=5)
# ax.set_title("Promedio anual de PM2 \n E.'Campo de Marte'",fontsize=20)
# ax.set_xlabel("Años",fontsize=15)
# ax.set_ylabel("PM 2 (µg/m³)",fontsize=20)
# ax.tick_params(axis="both",which="major",labelsize=15)
# ax.axis([2014,2019,0,120])


# plt.plot(datos_mayores_anuales_pm_2,label="PM2_Max")
# plt.plot(datos_menores_anuales_pm_2, label ="PM2_Min")
# plt.plot(promedio_datos_anual_pm_2, label ="PM2_Prom")

# plt.legend()
# plt.show()

# #hallando la lista de promedio de PM_10
# arreglo_cant_datos_mensuales_pm_2=[]
# #arreglos mensuales para la precipitacion
# promedio_datos_mensuales_pm_2=[]
# promedio_datos_mensuales_pm_2=[]
# maximo_datos_mensuales_pm_2=[]
# minimo_datos_mensuales_pm_2=[]
# for i in range(1,13):
#     cant_datos_mensual_pm_2=0
#     suma_datos_mensual_pm_2=0
#     ma=0
#     me=1000 
#     for a in range(0,cant_pm_2):
#         if dates_pm_2[a].month==i:
#           cant_datos_mensual_pm_2+=1
#           suma_datos_mensual_pm_2+=pm_2[a]
    #       if ma<pm_2[a]:
    #             ma=pm_2[a]
                
    #       if me>pm_2[a]:
    #             me=pm_2[a]
          
    # promedio_datos_pm_2=suma_datos_mensual_pm_2/cant_datos_mensual_pm_2
    
    # #agregamos los valores a las listas de las variables halladas
    # arreglo_cant_datos_mensuales_pm_2.append(cant_datos_mensual_pm_2)
    # promedio_datos_mensuales_pm_2.append(promedio_datos_pm_2)
        
    
    # maximo_datos_mensuales_pm_2.append(ma)
    # minimo_datos_mensuales_pm_2.append(me)

# promedio_datos_mensuales_pm_2
# meses=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
# fig,ax=plt.subplots()
# plt.style.use("seaborn")
# ax.plot(meses,maximo_datos_mensuales_pm_2,linewidth=5,c="red")
# ax.plot(meses,promedio_datos_mensuales_pm_2,linewidth=5,c="blue")
# ax.plot(meses,minimo_datos_mensuales_pm_2,linewidth=5,c="green")


# ax.set_title("Promedio estacional de PM2\n E.'Campo de Marte'",fontsize=20)
# ax.set_xlabel("Meses",fontsize=15)
# ax.set_ylabel("PM2(µg/m³)",fontsize=20)
# ax.tick_params(axis="both",which="major",labelsize=15)

# plt.plot(promedio_datos_mensuales_pm_2,label = "PM2_prom")

# plt.plot(minimo_datos_mensuales_pm_2,label="PM2_Min")
# plt.plot(maximo_datos_mensuales_pm_2,label="PM2_Max")
# plt.legend() 

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
datos_menores_anuales_co=[]
datos_mayores_anuales_co=[]
for a in range(2015,2020):
   #bucle para añadir informacion al  arreglo: 
    cant_datos_co=0
    suma_datos_co=0
    ma=0
    me=1000
    
    for i in range(0,cant_co):
        if dates_co[i].year==a:
            cant_datos_co+=1
            suma_datos_co=pm_co[i]
            
            if ma<pm_co[i]:
                ma=pm_co[i]
                
            if me>pm_co[i]:
                 me=pm_co[i]

                          
            
    
    datos_mayores_anuales_co.append(ma)
    
    datos_menores_anuales_co.append(me)
                           
    prom_datos_anual_co=suma_datos_co/cant_datos_co
       
    #agregamos los valores a las listas de las variables halladas
    arreglo_cant_datos_anual_co.append(cant_datos_co)
    promedio_datos_anual_co.append(prom_datos_anual_co)
print(datos_mayores_anuales_co)  
print(datos_menores_anuales_co)
print(promedio_datos_anual_co)
          
   
   
    

# #hallando la lista de promedio de PM_10
# arreglo_cant_datos_mensuales_co=[]
# #arreglos mensuales para la precipitacion
# promedio_datos_mensuales_co=[]
# for i in range(1,13):
#     cant_datos_mensual_co=0
#     suma_datos_mensual_co=0
#     for a in range(0,cant_co):
#         if dates_co[a].month==i:
#           cant_datos_mensual_co+=1
#           suma_datos_mensual_co=pm_co[a]
          
#     promedio_datos_co=suma_datos_mensual_co/cant_datos_mensual_co
    
#     #agregamos los valores a las listas de las variables halladas
#     arreglo_cant_datos_mensuales_co.append(cant_datos_mensual_co)
#     promedio_datos_mensuales_co.append(promedio_datos_co)

# promedio_datos_anual_co
# year=[2015,2016,2017,2018,2019]      
# fig,ax=plt.subplots()
# plt.style.use("seaborn")
# ax.plot(year,promedio_datos_anual_co,linewidth=5,c="green")
# ax.set_title("Promedio anual de CO\n E.'Campo de Marte'",fontsize=20)
# ax.set_xlabel("Años",fontsize=15)
# ax.set_ylabel("CO (µg/m³)",fontsize=20)
# ax.tick_params(axis="both",which="major",labelsize=20)
# plt.show()

# promedio_datos_mensuales_co
# meses=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
# fig,ax=plt.subplots()
# plt.style.use("seaborn")
# ax.plot(meses,promedio_datos_mensuales_co,linewidth=5,c="black")
# ax.set_title("Promedio estacional de CO\n E.'Campo de Marte'",fontsize=20)
# ax.set_xlabel("Meses",fontsize=15)
# ax.set_ylabel("CO (µg/m³)",fontsize=20)
# ax.tick_params(axis="both",which="major",labelsize=15)
# plt.show()    
