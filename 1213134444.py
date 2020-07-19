
import csv 
#import matplotlib.pyplot as plt
from datetime import datetime
#se extrae la informacion del archivo csv
work="real.csv"
# se extrae todos los datos del archivo csv para determinar cada variable:
# para Temperatura
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

promedio_por_dia_temperatura=[]  
promedio_por_mes_temperatura=[]   
promedio_por_año_termperatura=[]
maximos_mensuales_temperatura=[]
maximos_anuales_temperatura=[]
minimos_mensuales_temperatura=[]
minimos_anuales_temperatura=[]

promedio_anual_datos_oficial_temperatura=[]   
n_dia_t=dates_t[0].day
#
n_mes_t=dates_t[0].month #primer mes que se evalua 
n_año_t=dates_t[0].year   
suma_datos_por_dia_t=0
cant_datos_en_dia_t = 0
suma_datos_por_mes_t=0
cant_datos_por_mes_t=0
suma_datos_por_año_t=0
cant_datos_por_año_t=0
# sumatoria de datos
cant_datos_totales_t=0
cambio_mes_año = True
sumatoria_anual_de_datos_temperatura=0
cantidad_datos_promedio_anual=0
max_mensual_temperatura=0
max_anual_temperatura=0
min_mensual_temperatura=100000
min_anual_temperatura=100000
contador = 1
momento_de_borrar =True
datos_mayores_anuales_t=[]
datos_menores_anuales_t=[]
for i in temperatura:
    cant_datos_totales_t+=1
# hallar los promedios y lo guarda en una lista
for i in range(0,cant_datos_totales_t):
    # Cuando entra al condicional, es poruqe varia el mes
    
    if n_año_t==dates_t[i].year:
        
            #aqui se evalua para el 1er mes 
        if n_mes_t==dates_t[i].month:
            cant_datos_por_mes_t += 1
            suma_datos_por_mes_t+= temperatura[i]
            
            #max y min
            if (temperatura[i] > max_mensual_temperatura):
                max_mensual_temperatura = temperatura[i]
            if (temperatura[i] < min_mensual_temperatura and temperatura[i] != 0):
                min_mensual_temperatura = temperatura[i]
            if (temperatura[i] > max_anual_temperatura):
                max_anual_temperatura = temperatura[i]
            if (temperatura[i] < min_anual_temperatura and temperatura[i] != 0):
                min_anual_temperatura = temperatura[i]
            
            
            # servira para INCAS
            # if n_dia_t==dates_t[i].day: # n_dia_t = 13
            #     cant_datos_en_dia_t += 1
            #     suma_datos_por_dia_t+=temperatura[i] # 220
            #     # cuando cambia del dia, entra al valor de else
            # else:
            #     promedio_t=suma_datos_por_dia_t/cant_datos_en_dia_t
            #     promedio_por_dia_temperatura.append(promedio_t)
            #     suma_datos_por_dia_t= temperatura[i] # 20
            #     cant_datos_en_dia_t = 1
            #     n_dia_t = dates_t[i].day
        else:
            diferencia = dates_t[i].month - n_mes_t
            if diferencia > 1:
                for e in range(1,diferencia):
                    promedio_por_mes_temperatura.append(0)
          
            promedio_t = suma_datos_por_mes_t/cant_datos_por_mes_t
            promedio_por_mes_temperatura.append(promedio_t)
            maximos_mensuales_temperatura.append(max_mensual_temperatura)
            max_mensual_temperatura = 0
            minimos_mensuales_temperatura.append(min_mensual_temperatura)
            min_mensual_temperatura = 100000
            sumatoria_anual_de_datos_temperatura+=promedio_t
            cantidad_datos_promedio_anual+=1
            suma_datos_por_mes_t=temperatura[i]
            cant_datos_por_mes_t=1
            n_mes_t=dates_t[i].month
            momento_de_borrar = True
    else:
        promedio_t = suma_datos_por_mes_t/cant_datos_por_mes_t
        promedio_por_mes_temperatura.append(promedio_t)
        maximos_anuales_temperatura.append(max_anual_temperatura)
        max_anual_temperatura=0
        minimos_anuales_temperatura.append(min_anual_temperatura)
        min_anual_temperatura=100000
        cont_meses_actuales = len(promedio_por_mes_temperatura)%12
        diferencia2 = 12 - cont_meses_actuales
        if diferencia2 < 5:
            for e in range(0,diferencia2):
                promedio_por_mes_temperatura.append(0)
                
        promedio_anual_t=sumatoria_anual_de_datos_temperatura/cantidad_datos_promedio_anual
        promedio_anual_datos_oficial_temperatura.append(promedio_anual_t)
        suma_datos_por_mes_t=temperatura[i]
        cant_datos_por_mes_t=1
        n_año_t=dates_t[i].year
        n_mes_t=dates_t[i].month
        contador += 1
        
            
        ma=0
        me=1000
        for i in range(0,cant_datos_totales_t):
            if dates_t[i].year==n_año_t:
                            
                if ma<temperatura[i]:
                    ma=temperatura[i]
                    
                if me>temperatura[i]:
                    me=temperatura[i]
        
        datos_mayores_anuales_t.append(ma)
        datos_menores_anuales_t.append(me)
        

promedio_t = suma_datos_por_mes_t/cant_datos_por_mes_t
promedio_por_mes_temperatura.append(promedio_t)
promedio_anual_t=sumatoria_anual_de_datos_temperatura/cantidad_datos_promedio_anual
promedio_anual_datos_oficial_temperatura.append(promedio_anual_t)
maximos_mensuales_temperatura.append(max_mensual_temperatura)
minimos_mensuales_temperatura.append(min_mensual_temperatura)
maximos_anuales_temperatura.append(max_anual_temperatura)
minimos_anuales_temperatura.append(min_anual_temperatura)

# Hay datos vacios por lo que añado ceros al arreglos

#print(diccionario)
#print(len(promedio_por_mes_temperatura))

#print(promedio_por_año_termperatura)

for i in range(0,4):
    promedio_por_mes_temperatura.append(0)
    
t_2010=promedio_por_mes_temperatura[0:12]
t_2011=promedio_por_mes_temperatura[12:24]
t_2012=promedio_por_mes_temperatura[24:36]
t_2013=promedio_por_mes_temperatura[36:48]
t_2014=promedio_por_mes_temperatura[48:60]
t_2015=promedio_por_mes_temperatura[60:72]
t_2016=promedio_por_mes_temperatura[72:84]
t_2017=promedio_por_mes_temperatura[84:96]
t_2018=promedio_por_mes_temperatura[96:108]
t_2019=promedio_por_mes_temperatura[108:120]

promedio_por_año_termperatura.append(t_2010)
promedio_por_año_termperatura.append(t_2011)
promedio_por_año_termperatura.append(t_2012)
promedio_por_año_termperatura.append(t_2013)
promedio_por_año_termperatura.append(t_2014)
promedio_por_año_termperatura.append(t_2015)
promedio_por_año_termperatura.append(t_2016)
promedio_por_año_termperatura.append(t_2017)
promedio_por_año_termperatura.append(t_2018)
promedio_por_año_termperatura.append(t_2019)

promedio_mensual_temperatura= []
sumador_por_meses = []
sumador_t=0
contador_meses = 0
for e in range(0,12):
    for i in promedio_por_año_termperatura:
        sumador_t+= i[e]
        if i[e] != 0:
            contador_meses += 1
    promedio = sumador_t/contador_meses
    sumador_por_meses.append(sumador_t)
    promedio_mensual_temperatura.append(promedio)
    sumador_t=0
    promedio = 0
    contador_meses = 0

#print(maximos_mensuales_temperatura)
#print(minimos_mensuales_temperatura)

with open(work) as f:
    read=csv.reader(f)
    cabezera=next(read)


    dates_h=[]
    humedad=[]
    for row in read:
        current_date_h=datetime.strptime(row[0],'%d/%m/%Y')
        try:
            h=float(row[3])
            
#codigo para eliminar datos vacios            
        except ValueError:
            print(f"Missing data for {current_date_h}")
#esos valores se añaden a las listas desde la linea 13 hasta la 19            
        else:
            dates_h.append(current_date_h)
            humedad.append(h)  

promedio_por_dia_humedad=[]  
promedio_por_mes_humedad=[]   
promedio_por_año_humedad=[]
maximos_mensuales_humedad=[]
maximos_anuales_humedad=[]
minimos_mensuales_humedad=[]
minimos_anuales_humedad=[]


promedio_anual_datos_oficial_humedad=[]   
n_dia_h=dates_h[0].day
#
n_mes_h=dates_h[0].month #primer mes que se evalua 
n_año_h=dates_h[0].year   
suma_datos_por_dia_h=0
cant_datos_en_dia_h = 0
suma_datos_por_mes_h=0
cant_datos_por_mes_h=0
suma_datos_por_año_h=0
cant_datos_por_año_h=0
# sumatoria de datos
cant_datos_totales_h=0
max_mensual_humedad=0
max_anual_humedad=0
min_mensual_humedad=100000
min_anual_humedad=100000
cambio_mes_año = True
sumatoria_anual_de_datos_humedad=0
cantidad_datos_promedio_anual=0
contador = 1
momento_de_borrar =True
datos_mayores_anuales_h=[]
datos_menores_anuales_h=[]
for i in humedad:
    cant_datos_totales_h+=1
# hallar los promedios y lo guarda en una lista
for i in range(0,cant_datos_totales_h):
    # Cuando entra al condicional, es poruqe varia el mes
    
    if n_año_h==dates_h[i].year:
        
            #aqui se evalua para el 1er mes 
        if n_mes_h==dates_h[i].month:
            cant_datos_por_mes_h += 1
            suma_datos_por_mes_h+= humedad[i]
            
            #max y min
            if (humedad[i] > max_mensual_humedad):
                max_mensual_humedad = humedad[i]
            if (humedad[i] < min_mensual_humedad and humedad[i] != 0):
                min_mensual_humedad = humedad[i]
            if (humedad[i] > max_anual_humedad):
                max_anual_humedad = humedad[i]
            if (humedad[i] < min_anual_humedad and humedad[i] != 0):
                min_anual_humedad = humedad[i]
            
            
            # servira para INCAS
            # if n_dia_t==dates_t[i].day: # n_dia_t = 13
            #     cant_datos_en_dia_t += 1
            #     suma_datos_por_dia_t+=temperatura[i] # 220
            #     # cuando cambia del dia, entra al valor de else
            # else:
            #     promedio_t=suma_datos_por_dia_t/cant_datos_en_dia_t
            #     promedio_por_dia_temperatura.append(promedio_t)
            #     suma_datos_por_dia_t= temperatura[i] # 20
            #     cant_datos_en_dia_t = 1
            #     n_dia_t = dates_t[i].day
        else:
            diferencia = dates_h[i].month - n_mes_h
            if diferencia > 1:
                for e in range(1,diferencia):
                    promedio_por_mes_humedad.append(0)
          
            promedio_h = suma_datos_por_mes_h/cant_datos_por_mes_h
            promedio_por_mes_humedad.append(promedio_h)
            maximos_mensuales_humedad.append(max_mensual_humedad)
            max_mensual_humedad = 0
            minimos_mensuales_humedad.append(min_mensual_humedad)
            min_mensual_humedad = 100000
            sumatoria_anual_de_datos_humedad+=promedio_h
            cantidad_datos_promedio_anual+=1
            suma_datos_por_mes_h=humedad[i]
            cant_datos_por_mes_h=1
            n_mes_h=dates_h[i].month
            momento_de_borrar = True
    else:
        promedio_h = suma_datos_por_mes_h/cant_datos_por_mes_h
        promedio_por_mes_humedad.append(promedio_h)
        maximos_anuales_humedad.append(max_anual_humedad)
        max_anual_humedad=0
        minimos_anuales_humedad.append(min_anual_humedad)
        min_anual_humedad=100000
        cont_meses_actuales = len(promedio_por_mes_humedad)%12
        diferencia2 = 12 - cont_meses_actuales
        if diferencia2 < 5:
            for e in range(0,diferencia2):
                promedio_por_mes_humedad.append(0)
        promedio_anual_h=sumatoria_anual_de_datos_humedad/cantidad_datos_promedio_anual
        promedio_anual_datos_oficial_humedad.append(promedio_anual_h)
        suma_datos_por_mes_h=humedad[i]
        cant_datos_por_mes_h=1
        n_año_h=dates_h[i].year
        n_mes_h=dates_h[i].month
        contador += 1
      
        ma=0
        me=1000
        for i in range(0,cant_datos_totales_h):
            if dates_h[i].year==n_año_h:
            
               
                if ma<humedad[i]:
                    ma=humedad[i]
                    
                if me>humedad[i]:
                    me=humedad[i]
        
        datos_mayores_anuales_h.append(ma)
        datos_menores_anuales_h.append(me)
        

promedio_h = suma_datos_por_mes_h/cant_datos_por_mes_h
promedio_por_mes_humedad.append(promedio_h)
promedio_anual_h=sumatoria_anual_de_datos_humedad/cantidad_datos_promedio_anual
promedio_anual_datos_oficial_humedad.append(promedio_anual_h)
maximos_mensuales_humedad.append(max_mensual_humedad)
minimos_mensuales_humedad.append(min_mensual_humedad)
maximos_anuales_humedad.append(max_anual_humedad)
minimos_anuales_humedad.append(min_anual_humedad)

# Hay datos vacios por lo que añado ceros al arreglos

#print(diccionario)
#print(len(promedio_por_mes_temperatura))

#print(promedio_por_año_termperatura)

for i in range(0,4):
    promedio_por_mes_humedad.append(0)
    
h_2010=promedio_por_mes_humedad[0:12]
h_2011=promedio_por_mes_humedad[12:24]
h_2012=promedio_por_mes_humedad[24:36]
h_2013=promedio_por_mes_humedad[36:48]
h_2014=promedio_por_mes_humedad[48:60]
h_2015=promedio_por_mes_humedad[60:72]
h_2016=promedio_por_mes_humedad[72:84]
h_2017=promedio_por_mes_humedad[84:96]
h_2018=promedio_por_mes_humedad[96:108]
h_2019=promedio_por_mes_humedad[108:120]

promedio_por_año_humedad.append(h_2010)
promedio_por_año_humedad.append(h_2011)
promedio_por_año_humedad.append(h_2012)
promedio_por_año_humedad.append(h_2013)
promedio_por_año_humedad.append(h_2014)
promedio_por_año_humedad.append(h_2015)
promedio_por_año_humedad.append(h_2016)
promedio_por_año_humedad.append(h_2017)
promedio_por_año_humedad.append(h_2018)
promedio_por_año_humedad.append(h_2019)


promedio_mensual_humedad=[]
sumador_por_meses = []
sumador_h=0
contador_meses = 0

#print(maximos_mensuales_humedad)
#print(minimos_mensuales_humedad)    

for e in range(0,12):
    for i in promedio_por_año_humedad:
        sumador_h+= i[e]
        if i[e] != 0:
            contador_meses += 1
    promedio = sumador_h/contador_meses
    sumador_por_meses.append(sumador_h)
    
    promedio_mensual_humedad.append(promedio)
    
    sumador_h=0
    promedio = 0
    contador_meses = 0

with open(work) as f:
    read=csv.reader(f)
    cabezera=next(read)


    dates_d=[]
    direccion=[]
    for row in read:
        current_date_d=datetime.strptime(row[0],'%d/%m/%Y')
                
        try:
            d=float(row[5])            
#codigo para eliminar datos vacios            
        except ValueError:
            print(f"Missing data for {current_date_d}")
#esos valores se añaden a las listas desde la linea 13 hasta la 19            
        else:
            dates_d.append(current_date_d)
            direccion.append(d)  

promedio_por_dia_direccion=[]
promedio_por_mes_direccion=[]  
promedio_por_año_direccion=[]
maximos_mensuales_direccion=[]
maximos_anuales_direccion=[]
minimos_mensuales_direccion=[]
minimos_anuales_direccion=[]


promedio_anual_datos_oficial_direccion=[]
n_dia_d=dates_d[0].day
#
n_mes_d=dates_d[0].month #primer mes que se evalua 
n_año_d=dates_d[0].year   
suma_datos_por_dia_d=0
cant_datos_en_dia_d = 0
suma_datos_por_mes_d=0
cant_datos_por_mes_d=0
suma_datos_por_año_d=0
cant_datos_por_año_d=0
# sumatoria de datos
cant_datos_totales_d=0
max_mensual_direccion=0
max_anual_direccion=0
min_mensual_direccion=100000
min_anual_direccion=100000
cambio_mes_año = True
sumatoria_anual_de_datos_direccion=0
cantidad_datos_promedio_anual=0
contador_d=1
momento_de_borrar =True
datos_mayores_anuales_d=[]
datos_menores_anuales_d=[]
for i in direccion:
    cant_datos_totales_d+=1
# hallar los promedios y lo guarda en una lista
for i in range(0,cant_datos_totales_d):
    # Cuando entra al condicional, es poruqe varia el mes
    
    if n_año_d==dates_d[i].year:
        
            #aqui se evalua para el 1er mes 
        if n_mes_d==dates_d[i].month:
            cant_datos_por_mes_d += 1
            suma_datos_por_mes_d+= direccion[i]
            
            #max y min
            if (direccion[i] > max_mensual_direccion):
                max_mensual_direccion = direccion[i]
            if (direccion[i] < min_mensual_direccion and direccion[i] != 0):
                min_mensual_direccion = direccion[i]
            if (direccion[i] > max_anual_direccion):
                max_anual_direccion = direccion[i]
            if (direccion[i] < min_anual_direccion and direccion[i] != 0):
                min_anual_direccion = direccion[i]
            
            
            # servira para INCAS
            # if n_dia_t==dates_t[i].day: # n_dia_t = 13
            #     cant_datos_en_dia_t += 1
            #     suma_datos_por_dia_t+=temperatura[i] # 220
            #     # cuando cambia del dia, entra al valor de else
            # else:
            #     promedio_t=suma_datos_por_dia_t/cant_datos_en_dia_t
            #     promedio_por_dia_temperatura.append(promedio_t)
            #     suma_datos_por_dia_t= temperatura[i] # 20
            #     cant_datos_en_dia_t = 1
            #     n_dia_t = dates_t[i].day
        else:
            diferencia = dates_d[i].month - n_mes_d
            if diferencia > 1:
                for e in range(1,diferencia):
                    promedio_por_mes_direccion.append(0)
          
            promedio_d = suma_datos_por_mes_d/cant_datos_por_mes_d
            promedio_por_mes_direccion.append(promedio_d)
            maximos_mensuales_direccion.append(max_mensual_direccion)
            max_mensual_direccion = 0
            minimos_mensuales_direccion.append(min_mensual_direccion)
            min_mensual_direccion = 100000
            sumatoria_anual_de_datos_direccion+=promedio_d
            cantidad_datos_promedio_anual+=1
            suma_datos_por_mes_d=direccion[i]
            cant_datos_por_mes_d=1
            n_mes_d=dates_d[i].month
            momento_de_borrar = True
    else:
        promedio_d = suma_datos_por_mes_d/cant_datos_por_mes_d
        promedio_por_mes_direccion.append(promedio_d)
        maximos_anuales_direccion.append(max_anual_direccion)
        max_anual_direccion=0
        minimos_anuales_direccion.append(min_anual_direccion)
        min_anual_direccion=100000
        cont_meses_actuales = len(promedio_por_mes_direccion)%12
        diferencia2 = 12 - cont_meses_actuales
        if diferencia2 < 5:
            for e in range(0,diferencia2):
                promedio_por_mes_direccion.append(0)
        promedio_anual_d=sumatoria_anual_de_datos_direccion/cantidad_datos_promedio_anual
        promedio_anual_datos_oficial_direccion.append(promedio_anual_d)
        suma_datos_por_mes_d=direccion[i]
        cant_datos_por_mes_d=1
        n_año_d=dates_d[i].year
        n_mes_d=dates_d[i].month
        contador_d+= 1
        ma=0
        me=1000
        for i in range(0,cant_datos_totales_d):
            if dates_d[i].year==n_año_d:
                
                sumatoria_anual_de_datos_direccion+=direccion[i]
                
                if ma<direccion[i]:
                      ma=direccion[i]
                     
                if me>direccion[i]:
                    me=direccion[i]
                
        datos_mayores_anuales_d.append(ma)
        datos_menores_anuales_d.append(me)
        

promedio_d = suma_datos_por_mes_d/cant_datos_por_mes_d
promedio_por_mes_direccion.append(promedio_d)
promedio_anual_d=sumatoria_anual_de_datos_direccion/cantidad_datos_promedio_anual
promedio_anual_datos_oficial_direccion.append(promedio_anual_d)
maximos_mensuales_direccion.append(max_mensual_direccion)
minimos_mensuales_direccion.append(min_mensual_direccion)
maximos_anuales_direccion.append(max_anual_direccion)
minimos_anuales_direccion.append(min_anual_direccion)

# Hay datos vacios por lo que añado ceros al arreglos

#print(diccionario)
#print(len(promedio_por_mes_temperatura))

#print(promedio_por_año_termperatura)

for i in range(0,4):
    promedio_por_mes_direccion.append(0)
    
    

d_2010=promedio_por_mes_direccion[0:12]   

d_2011=promedio_por_mes_direccion[12:24]
d_2012=promedio_por_mes_direccion[24:36]
d_2013=promedio_por_mes_direccion[36:48]
d_2014=promedio_por_mes_direccion[48:60]
d_2015=promedio_por_mes_direccion[60:72]
d_2016=promedio_por_mes_direccion[72:84]
d_2017=promedio_por_mes_direccion[84:96]
d_2018=promedio_por_mes_direccion[96:108]
d_2019=promedio_por_mes_direccion[108:120]

promedio_por_año_direccion.append(d_2010)
promedio_por_año_direccion.append(d_2011)
promedio_por_año_direccion.append(d_2012)
promedio_por_año_direccion.append(d_2013)
promedio_por_año_direccion.append(d_2014)
promedio_por_año_direccion.append(d_2015)
promedio_por_año_direccion.append(d_2016)
promedio_por_año_direccion.append(d_2017)
promedio_por_año_direccion.append(d_2018)
promedio_por_año_direccion.append(d_2019)


promedio_mensual_direccion=[]
sumador_por_meses = []
sumador_d=0
contador_meses = 0

for e in range(0,12):
    for i in promedio_por_año_direccion:
        sumador_d+= i[e]
        if i[e] != 0:
            contador_meses += 1
    promedio = sumador_d/contador_meses
    sumador_por_meses.append(sumador_d)
    
    promedio_mensual_direccion.append(promedio)
    
    sumador_d=0
    promedio = 0
    contador_meses = 0

#print(maximos_mensuales_direccion)
#print(minimos_mensuales_direccion) 


with open(work) as f:
    read=csv.reader(f)
    cabezera=next(read)


    dates_v=[]
    velocidad=[]
    for row in read:
        current_date_v=datetime.strptime(row[0],'%d/%m/%Y')
        try:
            v=float(row[6])
            
#codigo para eliminar datos vacios            
        except ValueError:
            print(f"Missing data for {current_date_v}")
#esos valores se añaden a las listas desde la linea 13 hasta la 19            
        else:
            dates_v.append(current_date_v)
            velocidad.append(v) 

promedio_por_dia_velocidad=[]
promedio_por_mes_velocidad=[]
promedio_por_año_velocidad=[]
maximos_mensuales_velocidad=[]
maximos_anuales_velocidad=[]
minimos_mensuales_velocidad=[]
minimos_anuales_velocidad=[]


promedio_anual_datos_oficial_velocidad=[]
n_dia_v=dates_v[0].day
#
n_mes_v=dates_v[0].month #primer mes que se evalua 
n_año_v=dates_v[0].year   
suma_datos_por_dia_v=0
cant_datos_en_dia_v = 0
suma_datos_por_mes_v=0
cant_datos_por_mes_v=0
suma_datos_por_año_v=0
cant_datos_por_año_v=0
# sumatoria de datos
cant_datos_totales_v=0
max_mensual_velocidad=0
max_anual_velocidad=0
min_mensual_velocidad=100000
min_anual_velocidad=100000
cambio_mes_año = True
sumatoria_anual_de_datos_velocidad=0
cantidad_datos_promedio_anual=0
contador_v=1
momento_de_borrar =True
datos_mayores_anuales_v=[]
datos_menores_anuales_v=[]
for i in velocidad:
    cant_datos_totales_v+=1
# hallar los promedios y lo guarda en una lista
for i in range(0,cant_datos_totales_v):
    # Cuando entra al condicional, es poruqe varia el mes
    
    if n_año_v==dates_v[i].year:
        
            #aqui se evalua para el 1er mes 
        if n_mes_v==dates_v[i].month:
            cant_datos_por_mes_v += 1
            suma_datos_por_mes_v+= velocidad[i]
            
            #max y min
            if (velocidad[i] > max_mensual_velocidad):
                max_mensual_velocidad = velocidad[i]
            if (velocidad[i] < min_mensual_velocidad and velocidad[i] != 0):
                min_mensual_velocidad = velocidad[i]
            if (velocidad[i] > max_anual_velocidad):
                max_anual_velocidad = velocidad[i]
            if (velocidad[i] < min_anual_velocidad and velocidad[i] != 0):
                min_anual_velocidad = velocidad[i]
            
            
            # servira para INCAS
            # if n_dia_t==dates_t[i].day: # n_dia_t = 13
            #     cant_datos_en_dia_t += 1
            #     suma_datos_por_dia_t+=temperatura[i] # 220
            #     # cuando cambia del dia, entra al valor de else
            # else:
            #     promedio_t=suma_datos_por_dia_t/cant_datos_en_dia_t
            #     promedio_por_dia_temperatura.append(promedio_t)
            #     suma_datos_por_dia_t= temperatura[i] # 20
            #     cant_datos_en_dia_t = 1
            #     n_dia_t = dates_t[i].day
        else:
            diferencia = dates_v[i].month - n_mes_v
            if diferencia > 1:
                for e in range(1,diferencia):
                    promedio_por_mes_velocidad.append(0)
          
            promedio_v = suma_datos_por_mes_v/cant_datos_por_mes_v
            promedio_por_mes_velocidad.append(promedio_v)
            maximos_mensuales_velocidad.append(max_mensual_velocidad)
            max_mensual_velocidad = 0
            minimos_mensuales_velocidad.append(min_mensual_velocidad)
            min_mensual_velocidad = 100000
            sumatoria_anual_de_datos_velocidad+=promedio_v
            cantidad_datos_promedio_anual+=1
            suma_datos_por_mes_v=velocidad[i]
            cant_datos_por_mes_v=1
            n_mes_v=dates_v[i].month
            momento_de_borrar = True
    else:
        promedio_v = suma_datos_por_mes_v/cant_datos_por_mes_v
        promedio_por_mes_velocidad.append(promedio_v)
        maximos_anuales_velocidad.append(max_anual_velocidad)
        max_anual_velocidad=0
        minimos_anuales_velocidad.append(min_anual_velocidad)
        min_anual_velocidad=100000
        cont_meses_actuales = len(promedio_por_mes_velocidad)%12
        diferencia2 = 12 - cont_meses_actuales
        if diferencia2 < 5:
            for e in range(0,diferencia2):
                promedio_por_mes_velocidad.append(0)
        promedio_anual_v=sumatoria_anual_de_datos_velocidad/cantidad_datos_promedio_anual
        promedio_anual_datos_oficial_velocidad.append(promedio_anual_v)
        suma_datos_por_mes_v=velocidad[i]
        cant_datos_por_mes_v=1
        n_año_v=dates_v[i].year
        n_mes_v=dates_v[i].month
        contador_v+= 1
        
        ma=0
        me=1000
        for i in range(0,cant_datos_totales_v):
            if dates_v[i].year==n_año_v:
                
                sumatoria_anual_de_datos_velocidad+=velocidad[i]
                
                if ma<velocidad[i]:
                      ma=velocidad[i]
                     
                if me>velocidad[i]:
                    me=velocidad[i]
                
        datos_mayores_anuales_v.append(ma)
        datos_menores_anuales_v.append(me)
        

promedio_v = suma_datos_por_mes_v/cant_datos_por_mes_v
promedio_por_mes_velocidad.append(promedio_v)
promedio_anual_v=sumatoria_anual_de_datos_velocidad/cantidad_datos_promedio_anual
promedio_anual_datos_oficial_velocidad.append(promedio_anual_v)
maximos_mensuales_velocidad.append(max_mensual_velocidad)
minimos_mensuales_velocidad.append(min_mensual_velocidad)
maximos_anuales_velocidad.append(max_anual_velocidad)
minimos_anuales_velocidad.append(min_anual_velocidad)

# Hay datos vacios por lo que añado ceros al arreglos

#print(diccionario)
#print(len(promedio_por_mes_temperatura))

#print(promedio_por_año_termperatura)

for i in range(0,4):
    promedio_por_mes_velocidad.append(0)
    

v_2010=promedio_por_mes_velocidad[0:12]   

v_2011=promedio_por_mes_velocidad[12:24]
v_2012=promedio_por_mes_velocidad[24:36]
v_2013=promedio_por_mes_velocidad[36:48]
v_2014=promedio_por_mes_velocidad[48:60]
v_2015=promedio_por_mes_velocidad[60:72]
v_2016=promedio_por_mes_velocidad[72:84]
v_2017=promedio_por_mes_velocidad[84:96]
v_2018=promedio_por_mes_velocidad[96:108]
v_2019=promedio_por_mes_velocidad[108:120]

promedio_por_año_velocidad.append(v_2010)
promedio_por_año_velocidad.append(v_2011)
promedio_por_año_velocidad.append(v_2012)
promedio_por_año_velocidad.append(v_2013)
promedio_por_año_velocidad.append(v_2014)
promedio_por_año_velocidad.append(v_2015)
promedio_por_año_velocidad.append(v_2016)
promedio_por_año_velocidad.append(v_2017)
promedio_por_año_velocidad.append(v_2018)
promedio_por_año_velocidad.append(v_2019)


promedio_mensual_velocidad=[]
sumador_por_meses = []
sumador_v=0
contador_meses = 0

for e in range(0,12):
    for i in promedio_por_año_velocidad:
        sumador_v+= i[e]
        if i[e] != 0:
            contador_meses += 1
    promedio = sumador_v/contador_meses
    sumador_por_meses.append(sumador_v)
    
    promedio_mensual_velocidad.append(promedio)
    
    sumador_v=0
    promedio = 0
    contador_meses = 0
#print(promedio_anual_datos_oficial_temperatura)
promedio_datos_anual_t=promedio_anual_datos_oficial_temperatura

print(maximos_anuales_velocidad)
print(minimos_anuales_velocidad) 
"""
year=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]      
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(year,promedio_datos_anual_t,linewidth=5,c="green")
ax.set_title("Promedio anual de temperatura \n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Años",fontsize=15)
ax.set_ylabel("Temperatura °C",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=15)

plt.show()

t_mens=promedio_datos_mensuales_t=promedio_mensual_temperatura
meses=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(meses,t_mens,linewidth=5,c="black")
ax.set_title("Promedio estacional de temperatura \n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Meses",fontsize=15)
ax.set_ylabel("Temperatura °C",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=15)
plt.show()

promedio_datos_anual_h=promedio_anual_datos_oficial_humedad
year=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]   
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(year,promedio_datos_anual_h,linewidth=5,c="red")
ax.set_title("Promedio anual de humedad \n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Años",fontsize=20)
ax.set_ylabel("Humedad % ",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=15)
ax.axis([2010,2019,80,85])
plt.show()

promedio_datos_mensuales_h=promedio_mensual_humedad
meses=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
fig,ax=plt.subplots()
plt.style.use("seaborn")
ax.plot(meses,promedio_datos_mensuales_h,linewidth=5,c="green")
ax.set_title("Promedio estacional  de humedad\n E.'Campo de Marte'",fontsize=20)
ax.set_xlabel("Meses",fontsize=15)
ax.set_ylabel("Humedad %",fontsize=20)
ax.tick_params(axis="both",which="major",labelsize=15)
plt.show()


print()
"""























    
    