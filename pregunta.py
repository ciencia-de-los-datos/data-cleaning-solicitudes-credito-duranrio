"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col=0)

    df.dropna(inplace=True)
    
    columns = ["sexo", "tipo_de_emprendimiento", "idea_negocio","barrio","línea_credito"]
    for col in columns:
        df[col]=df[col].str.lower()
        df[col] = df[col].apply(lambda x: str(x).replace("-"," ").replace("_"," "))
    
    df["monto_del_credito"] = df["monto_del_credito"].apply(lambda x: str(x).strip("$").strip().replace(".00","").replace(",",""))

    
    df.fecha_de_beneficio = pd.to_datetime(df["fecha_de_beneficio"], dayfirst = True)
    df.monto_del_credito = df.monto_del_credito.astype(float)
    
    df.drop_duplicates(inplace=True)

    return df



