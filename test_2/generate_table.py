import pandas as pd
import sqlite3

def table():
    archivo_excel = pd.ExcelFile('test_1/data/WEB01012023.xlsx')
    hoja = 'LDM'

    df = archivo_excel.parse(hoja, header=None)

    filas_a_eliminar = []
    for index, row in df.iterrows():
        if "DEMANDA MEDIA" in row.values:
            filas_a_eliminar.append(index)
            filas_a_eliminar.append(index + 1)

    df = df.drop(filas_a_eliminar)

    df.columns = df.iloc[3]
    df = df[3:]
    df_jen_c = df[df['Nemo'] == 'JEN-C']
    print(df_jen_c)
