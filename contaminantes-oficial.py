import csv 
import matplotlib.pyplot as plt
from datetime import datetime
#se extrae la informacion del archivo csv

# # #################################################################################################

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
            pm_o=float(row[1])
            
        except ValueError:
            print(f"Missing data for {current_date_o}")
          
        else:
            dates_o.append(current_date_o)
            o.append(pm_o)
            
promedio_por_dia_o=[]
promedio_por_mes_o=[] 
promedio_por_año_o=[]
promedio_incas_o=[]

promedio_anual_datos_oficial_o=[]
n_dia_o=dates_o[0].day
n_hora_o=dates_o[0].day
#
n_mes_o=dates_o[0].month #primer mes que se evalua 
n_año_o=dates_o[0].year   
cant_datos_por_hora_mañana_o=0
suma_datos_por_hora_mañana_o=0
cant_datos_por_hora_tarde_o=0
suma_datos_por_hora_tarde_o=0
cant_datos_por_hora_noche_o=0
suma_datos_por_hora_noche_o=0
suma_datos_por_dia_o=0
cant_datos_en_dia_o= 0
suma_datos_por_mes_o=0
cant_datos_por_mes_o=0
suma_datos_por_año_o=0
cant_datos_por_año_o=0
# sumatoria de datos
cant_datos_totales_o=0
cambio_mes_año = True
sumatoria_anual_de_datos_o=0
cantidad_datos_promedio_anual=0
contador_o = 1
momento_de_borrar =True
booleano = False
datos_mayores_anuales_o=[]
datos_menores_anuales_o=[]
for i in range(0,10):
    promedio_por_mes_o.append(0)

for i in o:
    cant_datos_totales_o+=1
# hallar los promedios y lo guarda en una lista
for i in range(0,cant_datos_totales_o):
    # Cuando entra al condicional, es poruqe varia el mes
    
    if n_año_o==dates_o[i].year:
        
            #aqui se evalua para el 1er mes 
        if n_mes_o==dates_o[i].month:
            cant_datos_por_mes_o += 1
            suma_datos_por_mes_o+= o[i]
            if n_dia_o==dates_o[i].day: # n_dia_t = 13
                cant_datos_en_dia_o += 1
                suma_datos_por_dia_o+=o[i] # 220
                # cuando cambia del dia, entra al valor de else
                if dates_o[i].hour < 8:
                    cant_datos_por_hora_mañana_o+=1
                    suma_datos_por_hora_mañana_o+=o[i]
                    tempSuma = suma_datos_por_hora_mañana_o
                    cantTemp = cant_datos_por_hora_mañana_o
                    temp1 = o[i]
                elif dates_o[i].hour >=16:
                    cant_datos_por_hora_noche_o+=1
                    suma_datos_por_hora_noche_o+=o[i]
                    temp2 = o[i]
                else:
                    cant_datos_por_hora_tarde_o+=1
                    suma_datos_por_hora_tarde_o+=o[i]
                    temp3 = o[i]
                    
            else:
                #logica para dia
                promedio_o=(suma_datos_por_dia_o/cant_datos_en_dia_o)*100/150
                promedio_por_dia_o.append(promedio_o)
                suma_datos_por_dia_o= o[i] # 20
                cant_datos_en_dia_o = 1
                n_dia_o = dates_o[i].day
                #logica para incas
                if cant_datos_por_hora_mañana_o != 0:
                    promedio_inca_mañana_o=suma_datos_por_hora_mañana_o/cant_datos_por_hora_mañana_o
                else:
                    promedio_inca_mañana_o = 0
                if cant_datos_por_hora_tarde_o != 0:
                    promedio_inca_tarde_o=suma_datos_por_hora_tarde_o/cant_datos_por_hora_tarde_o
                else:
                    promedio_inca_tarde_o = 0
                if cant_datos_por_hora_noche_o != 0:
                    promedio_inca_noche_o=suma_datos_por_hora_noche_o/cant_datos_por_hora_noche_o
                else:
                    promedio_inca_noche_o = 0
                promedio_incas_o.append(promedio_inca_mañana_o)
                promedio_incas_o.append(promedio_inca_tarde_o)
                promedio_incas_o.append(promedio_inca_noche_o)
                cant_datos_por_hora_mañana_o=1
                cant_datos_por_hora_tarde_o=0
                cant_datos_por_hora_noche_o=0
                suma_datos_por_hora_mañana_o=o[i]
                suma_datos_por_hora_tarde_o=0
                suma_datos_por_hora_noche_o=0
        else:
          
            booleano = False
            promedio_o = suma_datos_por_mes_o/cant_datos_por_mes_o
            promedio_por_mes_o.append(promedio_o)
            sumatoria_anual_de_datos_o+=promedio_o
            diferencia = dates_o[i].month - n_mes_o
            if diferencia > 1 and booleano == False:
                for e in range(1,diferencia):
                    promedio_por_mes_o.append(0)
            cantidad_datos_promedio_anual+=1
            suma_datos_por_mes_o=o[i]
            cant_datos_por_mes_o=1
            n_mes_o=dates_o[i].month
            momento_de_borrar = True
    else:
        
        
        promedio_o = suma_datos_por_mes_o/cant_datos_por_mes_o
        promedio_por_mes_o.append(promedio_o)
        cont_meses_actuales = len(promedio_por_mes_o)%12
        diferencia2 = 12 - cont_meses_actuales
        if diferencia2 < 5:
            for e in range(0,diferencia2):
                promedio_por_mes_o.append(0)
        promedio_anual_o=sumatoria_anual_de_datos_o/cantidad_datos_promedio_anual
        promedio_anual_datos_oficial_o.append(promedio_anual_o)
        ceros = (12 - n_mes_o) + (dates_o[i].month-1) + (dates_o[i].year - n_año_o - 1)*12
        if (n_mes_o == 11):
            ceros -= 1
        if ceros > 0:
            booleano = True
        for x in range(0,ceros):
            promedio_por_mes_o.append(0)
        suma_datos_por_mes_o=o[i]
        cant_datos_por_mes_o=1
        n_año_o=dates_o[i].year
        n_mes_o=dates_o[i].month
        contador_o += 1

if cant_datos_por_hora_mañana_o != 0:
    promedio_inca_mañana_o=suma_datos_por_hora_mañana_o/cant_datos_por_hora_mañana_o
else:
    promedio_inca_mañana_o = 0
if cant_datos_por_hora_tarde_o != 0:
    promedio_inca_tarde_o=suma_datos_por_hora_tarde_o/cant_datos_por_hora_tarde_o
else:
    promedio_inca_tarde_o = 0
if cant_datos_por_hora_noche_o != 0:
    promedio_inca_noche_o=suma_datos_por_hora_noche_o/cant_datos_por_hora_noche_o
else:
    promedio_inca_noche_o = 0
promedio_incas_o.append(promedio_inca_mañana_o)
promedio_incas_o.append(promedio_inca_tarde_o)
promedio_incas_o.append(promedio_inca_noche_o)

promedio_o = suma_datos_por_mes_o/cant_datos_por_mes_o
promedio_por_mes_o.append(promedio_o)
promedio_anual_o=sumatoria_anual_de_datos_o/cantidad_datos_promedio_anual
promedio_anual_datos_oficial_o.append(promedio_anual_o)

# Hay datos vacios por lo que añado ceros al arreglos



for i in range(0,2):
    promedio_por_mes_o.append(0)
o_2015=promedio_por_mes_o[0:12]    
o_2016=promedio_por_mes_o[12:24]
o_2017=promedio_por_mes_o[24:36]
o_2018=promedio_por_mes_o[36:48]
o_2019=promedio_por_mes_o[48:60]


promedio_por_año_o.append(o_2015)
promedio_por_año_o.append(o_2016)
promedio_por_año_o.append(o_2017)
promedio_por_año_o.append(o_2018)
promedio_por_año_o.append(o_2019)

promedio_mensual_o= []
sumador_por_meses = []
sumador_o=0
contador_meses = 0

print((promedio_incas_o))
# print(len(promedio_por_dia_o))
print(temp1)
print(temp2)
print(temp3)
print(tempSuma) 
print(cantTemp)

for e in range(0,12):
    for i in promedio_por_año_o:
        sumador_o+= i[e]
        if i[e] != 0:
            contador_meses += 1
    promedio = sumador_o/contador_meses
    sumador_por_meses.append(sumador_o)
    promedio_mensual_o.append(promedio)
    sumador_o=0
    promedio= 0
    contador_meses = 0
    

promedio_datos_anual_o=promedio_anual_datos_oficial_o
year=[2015,2016,2017,2018,2019]      
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(year,promedio_datos_anual_o,linewidth=5,c="green")
ax.set_title("Promedio anual de O3\n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Años",fontsize=20)
ax.set_ylabel("O3 (µg/m³)",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=20)
ax.axis([2015,2019,5,25])
plt.show()


promedio_datos_mensuales_o=promedio_mensual_o
meses=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(meses,promedio_datos_mensuales_o,linewidth=5,c="black")
ax.set_title("Promedio estacional de O3\n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Meses",fontsize=15)
ax.set_ylabel("O3 (µg/m³)",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=15)
plt.show()    

# #############################################################
# work="SO.csv"
# with open(work) as f:
#     read=csv.reader(f)
#     cabezera=next(read)
# #se extrae todos los datos del archivo csv

#     dates_so=[]
#     so=[]
   
#     for row in read:
#         current_date_so=datetime.strptime(row[0],'%d/%m/%Y %H:%M')
        
#         try:
#             pm_so=float(row[1])
            
#         except ValueError:
#             print(f"Missing data for {current_date_so}")
          
#         else:
#             dates_so.append(current_date_so)
#             so.append(pm_so)
            
# promedio_por_dia_so=[]
# promedio_por_mes_so=[] 
# promedio_por_año_so=[]

# promedio_anual_datos_oficial_so=[]
# n_dia_so=dates_so[0].day
# #
# n_mes_so=dates_so[0].month #primer mes que se evalua 
# n_año_so=dates_so[0].year   
# suma_datos_por_dia_so=0
# cant_datos_en_dia_so= 0
# suma_datos_por_mes_so=0
# cant_datos_por_mes_so=0
# suma_datos_por_año_so=0
# cant_datos_por_año_so=0
# # sumatoria de datos
# cant_datos_totales_so=0
# cambio_mes_año = True
# sumatoria_anual_de_datos_so=0
# cantidad_datos_promedio_anual=0
# contador_so = 1
# momento_de_borrar =True
# booleano = False
# for i in range(0,15):
#     promedio_por_mes_so.append(0)

# for i in so:
#     cant_datos_totales_so+=1
# # hallar los promedios y lo guarda en una lista
# for i in range(0,cant_datos_totales_so):
#     # Cuando entra al condicional, es poruqe varia el mes
    
#     if n_año_so==dates_so[i].year:
        
#             #aqui se evalua para el 1er mes 
#         if n_mes_so==dates_so[i].month:
#             cant_datos_por_mes_so += 1
#             suma_datos_por_mes_so+= so[i]
#             # servira para INCAS
#             # if n_dia_t==dates_t[i].day: # n_dia_t = 13
#             #     cant_datos_en_dia_t += 1
#             #     suma_datos_por_dia_t+=temperatura[i] # 220
#             #     # cuando cambia del dia, entra al valor de else
#             # else:
#             #     promedio_t=suma_datos_por_dia_t/cant_datos_en_dia_t
#             #     promedio_por_dia_temperatura.append(promedio_t)
#             #     suma_datos_por_dia_t= temperatura[i] # 20
#             #     cant_datos_en_dia_t = 1
#             #     n_dia_t = dates_t[i].day
#         else:
          
#             booleano = False
#             promedio_so = suma_datos_por_mes_so/cant_datos_por_mes_so
#             promedio_por_mes_so.append(promedio_so)
#             sumatoria_anual_de_datos_so+=promedio_so
#             diferencia = dates_so[i].month - n_mes_so
#             if diferencia > 1 and booleano == False:
#                 for e in range(1,diferencia):
#                     promedio_por_mes_so.append(0)
#             cantidad_datos_promedio_anual+=1
#             suma_datos_por_mes_so=so[i]
#             cant_datos_por_mes_so=1
#             n_mes_so=dates_so[i].month
#             momento_de_borrar = True
#     else:
        
        
#         promedio_so = suma_datos_por_mes_so/cant_datos_por_mes_so
#         promedio_por_mes_so.append(promedio_so)
#         cont_meses_actuales = len(promedio_por_mes_so)%12
#         diferencia2 = 12 - cont_meses_actuales
#         if diferencia2 < 5:
#             for e in range(0,diferencia2):
#                 promedio_por_mes_so.append(0)
#         promedio_anual_so=sumatoria_anual_de_datos_so/cantidad_datos_promedio_anual
#         promedio_anual_datos_oficial_so.append(promedio_anual_so)
#         ceros = (12 - n_mes_so) + (dates_so[i].month-1) + (dates_so[i].year - n_año_so - 1)*12
#         if (n_mes_so == 11):
#             ceros -= 1
#         if ceros > 0:
#             booleano = True
#         for x in range(0,ceros):
#             promedio_por_mes_so.append(0)
#         suma_datos_por_mes_so=so[i]
#         cant_datos_por_mes_so=1
#         n_año_so=dates_so[i].year
#         n_mes_so=dates_so[i].month
#         contador_so += 1
        

# promedio_so = suma_datos_por_mes_so/cant_datos_por_mes_so
# promedio_por_mes_so.append(promedio_so)
# promedio_anual_so=sumatoria_anual_de_datos_so/cantidad_datos_promedio_anual
# promedio_anual_datos_oficial_so.append(promedio_anual_so)

# # Hay datos vacios por lo que añado ceros al arreglos

# #print(diccionario)
# #print(len(promedio_por_mes_temperatura))

# #print(promedio_por_año_termperatura)

# for i in range(0,26):
#     promedio_por_mes_so.append(0)
# so_2015=promedio_por_mes_so[0:12]    
# so_2016=promedio_por_mes_so[12:24]
# so_2017=promedio_por_mes_so[24:36]
# so_2018=promedio_por_mes_so[36:48]
# so_2019=promedio_por_mes_so[48:60]


# promedio_por_año_so.append(so_2015)
# promedio_por_año_so.append(so_2016)
# promedio_por_año_so.append(so_2017)
# promedio_por_año_so.append(so_2018)
# promedio_por_año_so.append(so_2019)

# promedio_mensual_so= []
# sumador_por_meses = []
# sumador_so=0
# contador_meses = 0


# for e in range(0,12):
#     for i in promedio_por_año_so:
#         sumador_so+= i[e]
#         if i[e] != 0:
#             contador_meses += 1
#     promedio = sumador_so/contador_meses
#     sumador_por_meses.append(sumador_so)
#     promedio_mensual_so.append(promedio)
#     sumador_so=0
#     promedio= 0
    
#     contador_meses = 0

####################################################


# work="PMT.csv"
# with open(work) as f:
#     read=csv.reader(f)
#     cabezera=next(read)
# #se extrae todos los datos del archivo csv
#     # rataza

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

# promedio_por_hora_pm_10=[]
# promedio_por_dia_pm_10=[]
# promedio_por_mes_pm_10=[] 
# promedio_por_año_pm_10=[]

# promedio_anual_datos_oficial_pm_10=[]

# n_dia_pm_10=dates_pm_10[0].day
# n_hora_pm_10=dates_pm_10[0].hour
# #
# n_mes_pm_10=dates_pm_10[0].month #primer mes que se evalua 
# n_año_pm_10=dates_pm_10[0].year  

# suma_datos_por_hora_pm_10=0
# cant_datos_por_hora_pm_10=1
# suma_datos_por_dia_pm_10=0
# cant_datos_en_dia_pm_10= 0
# suma_datos_por_mes_pm_10=0
# cant_datos_por_mes_pm_10=0
# suma_datos_por_año_pm_10=0
# cant_datos_por_año_pm_10=0
# # sumatoria de datos
# cant_datos_totales_pm_10=0
# cambio_mes_año = True
# sumatoria_anual_de_datos_pm_10=0
# cantidad_datos_promedio_anual=1
# contador_pm_10 = 1
# momento_de_borrar =True
# booleano = False
# for i in range(0,8):
#     promedio_por_mes_pm_10.append(0)

# for i in pm_10:
#     cant_datos_totales_pm_10+=1
# # hallar los promedios y lo guarda en una lista
# for i in range(0,cant_datos_totales_pm_10):
#     # Cuando entra al condicional, es poruqe varia el mes
    
#     if n_año_pm_10==dates_pm_10[i].year:
        
#             #aqui se evalua para el 1er mes 
#         if n_mes_pm_10==dates_pm_10[i].month:
#             cant_datos_por_mes_pm_10+= 1
#             suma_datos_por_mes_pm_10+= pm_10[i]
#             # servira para INCAS
#             if n_dia_pm_10==dates_pm_10[i].day: # n_dia_t = 13
#                 cant_datos_en_dia_pm_10 += 1
#                 suma_datos_por_dia_pm_10+=pm_10[i] # 220
#                 # cuando cambia del dia, entra al valor de else
#                 if n_hora_pm_10==dates_pm_10[i].hour:
#                     cant_datos_por_hora_pm_10+=1
#                     suma_datos_por_hora_pm_10+=pm_10[i]
#                 else:
#                     promedio_pm_10_por_hora=(suma_datos_por_hora_pm_10/cant_datos_por_hora_pm_10)*100/150
#                     promedio_por_hora_pm_10.append(promedio_pm_10_por_hora)
#                     suma_datos_por_hora_pm_10= pm_10[i] 
#                     cant_datos_por_hora_pm_10 = 1
#                     n_hora_pm_10 = dates_pm_10[i].hour
                    
                    
#             else:
#                 promedio_pm_10=(suma_datos_por_dia_pm_10/cant_datos_en_dia_pm_10)*100/150
#                 promedio_por_dia_pm_10.append(promedio_pm_10)
#                 suma_datos_por_dia_pm_10= pm_10[i] # 20
#                 cant_datos_en_dia_pm_10 = 1
#                 n_dia_pm_10 = dates_pm_10[i].day
#         else:
          
#             booleano = False
#             promedio_pm_10 = suma_datos_por_mes_pm_10/cant_datos_por_mes_pm_10
#             promedio_por_mes_pm_10.append(promedio_pm_10)
#             sumatoria_anual_de_datos_pm_10+=promedio_pm_10
#             diferencia = dates_pm_10[i].month - n_mes_pm_10
#             if diferencia > 1 and booleano == False:
#                 for e in range(1,diferencia):
#                     promedio_por_mes_pm_10.append(0)
#             cantidad_datos_promedio_anual+=1
#             suma_datos_por_mes_pm_10=pm_10[i]
#             cant_datos_por_mes_pm_10=1
#             n_mes_pm_10=dates_pm_10[i].month
#             momento_de_borrar = True
#     else:
        
        
#         promedio_pm_10 = suma_datos_por_mes_pm_10/cant_datos_por_mes_pm_10
#         promedio_por_mes_pm_10.append(promedio_pm_10)
#         cont_meses_actuales = len(promedio_por_mes_pm_10)%12
#         diferencia2 = 12 - cont_meses_actuales
#         if diferencia2 < 5:
#             for e in range(0,diferencia2):
#                 promedio_por_mes_pm_10.append(0)
#         promedio_anual_pm_10=sumatoria_anual_de_datos_pm_10/cantidad_datos_promedio_anual
#         promedio_anual_datos_oficial_pm_10.append(promedio_anual_pm_10)
#         ceros = (12 - n_mes_pm_10) + (dates_pm_10[i].month-1) + (dates_pm_10[i].year - n_año_pm_10 - 1)*12
#         if (n_mes_pm_10 == 11):
#             ceros -= 1
#         if ceros > 0:
#             booleano = True
#         for x in range(0,ceros):
#             promedio_por_mes_pm_10.append(0)
#         suma_datos_por_mes_pm_10=pm_10[i]
#         cant_datos_por_mes_pm_10=1
#         n_año_pm_10=dates_pm_10[i].year
#         n_mes_pm_10=dates_pm_10[i].month
#         contador_pm_10 += 1
        
# promedio_pm_10=(suma_datos_por_dia_pm_10/cant_datos_en_dia_pm_10)*100/150
# promedio_por_dia_pm_10.append(promedio_pm_10)
# promedio_pm_10 = suma_datos_por_mes_pm_10/cant_datos_por_mes_pm_10
# promedio_por_mes_pm_10.append(promedio_pm_10)
# promedio_anual_pm_10=sumatoria_anual_de_datos_pm_10/cantidad_datos_promedio_anual
# promedio_anual_datos_oficial_pm_10.append(promedio_anual_pm_10)

# # Hay datos vacios por lo que añado ceros al arreglos

# #print(diccionario)
# #print(len(promedio_por_mes_temperatura))

# #print(promedio_por_año_termperatura)

       
# pm_10_2010=promedio_por_mes_pm_10[0:12]
# pm_10_2011=promedio_por_mes_pm_10[12:24]
# pm_10_2012=promedio_por_mes_pm_10[24:36]
# pm_10_2013=promedio_por_mes_pm_10[36:48]
# pm_10_2014=promedio_por_mes_pm_10[48:60]
# pm_10_2015=promedio_por_mes_pm_10[60:75]
# pm_10_2016=promedio_por_mes_pm_10[72:84]
# pm_10_2017=promedio_por_mes_pm_10[84:96]
# pm_10_2018=promedio_por_mes_pm_10[96:108]
# pm_10_2019=promedio_por_mes_pm_10[108:120]


# promedio_por_año_pm_10.append(pm_10_2010)
# promedio_por_año_pm_10.append(pm_10_2011)
# promedio_por_año_pm_10.append(pm_10_2012)
# promedio_por_año_pm_10.append(pm_10_2013)
# promedio_por_año_pm_10.append(pm_10_2014)
# promedio_por_año_pm_10.append(pm_10_2015)
# promedio_por_año_pm_10.append(pm_10_2016)
# promedio_por_año_pm_10.append(pm_10_2017)
# promedio_por_año_pm_10.append(pm_10_2018)
# promedio_por_año_pm_10.append(pm_10_2019)

# promedio_anual_datos_oficial_pm_10.clear()
# promedio_anual_temporal = 0
# for i in promedio_por_año_pm_10:
#     for x in i:
#         promedio_anual_temporal += x
#     promedio_anual_datos_oficial_pm_10.append(promedio_anual_temporal/12)
#     promedio_anual_temporal = 0

# promedio_mensual_pm_10= []
# sumador_por_meses = []
# sumador_pm_10=0
# contador_meses = 0

# for e in range(0,12):
#     for i in promedio_por_año_pm_10:
#         sumador_pm_10+= i[e]
#         if i[e] != 0:
#             contador_meses += 1
#     promedio = sumador_pm_10/contador_meses
#     sumador_por_meses.append(sumador_pm_10)
#     promedio_mensual_pm_10.append(promedio)
#     sumador_pm_10=0
#     promedio= 0
#     contador_meses = 0
# print(promedio_mensual_pm_10)

# promedio_anual_inca_pm_10=[]
# promedio_mensual_inca_pm_10=[]
# #PARA HALLAR VALORES INCAS
# for i in promedio_anual_datos_oficial_pm_10:
#     inca_pm_10=i*100/150
#     promedio_anual_inca_pm_10.append(inca_pm_10)

# for i in promedio_mensual_pm_10:
#     inca_pm_10=i*100/150
#     promedio_mensual_inca_pm_10.append(inca_pm_10)


# work="PM2.csv"
# with open(work) as f:
#     read=csv.reader(f)
#     cabezera=next(read)
# #se extrae todos los datos del archivo csv
#     # rataza

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

# promedio_por_dia_pm_2=[]
# promedio_por_mes_pm_2=[] 
# promedio_por_año_pm_2=[]

# promedio_anual_datos_oficial_pm_2=[]
# n_dia_so=dates_pm_2[0].day
# #
# n_mes_pm_2=dates_pm_2[0].month #primer mes que se evalua 
# n_año_pm_2=dates_pm_2[0].year   
# suma_datos_por_dia_pm_2=0
# cant_datos_en_dia_pm_2= 0
# suma_datos_por_mes_pm_2=0
# cant_datos_por_mes_pm_2=0
# suma_datos_por_año_pm_2=0
# cant_datos_por_año_pm_2=0
# # sumatoria de datos
# cant_datos_totales_pm_2=0
# cambio_mes_año = True
# sumatoria_anual_de_datos_pm_2=0
# cantidad_datos_promedio_anual=0
# contador_pm_2 = 1
# momento_de_borrar =True
# booleano = False
# for i in range(0,9):
#     promedio_por_mes_pm_2.append(0)

# for i in pm_2:
#     cant_datos_totales_pm_2+=1
# # hallar los promedios y lo guarda en una lista
# for i in range(0,cant_datos_totales_pm_2):
#     # Cuando entra al condicional, es poruqe varia el mes
    
#     if n_año_pm_2==dates_pm_2[i].year:
        
#             #aqui se evalua para el 1er mes 
#         if n_mes_pm_2==dates_pm_2[i].month:
#             cant_datos_por_mes_pm_2+= 1
#             suma_datos_por_mes_pm_2+= pm_2[i]
#             # servira para INCAS
#             # if n_dia_t==dates_t[i].day: # n_dia_t = 13
#             #     cant_datos_en_dia_t += 1
#             #     suma_datos_por_dia_t+=temperatura[i] # 220
#             #     # cuando cambia del dia, entra al valor de else
#             # else:
#             #     promedio_t=suma_datos_por_dia_t/cant_datos_en_dia_t
#             #     promedio_por_dia_temperatura.append(promedio_t)
#             #     suma_datos_por_dia_t= temperatura[i] # 20
#             #     cant_datos_en_dia_t = 1
#             #     n_dia_t = dates_t[i].day
#         else:
          
#             booleano = False
#             promedio_pm_2 = suma_datos_por_mes_pm_2/cant_datos_por_mes_pm_2
#             promedio_por_mes_pm_2.append(promedio_pm_2)
#             sumatoria_anual_de_datos_pm_2+=promedio_pm_2
#             diferencia = dates_pm_2[i].month - n_mes_pm_2
#             if diferencia > 1 and booleano == False:
#                 for e in range(1,diferencia):
#                     promedio_por_mes_pm_2.append(0)
#             cantidad_datos_promedio_anual+=1
#             suma_datos_por_mes_pm_2=pm_2[i]
#             cant_datos_por_mes_pm_2=1
#             n_mes_pm_2=dates_pm_2[i].month
#             momento_de_borrar = True
#     else:
        
        
#         promedio_pm_2 = suma_datos_por_mes_pm_2/cant_datos_por_mes_pm_2
#         promedio_por_mes_pm_2.append(promedio_pm_2)
#         cont_meses_actuales = len(promedio_por_mes_pm_2)%12
#         diferencia2 = 12 - cont_meses_actuales
#         if diferencia2 < 5:
#             for e in range(0,diferencia2):
#                 promedio_por_mes_pm_2.append(0)
#         promedio_anual_pm_2=sumatoria_anual_de_datos_pm_2/cantidad_datos_promedio_anual
#         promedio_anual_datos_oficial_pm_2.append(promedio_anual_pm_2)
#         ceros = (12 - n_mes_pm_2) + (dates_pm_2[i].month-1) + (dates_pm_2[i].year - n_año_pm_2 - 1)*12
#         if (n_mes_pm_2 == 11):
#             ceros -= 1
#         if ceros > 0:
#             booleano = True
#         for x in range(0,ceros):
#             promedio_por_mes_pm_2.append(0)
#         suma_datos_por_mes_pm_2=pm_2[i]
#         cant_datos_por_mes_pm_2=1
#         n_año_pm_2=dates_pm_2[i].year
#         n_mes_pm_2=dates_pm_2[i].month
#         contador_pm_2 += 1
        

# promedio_pm_2 = suma_datos_por_mes_pm_2/cant_datos_por_mes_pm_2
# promedio_por_mes_pm_2.append(promedio_pm_2)
# promedio_anual_pm_2=sumatoria_anual_de_datos_pm_2/cantidad_datos_promedio_anual
# promedio_anual_datos_oficial_pm_2.append(promedio_anual_pm_2)

# # Hay datos vacios por lo que añado ceros al arreglos

# #print(diccionario)
# #print(len(promedio_por_mes_temperatura))

# #print(promedio_por_año_termperatura)
# for i in range(0,4):
#     promedio_por_mes_pm_2.append(0)
    

# pm_2_2014=promedio_por_mes_pm_2[0:12]
# pm_2_2015=promedio_por_mes_pm_2[12:24]
# pm_2_2016=promedio_por_mes_pm_2[24:36]
# pm_2_2017=promedio_por_mes_pm_2[36:48]
# pm_2_2018=promedio_por_mes_pm_2[48:64]
# pm_2_2019=promedio_por_mes_pm_2[60:72]


# promedio_por_año_pm_2.append(pm_2_2014)
# promedio_por_año_pm_2.append(pm_2_2015)
# promedio_por_año_pm_2.append(pm_2_2016)
# promedio_por_año_pm_2.append(pm_2_2017)
# promedio_por_año_pm_2.append(pm_2_2018)
# promedio_por_año_pm_2.append(pm_2_2019)

# promedio_mensual_pm_2= []
# sumador_por_meses = []
# sumador_pm_2=0
# contador_meses = 0

# for e in range(0,12):
#     for i in promedio_por_año_pm_2:
#         sumador_pm_2+= i[e]
#         if i[e] != 0:
#             contador_meses += 1
#     promedio = sumador_pm_2/contador_meses
#     sumador_por_meses.append(sumador_pm_2)
#     promedio_mensual_pm_2.append(promedio)
#     sumador_pm_2=0
#     promedio= 0
#     contador_meses = 0

# print(promedio_por_mes_pm_2)

# work="NO2.csv"
# with open(work) as f:
#     read=csv.reader(f)
#     cabezera=next(read)
# #se extrae todos los datos del archivo csv

#     dates_no=[]
#     no=[]
   
#     for row in read:
#         current_date_no=datetime.strptime(row[0],'%d/%m/%Y %H:%M')
        
#         try:
#             no_two=float(row[1])
            
#         except ValueError:
#             print(f"Missing data for {current_date_no}")
          
#         else:
#             dates_no.append(current_date_no)
#             no.append(no_two)

# promedio_por_hora_no=[]
# promedio_por_dia_no=[]
# promedio_por_mes_no=[] 
# promedio_por_año_no=[]

# promedio_anual_datos_oficial_no=[]
# n_dia_no=dates_no[0].day
# #
# n_mes_no=dates_no[0].month #primer mes que se evalua 
# n_año_no=dates_no[0].year   
# suma_datos_por_dia_no=0
# cant_datos_en_dia_no= 0
# suma_datos_por_mes_no=0
# cant_datos_por_mes_no=0
# suma_datos_por_año_no=0
# cant_datos_por_año_no=0

# cant_datos_por_hora_no=1
# suma_datos_por_hora_no=0


# # sumatoria de datos
# cant_datos_totales_no=0
# cambio_mes_año = True
# sumatoria_anual_de_datos_no=0
# cantidad_datos_promedio_anual=0
# contador_no = 1
# momento_de_borrar =True
# booleano = False
# for i in range(0,10):
#     promedio_por_mes_no.append(0)

# for i in no:
#     cant_datos_totales_no+=1
# # hallar los promedios y lo guarda en una lista
# for i in range(0,cant_datos_totales_no):
#     # Cuando entra al condicional, es poruqe varia el mes
    
#     if n_año_no==dates_no[i].year:
        
#             #aqui se evalua para el 1er mes 
#         if n_mes_no==dates_no[i].month:
#             cant_datos_por_mes_no += 1
#             suma_datos_por_mes_no+= no[i]
#             # servira para INCAS
            
            
            
                                    
            
                                        
#         else:
          
#             booleano = False
#             promedio_no = suma_datos_por_mes_no/cant_datos_por_mes_no
#             promedio_por_mes_no.append(promedio_no)
#             sumatoria_anual_de_datos_no+=promedio_no
#             diferencia = dates_no[i].month - n_mes_no
#             if diferencia > 1 and booleano == False:
#                 for e in range(1,diferencia):
#                     promedio_por_mes_no.append(0)
#             cantidad_datos_promedio_anual+=1
#             suma_datos_por_mes_no=no[i]
#             cant_datos_por_mes_no=1
#             n_mes_no=dates_no[i].month
#             momento_de_borrar = True
#     else:
        
        
#         promedio_no = suma_datos_por_mes_no/cant_datos_por_mes_no
#         promedio_por_mes_no.append(promedio_no)
#         cont_meses_actuales = len(promedio_por_mes_no)%12
#         diferencia2 = 12 - cont_meses_actuales
#         if diferencia2 < 5:
#             for e in range(0,diferencia2):
#                 promedio_por_mes_no.append(0)
#         promedio_anual_no=sumatoria_anual_de_datos_no/cantidad_datos_promedio_anual
#         promedio_anual_datos_oficial_no.append(promedio_anual_no)
#         ceros = (12 - n_mes_no) + (dates_no[i].month-1) + (dates_no[i].year - n_año_no - 1)*12
#         if (n_mes_no == 11):
#             ceros -= 1
#         if ceros > 0:
#             booleano = True
#         for x in range(0,ceros):
#             promedio_por_mes_no.append(0)
#         suma_datos_por_mes_no=no[i]
#         cant_datos_por_mes_no=1
#         n_año_no=dates_no[i].year
#         n_mes_no=dates_no[i].month
#         contador_no += 1
        
# for i in range (0,cant_datos_totales_no):
#     if n_dia_no==dates_no[i].hour:
#         cant_datos_por_hora_no+=1
#         suma_datos_por_hora_no+=no[i]
#     else:
#         promedio_no_hora=(suma_datos_por_hora_no/cant_datos_por_hora_no)*100/200
#         promedio_por_hora_no.append(promedio_no_hora)
#         suma_datos_por_hora_no= no[i] 
#         cant_datos_por_hora_no = 1
#         n_hora_no = dates_no[i].hour
# promedio_por_hora_no.append(no[cant_datos_totales_no-1]*100/200)

# promedio_no = suma_datos_por_mes_no/cant_datos_por_mes_no
# promedio_por_mes_no.append(promedio_no)
# promedio_anual_no=sumatoria_anual_de_datos_no/cantidad_datos_promedio_anual
# promedio_anual_datos_oficial_no.append(promedio_anual_no)
# print(promedio_por_hora_no)

# # Hay datos vacios por lo que añado ceros al arreglos

# #print(diccionario)
# #print(len(promedio_por_mes_temperatura))

# #print(promedio_por_año_termperatura)

# for i in range(0,2):
#     promedio_por_mes_no.append(0)
    
# no_2015=promedio_por_mes_no[0:12]
# no_2016=promedio_por_mes_no[12:24]
# no_2017=promedio_por_mes_no[24:36]
# no_2018=promedio_por_mes_no[36:48]
# no_2019=promedio_por_mes_no[48:60]


# promedio_por_año_no.append(no_2015)
# promedio_por_año_no.append(no_2016)
# promedio_por_año_no.append(no_2017)
# promedio_por_año_no.append(no_2018)
# promedio_por_año_no.append(no_2019)

# promedio_mensual_no= []
# sumador_por_meses = []
# sumador_no=0
# contador_meses = 0

# for e in range(0,12):
#     for i in promedio_por_año_no:
#         sumador_no+= i[e]
#         if i[e] != 0:
#             contador_meses += 1
#     promedio = sumador_no/contador_meses
#     sumador_por_meses.append(sumador_no)
#     promedio_mensual_no.append(promedio)
#     sumador_no=0
#     promedio= 0
#     contador_meses = 0
# print(promedio_por_hora_no)
# work="CO.csv"
# with open(work) as f:
#     read=csv.reader(f)
#     cabezera=next(read)
# #se extrae todos los datos del archivo csv

#     dates_co=[]
#     co=[]
   
#     for row in read:
#         current_date_co=datetime.strptime(row[0],'%d/%m/%Y %H:%M')
        
#         try:
#             pm_c=float(row[1])
            
#         except ValueError:
#             print(f"Missing data for {current_date_co}")
          
#         else:
#             dates_co.append(current_date_co)
#             co.append(pm_c)
# promedio_por_dia_co=[]
# promedio_por_mes_co=[] 
# promedio_por_año_co=[]

# promedio_anual_datos_oficial_co=[]
# n_dia_co=dates_co[0].day
# #
# n_mes_co=dates_co[0].month #primer mes que se evalua 
# n_año_co=dates_co[0].year   
# suma_datos_por_dia_co=0
# cant_datos_en_dia_co= 0
# suma_datos_por_mes_co=0
# cant_datos_por_mes_co=0
# suma_datos_por_año_co=0
# cant_datos_por_año_co=0
# # sumatoria de datos
# cant_datos_totales_co=0
# cambio_mes_año = True
# sumatoria_anual_de_datos_co=0
# cantidad_datos_promedio_anual=0
# contador_co = 1
# momento_de_borrar =True
# booleano = False
# for i in range(0,10):
#     promedio_por_mes_co.append(0)

# for i in co:
#     cant_datos_totales_co+=1
# # hallar los promedios y lo guarda en una lista
# for i in range(0,cant_datos_totales_co):
# #     # Cuando entra al condicional, es poruqe varia el mes
    
#     if n_año_co==dates_co[i].year:
        
#             #aqui se evalua para el 1er mes 
#         if n_mes_co==dates_co[i].month:
#             cant_datos_por_mes_co += 1
#             suma_datos_por_mes_co+= co[i]
#             # servira para INCAS
#             # if n_dia_t==dates_t[i].day: # n_dia_t = 13
#             #     cant_datos_en_dia_t += 1
#             #     suma_datos_por_dia_t+=temperatura[i] # 220
#             #     # cuando cambia del dia, entra al valor de else
#             # else:
#             #     promedio_t=suma_datos_por_dia_t/cant_datos_en_dia_t
#             #     promedio_por_dia_temperatura.append(promedio_t)
#             #     suma_datos_por_dia_t= temperatura[i] # 20
#             #     cant_datos_en_dia_t = 1
#             #     n_dia_t = dates_t[i].day
#         else:
          
#             booleano = False
#             promedio_co = suma_datos_por_mes_co/cant_datos_por_mes_co
#             promedio_por_mes_co.append(promedio_co)
#             sumatoria_anual_de_datos_co+=promedio_co
#             diferencia = dates_co[i].month - n_mes_co
#             if diferencia > 1 and booleano == False:
#                 for e in range(1,diferencia):
#                     promedio_por_mes_co.append(0)
#             cantidad_datos_promedio_anual+=1
#             suma_datos_por_mes_co=co[i]
#             cant_datos_por_mes_co=1
#             n_mes_co=dates_co[i].month
#             momento_de_borrar = True
#     else:
        
        
#         promedio_co = suma_datos_por_mes_co/cant_datos_por_mes_co
#         promedio_por_mes_co.append(promedio_co)
#         cont_meses_actuales = len(promedio_por_mes_co)%12
#         diferencia2 = 12 - cont_meses_actuales
#         if diferencia2 < 5:
#             for e in range(0,diferencia2):
#                 promedio_por_mes_co.append(0)
#         promedio_anual_co=sumatoria_anual_de_datos_co/cantidad_datos_promedio_anual
#         promedio_anual_datos_oficial_co.append(promedio_anual_co)
#         ceros = (12 - n_mes_co) + (dates_co[i].month-1) + (dates_co[i].year - n_año_co - 1)*12
#         if (n_mes_co == 11):
#             ceros -= 1
#         if ceros > 0:
#             booleano = True
#         for x in range(0,ceros):
#             promedio_por_mes_co.append(0)
#         suma_datos_por_mes_co=co[i]
#         cant_datos_por_mes_co=1
#         n_año_co=dates_co[i].year
#         n_mes_co=dates_co[i].month
#         contador_co += 1
        

# promedio_co = suma_datos_por_mes_co/cant_datos_por_mes_co
# promedio_por_mes_co.append(promedio_co)
# promedio_anual_co=sumatoria_anual_de_datos_co/cantidad_datos_promedio_anual
# promedio_anual_datos_oficial_co.append(promedio_anual_co)



# for i in range(0,6):
#     promedio_por_mes_co.append(0)

# co_2015=promedio_por_mes_co[0:12]
# co_2016=promedio_por_mes_co[12:24]
# co_2017=promedio_por_mes_co[24:36]
# co_2018=promedio_por_mes_co[36:48]
# co_2019=promedio_por_mes_co[48:60]


# promedio_por_año_co.append(co_2015)
# promedio_por_año_co.append(co_2016)
# promedio_por_año_co.append(co_2017)
# promedio_por_año_co.append(co_2018)
# promedio_por_año_co.append(co_2019)

# promedio_mensual_co= []
# sumador_por_meses = []
# sumador_co=0
# contador_meses = 0


# for e in range(0,12):
#     for i in promedio_por_año_co:
#         sumador_co+= i[e]
#         if i[e] != 0:
#             contador_meses += 1
#     promedio = sumador_co/contador_meses
#     sumador_por_meses.append(sumador_co)
#     promedio_mensual_co.append(promedio)
#     sumador_co=0
#     promedio= 0
#     contador_meses = 0
# print(promedio_por_mes_co)