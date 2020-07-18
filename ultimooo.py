import csv 
import matplotlib.pyplot as plt
from datetime import datetime




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


arreglo_datos_suma_dia=[]
arreglo_datos_promedio_dia=[]
arreglo_datos_suma_mes_2017 = []
arreglo_datos_suma_mes_2018 = []
arreglo_datos_suma_mes_2019 = []
arreglo_datos_promedio_mes_inca=[]
arreglo_datos_suma_anio = []
arreglo_datos_promedio_anio_inca= []
arreglo_datos_inca_inicial = []  
arreglo_datos_inca_medio = [] 
arreglo_datos_inca_final = []  
 
# año 2017
for mes in range(1,13):   
    arreglo_datos_suma_dia.clear()                
    for dia in range(1,32):
        #bucle para añadir informacion al  arreglo: 
        suma_datos_dia = 0
        cant_datos_dia = 0
        suma_datos_inca_inicial = 0
        suma_datos_inca_medio = 0
        suma_datos_inca_final = 0
        cant_inicial = 0
        cant_medio = 0
        cant_final = 0
        
        
        for i in range(0,cant_no):
            if dates_no[i].year==2017:
                if dates_no[i].month==mes:
                    if dates_no[i].day==dia:
                        suma_datos_dia += no[i]
                        if dates_no[i].hour <= 8.00:
                            suma_datos_inca_inicial += no[i]
                            cant_inicial += 1
                        elif dates_no[i].hour > 16:
                            suma_datos_inca_final += no[i]
                            cant_final += 1
                        else:
                            suma_datos_inca_medio += no[i]
                            cant_medio += 1
        if (cant_inicial != 0):
            arreglo_datos_inca_inicial.append(suma_datos_inca_inicial/cant_inicial)
        if (cant_medio != 0):
            arreglo_datos_inca_medio.append(suma_datos_inca_medio/cant_medio)
        if (cant_final != 0):
            arreglo_datos_inca_final.append(suma_datos_inca_final/cant_final)
        arreglo_datos_suma_dia.append(suma_datos_dia)
    arreglo_datos_suma_mes_2017.append(arreglo_datos_suma_dia)
print(arreglo_datos_suma_mes_2017)
# # año 2018
# for mes in range(1,13):   
#     arreglo_datos_suma_dia.clear()                
#     for dia in range(1,32):
#         #bucle para añadir informacion al  arreglo: 
#         suma_datos_dia = 0
#         cant_datos_dia = 0
#         suma_datos_inca_inicial = 0
#         suma_datos_inca_medio = 0
#         suma_datos_inca_final = 0
#         cant_inicial = 0
#         cant_medio = 0
#         cant_final = 0
        
        
#         for i in range(0,cant_no):
#             if dates_no[i].year==2018:
#                 if dates_no[i].month==mes:
#                     if dates_no[i].day==dia:
#                         suma_datos_dia += no[i]
#                         if dates_no[i].hour <= 8.00:
#                             suma_datos_inca_inicial += no[i]
#                             cant_inicial += 1
#                         elif dates_no[i].hour > 16:
#                             suma_datos_inca_final += no[i]
#                             cant_final += 1
#                         else:
#                             suma_datos_inca_medio += no[i]
#                             cant_medio += 1
#         if (cant_inicial != 0):
#             arreglo_datos_inca_inicial.append(suma_datos_inca_inicial/cant_inicial)
#         if (cant_medio != 0):
#             arreglo_datos_inca_medio.append(suma_datos_inca_medio/cant_medio)
#         if (cant_final != 0):
#             arreglo_datos_inca_final.append(suma_datos_inca_final/cant_final)
#         arreglo_datos_suma_dia.append(suma_datos_dia)
#     arreglo_datos_suma_mes_2018.append(arreglo_datos_suma_dia)
  
# # año 2019
# # for mes in range(1,13):   
# #     arreglo_datos_suma_dia.clear()                
# #     for dia in range(1,32):
#         #bucle para añadir informacion al  arreglo: 
#         suma_datos_dia = 0
#         cant_datos_dia = 0
#         suma_datos_inca_inicial = 0
#         suma_datos_inca_medio = 0
#         suma_datos_inca_final = 0
#         cant_inicial = 0
#         cant_medio = 0
#         cant_final = 0
        
        
#         for i in range(0,cant_no):
#             if dates_no[i].year==2019:
#                 if dates_no[i].month==mes:
#                     if dates_no[i].day==dia:
#                         suma_datos_dia += no[i]
#                         if dates_no[i].hour <= 8.00:
#                             suma_datos_inca_inicial += no[i]
#                             cant_inicial += 1
#                         elif dates_no[i].hour > 16:
#                             suma_datos_inca_final += no[i]
#                             cant_final += 1
#                         else:
#                             suma_datos_inca_medio += no[i]
#                             cant_medio += 1
#         if (cant_inicial != 0):
#             arreglo_datos_inca_inicial.append(suma_datos_inca_inicial/cant_inicial)
#         if (cant_medio != 0):
#             arreglo_datos_inca_medio.append(suma_datos_inca_medio/cant_medio)
#         if (cant_final != 0):
#             arreglo_datos_inca_final.append(suma_datos_inca_final/cant_final)
#         arreglo_datos_suma_dia.append(suma_datos_dia)
#     arreglo_datos_suma_mes_2019.append(arreglo_datos_suma_dia)
    

# promedio_anual = 0
# for a in arreglo_datos_suma_mes_2018:
#     promedio = 0
#     cantidad = 0
#     suma = 0
#     for x in a:
#         suma += x
#         cantidad += 1
#     promedio = suma/cantidad
#     promedio_anual += promedio
# promedio_anual = promedio_anual/12

# print(promedio_anual)
        
# for a in range(2015,2020):
#     #bucle para añadir informacion al  arreglo: 
#     cant_datos_no=0
#     suma_datos_no=0
    
#     for i in range(0,cant_no):
#         if dates_no[i].year==a:
#             cant_datos_no+=1
#             suma_datos_no=no[i]
                       
#     prom_datos_anual_no=suma_datos_no/cant_datos_no
       
#     #agregamos los valores a las listas de las variables halladas
#     arreglo_cant_datos_anual_no.append(cant_datos_no)
#     promedio_datos_anual_no.append(prom_datos_anual_no)
   

# #hallando la lista de promedio de PM_10
# arreglo_cant_datos_mensuales_no=[]
# #arreglos mensuales para la precipitacion
# promedio_datos_mensuales_no=[]
# for i in range(1,13):
#     cant_datos_mensual_no=0
#     suma_datos_mensual_no=0
#     for a in range(0,cant_no):
#         if dates_no[a].month==i:
#           cant_datos_mensual_no+=1
#           suma_datos_mensual_no=no[a]
          
#     promedio_datos_no=suma_datos_mensual_no/cant_datos_mensual_no
    
#     #agregamos los valores a las listas de las variables halladas
#     arreglo_cant_datos_mensuales_no.append(cant_datos_mensual_no)
#     promedio_datos_mensuales_no.append(promedio_datos_no)
