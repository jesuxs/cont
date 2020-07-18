import statistics
import csv 
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import pyplot as plt
#se extrae la informacion del archivo csv
work="pp.csv"
with open(work) as f:
    read=csv.reader(f)
    cabezera=next(read)
#se extrae los datos de temperaturas y el tiempo de medicion
#se elimina los datos vacios
    humedad=[]
    dates=[]
    for row in read:
        current_date=datetime.strptime(row[0],'%d/%m/%Y')
        try:
            h=float((row[6]))
            
        except ValueError:
            print(f"Missing data for {current_date}")
            
        else:
            dates.append(current_date)
            humedad.append(h)
#bucle for para determinar la cantidad de datos "limpios"

cant=0
for i in dates:
    cant +=1
#hallando la lista de promedio anual para en los 9 años de registro
arreglo_cant_datos_anual,arreglo_suma_datos_anual=[],[]
arreglo_promedio_datos_anual=[]
for a in range(2010,2020):
    cant_datos=0
    suma_datos=0
    for i in range(0,cant):
        if dates[i].year==a:
            cant_datos+=1
            suma_datos+=humedad[i]
    prom_datos_anual=suma_datos/cant_datos
    arreglo_cant_datos_anual.append(cant_datos)
    arreglo_suma_datos_anual.append(suma_datos)
    arreglo_promedio_datos_anual.append(prom_datos_anual)
  