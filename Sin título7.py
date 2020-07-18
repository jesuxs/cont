carro_1={"color":"green","llantas":"4"}
print(carro_1["color"])
print(carro_1["llantas"])

n_llantas=carro_1["llantas"]
print(f"Ud. obtuvo {n_llantas} pts")

carro_1["ventanas"]=2
carro_1["timon"]=1
print(carro_1)


carro_2={}
carro_2["color"]="rojo"
carro_2["llantas"]=2
carro_2["ventana"]=1
carro_2["timon"]=1
print(carro_2)

carro_1["color"]="celeste"
carro_2["color"]="azul"

print(carro_1)
print(carro_2)

car={"x":0,"y":0,"speed":"media"}
if car["speed"]== "lenta":
    ace_x=1
elif car["speed"]=="media":
    ace_x=2
else:
    ace_x=3
    
car["x"]= car["x"]+ace_x
print(f' la nueva posicion es: {car["x"]}')

del car['y']
print(car)


gustos={
        "marco":"cebiche",
        "apes":"papa frita",
        "flora":"chancho",
        "adrian":"cheva"
        }
print(gustos)

platos=gustos["apes"].title()
print(f'a la "apes" le gusta la {platos}')

gustos["apes"]




      
      


    
    


