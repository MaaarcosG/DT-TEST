from test_1.download_automation import automation
from test_2.generate_table import table
from test_3.database import data
def main():
    menu = '''
        1. Tarea No. 1
        2. Tarea No. 2
        3. Tarea No. 3
        4. Tarea No. 4
        5. Salir
    '''
    flag = True
    while flag:
        print(menu)
        select = input('Elige una opcion: ')
        if (select == '1'):
            automation()
            break
        elif (select == '2'):
            table()
            break
        elif (select == '3'):
            data()
            break
        elif (select == '5'):
            print("Saliendo del programa...")
            break
        else:
            print('Opcion invalida')


if __name__ == "__main__":
    main()