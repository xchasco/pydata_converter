import pandas as pd

def lines_conv(path, bus_map, dir_name):
    df_original = pd.read_excel(f'{path}', sheet_name='Lines') 

    # Copiamos solo lo necesario para no tocar el original
    df = df_original[["bus0", "bus1", "x", "s_nom_max"]].copy()

    # Convertimos nombres a números usando bus_map
    df["fbus"] = df["bus0"].map(bus_map)
    df["tbus"] = df["bus1"].map(bus_map)

    # Convertimos comas por puntos y casteamos a float
    df["x"] = df["x"].astype(str).str.replace(",", ".").astype(float)
    df["s_nom_max"] = df["s_nom_max"].astype(str).str.replace(",", ".").astype(float)

    # Añadimos columnas necesarias
    df["r"] = 0
    df["b"] = 0
    df["rateA"] = df["s_nom_max"]
    df["rateB"] = df["s_nom_max"]
    df["rateC"] = df["s_nom_max"]
    df["ratio"] = 0
    df["angle"] = 0
    df["status"] = 1
    df["angmin"] = -30
    df["angmax"] = 30

    # Reordenamos las columnas en formato Matpower
    df_matpower = df[[
        "fbus", "tbus", "r", "x", "b",
        "rateA", "rateB", "rateC",
        "ratio", "angle", "status",
        "angmin", "angmax"
    ]]

    # Guardar nuevo archivo CSV
    df_matpower.to_csv(f'./{dir_name}/lineData.csv', index=False)