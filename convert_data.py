import os

from functions.demand_conv import demand_conv

dir_name = input('Introduce the name of the case: ')

# Crear la carpeta si no existe
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
    print(f"Carpeta '{dir_name}' creada con éxito.")
else:
    print(f"La carpeta '{dir_name}' ya existe.")

#####ADAPTAR DATOS DE DEMANDA#####
bus_info = demand_conv(dir_name=dir_name)