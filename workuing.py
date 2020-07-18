import statistics
import csv 
import matplotlib.pyplot as plt
from datetime import datetime
#se extrae la informacion del archivo csv
work="PMT.csv"
with open(work) as f:
    read=csv.reader(f)
    cabezera=next(read)
#se extrae todos los datos del archivo csv

    dates=[]
    pm_ten=[]
    for row in read:
        current_date=datetime.strptime(row[0],'%d/%m/%Y')
        try:
            mp_ten=float(row[1])
                    
        except ValueError:
            print(f"Missing data for {current_date}")
          
        else:
            dates.append(current_date)
            pm_ten.append

# =============================================================================
# cant=0
# for i in dates:
#     cant +=1
# 
# arreglo_cant_datos_anual=[]
# promedio_datos_anual_pp=[]
# for a in range(2010,2020): 
#     cant_datos=0
#     suma_datos_pp=0
#     for i in range(0,cant):
#         if dates[i].year==a:        
#             cant_datos+=1
#     if cant_datos != 0:
#         suma_datos_pp+=precipitacion[i]
#         prom_datos_anual_pp=suma_datos_pp/cant_datos
#         promedio_datos_anual_pp.append(prom_datos_anual_pp)
# =============================================================================
