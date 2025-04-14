import pandas as pd
import re

def renewable_conv(path, bus_map, dir_name):
    df = pd.read_excel(f'{path}', sheet_name='gen_t')  # puedes usar el nombre o el índice de la hoja

   # Separar columnas de snapshot y tecnologías
    snapshots = df['snapshot']
    df = df.drop(columns=['snapshot'])

    # Inicializar diccionarios por tecnología
    tech_dfs = {'solar': {}, 'onwind': {}}

    # Procesar columnas del dataframe
    for col in df.columns:
        match = re.match(r"(ES\d+ \d+) 0 (solar|onwind)", col)
        if match:
            node, tech = match.groups()
            if tech in tech_dfs and node in bus_map:
                bus_number = bus_map[node]
                if bus_number not in tech_dfs[tech]:
                    tech_dfs[tech][bus_number] = []
                # Convertimos los valores a float y coma por punto decimal
                tech_dfs[tech][bus_number] = df[col].astype(str).str.replace(',', '.').astype(float).values

    # Escribir los archivos por tecnología
    for tech, data in tech_dfs.items():
        # Crear DataFrame con filas = buses y columnas = horas
        gen_df = pd.DataFrame.from_dict(data, orient='index')
        gen_df.index.name = 'bus'
        gen_df.columns = [f"h{i+1}" for i in range(gen_df.shape[1])]
        gen_df.sort_index(inplace=True)
        # Guardar como CSV
        if tech == 'solar':
            gen_df.to_csv(f"{dir_name}/solarData.csv", float_format='%.6f')
        elif tech == 'onwind':
            gen_df.to_csv(f"{dir_name}/windData.csv", float_format='%.6f')

    print("Archivos de generación renovable se han generado correctamente.")