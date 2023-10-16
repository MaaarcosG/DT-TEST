from datetime import date, timedelta, datetime
import requests

def automation():
    # URL de la página con los enlaces a los informes diarios
    url = "https://www.amm.org.gt/pdfs2/programas_despacho/01_PROGRAMAS_DE_DESPACHO_DIARIO/2023/01_PROGRAMAS_DE_DESPACHO_DIARIO/01_ENERO/WEB02012023.xlsx"
    
    # Definir la fecha de inicio y fin
    start_date = date(2023, 1, 1)
    end_date = date(2023, 6, 30)
    
    delta = end_date - start_date   # returns timedelta

    listMonths = [
        "ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"
    ]

    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        month = listMonths[day.month - 1]
        # print('%s/%s' % (day.day, month))
        dayIterate = day.day if day.day >= 10 else f'0{day.day}'
        fileName = 'WEB%s0%s2023.xlsx' % (dayIterate, day.month)
        urlIterate = 'https://www.amm.org.gt/pdfs2/programas_despacho/01_PROGRAMAS_DE_DESPACHO_DIARIO/2023/01_PROGRAMAS_DE_DESPACHO_DIARIO/0%s_%s/%s' % (day.month, month, fileName)
        response = requests.get(urlIterate)

        open(f'test_1/data/{fileName}', "wb").write(response.content)

