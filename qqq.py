import statistics
import csv 
import matplotlib.pyplot as plt
from datetime import datetime
from windrose import WindroseAxes
#se extrae la informacion del archivo csv
work="pp.csv"
#se extrae todos los datos del archivo csv para determinar cada variable:
#para Temperatura
   
        #para humedad

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
            print(f"Missing data for {current_date_dv}")        
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
            print(f"Missing data for {current_date_vv}")
#esos valores se añaden a las listas desde la linea 13 hasta la 19            
        else:
            dates_vv.append(current_date_vv)  
            velocidad_viento.append(v_v)

##########################################################################         
#bucle for para determinar la cantidad de datos "limpios" para cada variable


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
   
            
    for i in range(0,cant_dv):
        if dates_dv[i].year==a:
           
            cant_datos_dv+=1
            suma_datos_dv+=direccion_viento[i]
            
            
    for i in range(0,cant_vv):
        if dates_vv[i].year==a:
            
            cant_datos_vv+=1
            suma_datos_vv+=velocidad_viento[i]
          
            
            

    
   
    prom_datos_anual_dv=suma_datos_dv/cant_datos_dv
    prom_datos_anual_vv=suma_datos_vv/cant_datos_vv 
    #agregamos los valores a las listas de las variables halladas
    arreglo_cant_datos_anual_t.append(cant_datos_t)
    arreglo_cant_datos_anual_h.append(cant_datos_h)
    arreglo_cant_datos_anual_dv.append(cant_datos_dv)
    arreglo_cant_datos_anual_vv.append(cant_datos_vv)
    
    
  
   
    
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
    
    
    
    
            
    for a in range(0,cant_dv):
        if dates_dv[a].month==i:
            cant_datos_mensual_dv+=1
            suma_datos_mensual_dv+=direccion_viento[a]
            
            
    for a in range(0,cant_vv):
        if dates_vv[a].month==i:
            cant_datos_mensual_vv+=1
           
          
    
    promedio_datos_dv=suma_datos_dv/cant_datos_mensual_dv
    promedio_datos_vv=suma_datos_vv/cant_datos_mensual_vv
    #agregamos los valores a las listas de las variables halladas
    
    arreglo_cant_datos_mensuales_dv.append(cant_datos_mensual_dv)
    arreglo_cant_datos_mensuales_vv.append(cant_datos_mensual_vv)
    
    
    
   
    promedio_datos_mensuales_dv.append(promedio_datos_dv)
    promedio_datos_mensuales_vv.append(promedio_datos_vv)
print(promedio_datos_mensuales_vv)
print(promedio_datos_mensuales_dv)

ax = WindroseAxes.from_ax()
ax.bar(promedio_datos_anual_dv,promedio_datos_anual_vv, normed=True, opening=0.8, edgecolor='white')
ax.set_title("Rosa de viento promedio anual\n Est. Campo de Marte",fontsize=20)
ax.set_legend()
plt.show()

ax = WindroseAxes.from_ax()
ax.bar(promedio_datos_mensuales_dv,promedio_datos_mensuales_vv, normed=True, opening=0.8, edgecolor='yellow')
ax.set_title("Rosa de viento promedio mensual\n Est. Campo de Marte",fontsize=20)
ax.set_legend()
plt.show()