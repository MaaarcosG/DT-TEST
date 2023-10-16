import pandas as pd

def table():
    archivo_excel = pd.ExcelFile('test_1/data/WEB01012023.xlsx')
    page = 'LDM'
    hoja = archivo_excel.parse(page, header=None) 
    # Buscar la fila que contiene "DEMANDA MÍNIMA"
    fila_demanda_minima = hoja[hoja.apply(lambda row: 'DEMANDA MEDIA' in row.values, axis=1)]

    if not fila_demanda_minima.empty:
        # Obtener el índice de la fila "DEMANDA MÍNIMA"
        indice_fila = fila_demanda_minima.index[0]

        # Leer los datos a partir de la fila siguiente
        demanda_minima = hoja.iloc[indice_fila + 1:]

        # Reiniciar los índices
        demanda_minima.reset_index(drop=True, inplace=True)
        print(demanda_minima[demanda_minima[0] == 'JEN-C'])
        print(demanda_minima.columns)
    else:
        print("No se encontró la tabla 'DEMANDA MÍNIMA' en la hoja.")