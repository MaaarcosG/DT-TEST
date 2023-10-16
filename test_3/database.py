import pandas as pd 
def data():
    df_generacion = pd.read_csv('test_3/data/Generacion.csv')
    df_poe = pd.read_csv('test_3/data/POE.csv')
    # merge de los dos dataframes
    # falta los datos del ejercicio anterior ya que no me sale jajajaja :c
    df_finish = df_generacion.merge(df_poe, left_on='fecha_hora', right_on='fecha_hora')
    print(df_finish)