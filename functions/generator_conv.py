import pandas as pd

def generator_conv(path, bus_map, dir_name):
    df = pd.read_excel(f'{path}', sheet_name='Generators')

    # Filtrar por tipo de tecnología
    filtered = df[df['carrier'].isin(['CCGT', 'nuclear'])].copy()

    gen_table = pd.DataFrame(columns=[
    'bus', 'Pg', 'Qg', 'Qmax', 'Qmin', 'Vg', 'mBase', 'status',
    'Pmax', 'Pmin', 'c2', 'c1', 'c0'
    ])

    for _, row in filtered.iterrows():
        bus_name = row['bus']
        if bus_name in bus_map:
            gen_table = pd.concat([gen_table, pd.DataFrame([{
                'bus': bus_map[bus_name],
                'Pg': 0,
                'Qg': 0,
                'Qmax': 100,
                'Qmin': -100,
                'Vg': 1,
                'mBase': 1,
                'status': 1,
                'Pmax': row['p_nom'],
                'Pmin': 0,
                'c2': 0,
                'c1': row['marginal_cost'],
                'c0': row['capital_cost']
            }])], ignore_index=True)

    # Guardar como CSV
    gen_table.to_csv(f'./{dir_name}/generatorData.csv', sep=";",index=False)