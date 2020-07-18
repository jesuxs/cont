# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 00:12:31 2020

@author: JOTA
"""

# =============================================================================
# para luineas
# # =============================================================================
# # import matplotlib.pyplot as plt
# # plt.style.available
# # a=[0,1,8,27,64,81]
# # datos=[0,1,4,9,16,25]
# # plt.style.use("seaborn")
# # 
# # fig,ax=plt.subplots()
# # ax.scatter(3,4,s=100)
# # 
# # 
# # # ax.plot(datos,linewidth=4)
# # ax.set_title("Cuadrados de numeros",fontsize=15)
# # ax.set_xlabel("datos en x", fontsize=15)
# # ax.set_ylabel("datos en y",fontsize=15)
# # ax.tick_params(axis="both",labelsize=15)
# =============================================================================
# # =============================================================================
# 
# plt.show()
# 
# =============================================================================
# =============================================================================
# import matplotlib.pyplot as plt
# x_val=[1,3,5,7,9]
# y_val=[1,9,125,243,729]
# plt.style.use("seaborn")
# fig,ax=plt.subplots()
# ax.scatter(x_val,y_val,s=100)
# ax.set_title("Cuadrados de numeros",fontsize=15)
# ax.set_xlabel("datos en x", fontsize=15)
# ax.set_ylabel("datos en y",fontsize=15)
# ax.tick_params(axis="both",labelsize=15)
# plt.show()
# 
# =============================================================================

# =============================================================================
# import matplotlib.pyplot as plt
# x_val=range(1,21)
# y_val= [x**2 for x in x_val]
# plt.style.use("seaborn")
# fig,ax=plt.subplots()
# ax.scatter(x_val,y_val,c=y_val, cmap=plt.cm.Reds,s=20)
# ax.axis([0,20,0,442])
# ax.set_title("Cuadrados de numeros",fontsize=15)
# ax.set_xlabel("datos en x", fontsize=15)
# ax.set_ylabel("datos en y",fontsize=15)
# ax.tick_params(axis="both",labelsize=15)
# plt.show()
# =============================================================================

# =============================================================================
# para puntos y escaluimetrossssss
# import matplotlib.pyplot as plt
# a=range(1,5001)
# b=[x**3 for x in a]
# plt.style.use("seaborn")
# fig,ax=plt.subplots()
# ax.axis([0,5001,0,5001**3])
# ax.scatter(a,b,c=b, cmap=plt.cm.Greens,s=17)
# ax.set_title("Cuadrados de numeros",fontsize=15)
# ax.set_xlabel("datos en x", fontsize=15)
# ax.set_ylabel("datos en y",fontsize=15)
# ax.tick_params(axis="both",labelsize=15)
# plt.show()
#          
# =============================================================================
from random import choice
class randomwalk:
    def_init_(self, num_pts=5000):
        self.num_pts=num_pts
        self.x_val=[0]
        self.y_val=[0]
        

    


















