import os
import pandas as pd

#####ADAPTAR DATOS DE DEMANDA#####
def demand_conv(dir_name, path):
    os.makedirs(f'./{dir_name}/demandData')
    df = pd.read_excel(f'{path}', sheet_name='Loads_t')  # puedes usar el nombre o el índice de la hoja

    # Detectar columnas que corresponden a nudos (empiezan por "ES")
    nodo_cols = [col for col in df.columns if str(col).startswith('ES')]

    # Crear diccionario de mapeo: columna -> número de bus como información interna para el programa
    col_to_bus = {col: i + 1 for i, col in enumerate(nodo_cols)}

    num_buses = len(nodo_cols)
    base_bus = pd.DataFrame({
        'bus_i': range(1, num_buses + 1),
        'type': [1]*num_buses,
        'Pd': [0]*num_buses,
        'Qd': [0]*num_buses,
        'Gs': [0]*num_buses,
        'Bs': [0]*num_buses,
        'area': [1]*num_buses,
        'Vm': [1]*num_buses,
        'Va': [0]*num_buses,
        'baseKV': [100]*num_buses,
        'zone': [1]*num_buses,
        'Vmax': [1.1]*num_buses,
        'Vmin': [0.9]*num_buses
    })

    # Recorrer cada fila (hora) y crear un CSV por cada una
    for index, row in df.iterrows():

        # Copiar plantilla base
        bus_hour = base_bus.copy()

        # Rellenar Pd con la demanda de cada nodo en esta hora
        for i, col in enumerate(nodo_cols):
            bus_hour.at[i, 'Pd'] = float(row[col])

        # Guardar archivo CSV
        nombre_archivo = f'./{dir_name}/demandData/nodeData_{index+1}.csv'
        bus_hour.to_csv(nombre_archivo, index=False)

    print("¡Archivos de demanda generados con éxito!")

    return col_to_bus