import pypsa
import matplotlib.pyplot as plt
import pandas as pd


fn = 'C:/Users/josut/OneDrive/Escritorio/Python_TFM/pypsa_proc/networks/base_s_20_elec_.nc'
n = pypsa.Network(fn)

# Exportar varias tablas a un archivo Excel
with pd.ExcelWriter("results/red_pypsa_datos.xlsx", engine="openpyxl") as writer:
    n.buses.to_excel(writer, sheet_name="Buses")
    n.lines.to_excel(writer, sheet_name="Lines")
    n.generators.to_excel(writer, sheet_name="Generators")
    n.loads_t.p.to_excel(writer, sheet_name="Loads_t")


#print(n.buses)
#print(n.lines)
#print(n.generators)
#print(n.loads)

"""
n.plot(
    bus_sizes=0.01,             # escala de tamaño de los buses
    line_widths=1.0,           # grosor de líneas
    color_geomap=True,         # fondo con mapa geográfico
    title="Red eléctrica Simplificada con PyPSA-Eur de 20 nudos"
)
"""

# Mostrar el gráfico
#plt.show()