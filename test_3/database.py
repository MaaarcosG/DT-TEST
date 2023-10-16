import pandas as pd 
def data():
    df_generacion = pd.read_csv('test_3/data/Generacion.csv')
    df_poe = pd.read_csv('test_3/data/POE.csv')
    # merge de los dos dataframes
    df_finish = df_generacion.merge(df_poe, left_on='fecha_hora', right_on='fecha_hora')
    print(df_finish)