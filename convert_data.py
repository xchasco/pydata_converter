import os

from functions.demand_conv import demand_conv
from functions.generator_conv import generator_conv
from functions.renewable_conv import renewable_conv


#path = './results/red_pypsa_datos_20nudos_v1.xlsx'
path = './results/red_pypsa_datos.xlsx'
dir_name = input('Introduce the name of the case: ')

# Crear la carpeta si no existe
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
    print(f"Carpeta '{dir_name}' creada con éxito.")
else:
    print(f"La carpeta '{dir_name}' ya existe.")

#####ADAPTAR DATOS DE DEMANDA#####
bus_map = demand_conv(dir_name=dir_name, path=path)

#####ADAPTAR DATOR DE GENERACIÓN CONVENCIONAL#####
generator_conv(path=path, dir_name=dir_name, bus_map=bus_map)

#####ADAPTA DATOS DE GENERACIÓN RENOVABLE#####
renewable_conv(path=path, dir_name=dir_name, bus_map=bus_map)

print(bus_map)