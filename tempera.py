import statistics
import csv 
import matplotlib.pyplot as plt
from datetime import datetime
#se extrae la informacion del archivo csv
work="real.csv"
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
###evaluamos anualmente
cant_t=0
for i in dates_t:
    cant_t+=1
    
arreglo_cant_datos_anual_t=[]
promedio_datos_anual_t=[]
datos_menores_anuales_t=[]
datos_mayores_anuales_t=[]

for a in range(2010,2020):
    #bucle para añadir informacion al  arreglo: 
    cant_datos_t=0
    ma=0
    me=1000
    cant_datos_t=0
    suma_datos_t=0
   
    for i in range(0,cant_t):
        if dates_t[i].year==a:
            cant_datos_t+=1
            suma_datos_t+=temperatura[i]
            if ma<temperatura[i]:
                ma=temperatura[i]
                
            if me>temperatura[i]:
                me=temperatura[i]
            
            
            
    prom_datos_anual_t=suma_datos_t/cant_datos_t
    
    promedio_datos_anual_t.append(prom_datos_anual_t)
    datos_mayores_anuales_t.append(ma)
    datos_menores_anuales_t.append(me)
print(promedio_datos_anual_t)
# print(datos_mayores_anuales_t)
# print(datos_menores_anuales_t)

# year=[]
# for a in range(2009,2019):
#     a=a+1
#     year.append(a)

# plt.style.use('seaborn')
# fig,ax=plt.subplots()
# ax.plot(year,datos_mayores_anuales_t,c="blue",linewidth=5)
# ax.plot(year,promedio_datos_anual_t,c="red",linewidth=5)
# ax.plot(year,datos_menores_anuales_t,c="green",linewidth=5)
# ax.set_title("Promedio anual de temperatura \n E.'Campo de Marte'",fontsize=20)
# ax.set_xlabel("Años",fontsize=15)
# ax.set_ylabel("Temperatura °C",fontsize=20)
# ax.tick_params(axis="both",which="major",labelsize=15)
# ax.axis([2010,2019,10,35])
# plt.plot(datos_mayores_anuales_t, label = "Tmax")
# plt.plot(datos_menores_anuales_t,label="Tmin")
# plt.plot(datos_mayores_anuales_t, label = "Tprom")
# plt.legend()
# plt.show()
# ###evaluamos mensualmente
# arreglo_cant_datos_mensuales_t=[]
# promedio_datos_mensuales_t=[]
# maximo_datos_mensuales_t=[]
# minimo_datos_mensuales_t=[]
# for i in range(1,13):
#     cant_datos_mensual_t=0
#     ma=0
#     me=1000        
#     suma_datos_mensual_t=0     
#     for a in range(0,cant_t):
#         if dates_t[a].month==i:
#             cant_datos_mensual_t+=1
#             suma_datos_mensual_t+=temperatura[a]
            
#             if ma<temperatura[a]:
#                 ma=temperatura[a]
                
#             if me>temperatura[a]:
#                 me=temperatura[a]
#     promedio_datos_t=suma_datos_mensual_t/cant_datos_mensual_t
#     promedio_datos_mensuales_t.append(promedio_datos_t)
#     maximo_datos_mensuales_t.append(ma)
#     minimo_datos_mensuales_t.append(me)

# t_mens=promedio_datos_mensuales_t
# meses=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
# fig,ax=plt.subplots()
# plt.style.use("seaborn")
# ax.plot(meses,promedio_datos_mensuales_t,linewidth=5,c="red")
# ax.plot(meses, maximo_datos_mensuales_t,linewidth=5,c="blue")
# ax.plot(meses,minimo_datos_mensuales_t,linewidth=5,c="green")
# ax.set_title("Promedio estacional de temperatura \n E.'Campo de Marte'",fontsize=20)
# ax.set_xlabel("Meses",fontsize=15)
# ax.set_ylabel("Temperatura °C",fontsize=20)
# ax.tick_params(axis="both",which="major",labelsize=15)
# plt.plot(maximo_datos_mensuales_t, label = "T_mens_max")
# plt.plot(minimo_datos_mensuales_t,label="T_mens_min")
# plt.plot(promedio_datos_mensuales_t, label = "T_mens_prom")
# plt.legend()
# plt.show()
# # =============================================================================
# # 
# # # para humeadad
# # =============================================================================
# with open(work) as f: 
#     dates_h=[]
#     humedad=[]
       
#     read=csv.reader(f)
#     cabezera=next(read)
#     for row in read:
#         current_date_h=datetime.strptime(row[0],'%d/%m/%Y')                      
#         try:
           
#             h=float(row[3])
          
# #codigo para eliminar datos vacios            
#         except ValueError:
#             print(f"Missing data for {current_date}")
# #esos valores se añaden a las listas desde la linea 13 hasta la 19            
#         else:
#             dates_h.append(current_date_h)
#             humedad.append(h)
# cant_h=0
# for i in dates_h:
#     cant_h+=1            
# arreglo_cant_datos_anual_h=[]
# promedio_datos_anual_h=[]
# datos_menores_anuales_h=[]
# datos_mayores_anuales_h=[]
# for a in range(2010,2020):
#     cant_datos_h=0
#     suma_datos_h=0
#     ma=0
#     me=1000
          
#     for i in range(0,cant_h):
#         if dates_h[i].year==a:
#             cant_datos_h+=1
#             suma_datos_h+=humedad[i]
            
#             if ma<humedad[i]:
#                  ma=humedad[i]
                 
#             if me>humedad[i]:
#                 me=humedad[i]
                
#     prom_datos_anual_h=suma_datos_h/cant_datos_h
    
#     promedio_datos_anual_h.append(prom_datos_anual_h)
#     datos_mayores_anuales_h.append(ma)
#     datos_menores_anuales_h.append(me)
    
    
# plt.style.use('seaborn')
# fig,ax=plt.subplots()
# ax.plot(year,datos_mayores_anuales_h,c="blue",linewidth=5)
# ax.plot(year,promedio_datos_anual_h,c="red",linewidth=5)
# ax.plot(year,datos_menores_anuales_h,c="green",linewidth=5)
# ax.set_title("Promedio anual de humedad \n E.'Campo de Marte'",fontsize=20)
# ax.set_xlabel("Años",fontsize=15)
# ax.set_ylabel("Humedad %",fontsize=20)
# ax.tick_params(axis="both",which="major",labelsize=15)
# plt.plot(datos_mayores_anuales_h, label = "Hmax")
# plt.plot(datos_menores_anuales_h,label="Hmin")
# plt.plot(datos_mayores_anuales_h, label = "Hprom")
# ax.axis([2010,2019,30,100])
# plt.legend()
# plt.show()    



# # ###evaluamos mensualmente
# # arreglo_cant_datos_mensuales_h=[]
# # promedio_datos_mensuales_h=[]
# # maximo_datos_mensuales_h=[]
# # minimo_datos_mensuales_h=[]
# # for i in range(1,13):
# #     cant_datos_mensual_h=0
# #     ma=0
# #     me=1000        
# #     suma_datos_mensual_h=0     
# #     for a in range(0,cant_h):
# #         if dates_t[a].month==i:
# #             cant_datos_mensual_h+=1
# #             suma_datos_mensual_h+=humedad[a]
            
# #             if ma<humedad[a]:
# #                 ma=humedad[a]
                
# #             if me>humedad[a]:
# #                 me=humedad[a]
# #     promedio_datos_h=suma_datos_mensual_t/cant_datos_mensual_h
# #     promedio_datos_mensuales_h.append(promedio_datos_h)
# #     maximo_datos_mensuales_h.append(ma)
# #     minimo_datos_mensuales_h.append(me)
# # fig,ax=plt.subplots()
# # plt.style.use("seaborn")
# # ax.plot(meses,promedio_datos_mensuales_h,linewidth=5,c="red")
# # ax.plot(meses, maximo_datos_mensuales_h,linewidth=5,c="blue")
# # ax.plot(meses,minimo_datos_mensuales_h,linewidth=5,c="green")
# # ax.set_title("Promedio estacional  de humedad\n E.'Campo de Marte'",fontsize=20)
# # ax.set_xlabel("Meses",fontsize=15)
# # ax.set_ylabel("Humedad %",fontsize=20)
# # ax.tick_params(axis="both",which="major",labelsize=15)
# # plt.plot(maximo_datos_mensuales_h, label = "H_mens_max")

# # plt.plot(promedio_datos_mensuales_h, label = "H_mens_prom")
# # plt.plot(minimo_datos_mensuales_h,label="H_mens_min")
# # plt.legend()
# # plt.show()

# # # para viento(dir y veloc)

# with open(work) as f:
#     direccion_viento=[]
#     dates_dv=[]
    
    
#     read=csv.reader(f)
#     cabezera=next(read)
#     for row in read:
#         current_date_dv=datetime.strptime(row[0],'%d/%m/%Y') 
#         try:
            
          
#             d_v=float(row[5])
           
# #codigo para eliminar datos vacios            
#         except ValueError:
#             print(f"Missing data for {current_date}")        
#         else:
#             dates_dv.append(current_date_dv)
#             direccion_viento.append(d_v)


# # datos dv
# promedio_datos_anual_dv=[]
# datos_menores_anuales_dv=[]
# datos_mayores_anuales_dv=[]
# cant_dv=0
# for i in dates_dv:
#     cant_dv+=1
    
# for a in range(2010,2020):
#     #bucle para añadir informacion al  arreglo: 

#     cant_datos_dv=0
#     suma_datos_dv=0  
#     ma=0
#     me=1000  
#     for i in range(0,cant_dv):
#         if dates_dv[i].year==a:           
#             cant_datos_dv+=1
#             suma_datos_dv+=direccion_viento[i]
#             if ma<direccion_viento[i]:
                        
#                 ma=direccion_viento[i]
                
                                                  
                                    
#             if me>direccion_viento[i] :
            
#                 me=direccion_viento[i]
              
             
#     prom_datos=suma_datos_dv/cant_datos_dv
#     promedio_datos_anual_dv.append(prom_datos)
#     datos_menores_anuales_dv.append(me)
#     datos_mayores_anuales_dv.append(ma)
           
            
     
        
            
    
           
            
        
            
            
    
   

    
   

            
# #           #velocidad del viento
# # with open(work) as f:
# #     velocidad_viento=[]
# #     dates_vv=[]
# #     read=csv.reader(f)
# #     cabezera=next(read)
# #     for row in read:
# #         current_date_vv=datetime.strptime(row[0],'%d/%m/%Y') 
            
# #         try:
# #             v_v=float(row[6])

# # #codigo para eliminar datos vacios            
# #         except ValueError:
# #             print(f"Missing data for {current_date}")
# # #esos valores se añaden a las listas desde la linea 13 hasta la 19            
# #         else:
# #             dates_vv.append(current_date_vv)  
# #             velocidad_viento.append(v_v)
# # cant_dv=0
# # for i in dates_dv:
# #     cant_dv+=1
    
# # cant_vv=0
# # for i in dates_vv:
# #     cant_vv+=1

# # arreglo_cant_datos_anual_dv=[]
# # arreglo_cant_datos_anual_vv=[]
# # # datos dv
# # promedio_datos_anual_dv=[]
# # datos_menores_anuales_dv=[]
# # datos_mayores_anuales_dv=[]
# # for a in range(2010,2020):
# #     #bucle para añadir informacion al  arreglo: 

# #     cant_datos_dv=0
# #     suma_datos_dv=0
    
    
# #     ma=0
# #     me=1000  
# #     for i in range(0,cant_dv):
# #         if dates_dv[i].year==a:
            
# #             cant_datos_dv+=1
# #             suma_datos_dv+=direccion_viento[i]
            
# #             if ma<direccion_viento[i]:
# #                 ma=direccion_viento[i]
                
# #             if me>direccion_viento[i]:
# #                 me=direccion_viento[i]
    
# #     prom_datos_anual_dv=suma_datos_dv/cant_datos_dv                   
# #     promedio_datos_anual_dv.append(prom_datos_anual_dv)
# #     datos_menores_anuales_dv.append(me)
# #     datos_mayores_anuales_dv.append(ma)


# # print(datos_menores_anuales_dv)        
# # for a in range(2010,2020):
# #     #bucle para añadir informacion al  arreglo: 
# #     cant_datos_t=0
# #     ma=0
# #     me=100000
# #     cant_datos_t=0
# #     suma_datos_t=0
   
# #     for i in range(0,cant_t):
# #         if dates_t[i].year==a:
# #             cant_datos_t+=1
# #             suma_datos_t+=temperatura[i]
# #             if ma<temperatura[i]:
# #                 ma=temperatura[i]
                
# #             if me>temperatura[i]:
# #                 me=temperatura[i]
            
            
# #     prom_datos_anual_t=suma_datos_t/cant_datos_t
    
# #     promedio_datos_anual_t.append(prom_datos_anual_t)    
# #     datos_menores_anuales_t.append(me)
# #     datos_mayores_anuales_t.append(ma)




# # # datos vv
# # promedio_datos_anual_vv=[]
# # datos_menores_anuales_vv=[]
# # datos_mayores_anuales_vv=[]

# # for a in range(2010,2020):
# #     #bucle para añadir informacion al  arreglo: 
# #     cant_datos_vv=0
# #     cant_datos_dv=0
# #     suma_datos_dv=0
# #     suma_datos_vv=0
    
# #     ma=0
# #     me=1000  
# #     for i in range(0,cant_dv):
# #         if dates_dv[i].year==a:
            
# #             cant_datos_dv+=1
# #             suma_datos_dv+=direccion_viento[i]
            
# #             if ma<direccion_viento[i]:
# #                 ma=direccion_viento[i]
                
#             if me>direccion_viento[i]:
#                 me=direccion_viento[i]
    
#     prom_datos_anual_dv=suma_datos_dv/cant_datos_dv                   
#     arreglo_cant_datos_anual_dv.append(cant_datos_dv)
#     promedio_datos_anual_dv.append(prom_datos_anual_dv)
#     datos_menores_anuales_dv.append(me)
#     datos_mayores_anuales_dv.append(ma)
            
            
            
#     for i in range(0,cant_vv):
#         if dates_vv[i].year==a:
            
#             cant_datos_vv+=1
#             suma_datos_vv+=velocidad_viento[i]
            
#             if ma<velocidad_viento[i]:
#                 ma=velocidad_viento[i]
                
#             if me>velocidad_viento[i]:
#                 me=velocidad_viento[i]
                
    
    
#     prom_datos_anual_vv=suma_datos_vv/cant_datos_vv 
#     #agregamos los valores a las listas de las variables halladas
#     #Datos para vel. 
#     promedio_datos_anual_vv.append(prom_datos_anual_vv)
#     arreglo_cant_datos_anual_vv.append(cant_datos_vv)
#     datos_menores_anuales_vv.append(me)
#     datos_mayores_anuales_vv.append(ma)
    
    
#     for i in range(0,cant_t):
#         if dates_t[i].year==a:
#             cant_datos_t+=1
#             suma_datos_t+=temperatura[i]
#             if ma<temperatura[i]:
#                 ma=temperatura[i]
                
#             if me>temperatura[i]:
#                 me=temperatura[i]
            
#     prom_datos_anual_t=suma_datos_t/cant_datos_t
    
#     promedio_datos_anual_t.append(prom_datos_anual_t)
#     datos_menores_anuales_t.append(me)
#     datos_mayores_anuales_t.append(ma)
    
    
# # print(datos_menores_anuales_dv)
# # print(datos_mayores_anuales_dv)
# # print(promedio_datos_anual_dv)
    
            

