"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep= ";")
   
    columns = ["sexo", "tipo_de_emprendimiento", "idea_negocio","barrio","línea_credito"]
    for col in columns:
        df[col]=df[col].str.lower()
        df[col] = df[col].apply(lambda x: str(x).replace("-"," ").replace("_"," "))
    

    date = df['fecha_de_beneficio'].str.split("/")
    d = []
    m = []
    y = []
    for date_1 in date:
        d.append(date_1[0])
        m.append(date_1[1])
        y.append(date_1[2])

    d_1 = []
    y_1 = []
    for date in range(len(d)):
        if int(d[date]) > 31:
            d_1.append(y[date])
            y_1.append(d[date])
        else:
            d_1.append(d[date])
            y_1.append(y[date])
        

    date_2 = []
    for day, month, year in zip(d_1, m, y_1):
        date_2.append(f"{day}/{month}/{year}")

    date_df = pd.DataFrame(date_2)

    df['fecha_de_beneficio'] = date_df
   

    df["monto_del_credito"] = df["monto_del_credito"].apply(lambda x: str(x).strip("$").strip().replace(".00","").replace(",",""))
    df['barrio'] = df['barrio'].str.replace("no. ", "no.", regex=False)   
    df['barrio'] = df['barrio'].str.replace('bel¿n', 'belen', regex=False)
    df['barrio'] = df['barrio'].str.replace('boyac¿', 'boyaca', regex=False)
    df['barrio'] = df['barrio'].str.replace('andaluc¿a', 'andalucia', regex=False)
    df['barrio'] = df['barrio'].str.replace('antonio_nari¿o', 'antonio_narino', regex=False)
    df['barrio'] = df['barrio'].str.replace('barrio_caycedo', 'barrio_caicedo', regex=False)
    df['barrio'] = df['barrio'].str.replace('antonio_nariño', 'antonio_narino', regex=False)
    df['barrio'] = df['barrio'].str.replace('campo_vald¿s_no.1', 'campo_valdes_no.1', regex=False)
    df['barrio'] = df['barrio'].str.replace('veinte_de_julio', '20_de_julio', regex=False)

   
    df.drop_duplicates(inplace = True)
    
    return df


