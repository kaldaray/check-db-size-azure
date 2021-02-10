import pyodbc
from config import DbConnect

def connect_to_db():
    # Объявляем подключение к БД
    with pyodbc.connect('DRIVER='+DbConnect.driver+';SERVER='+DbConnect.server+';PORT=1433;DATABASE='+DbConnect.database+';UID='+DbConnect.username+';PWD='+ DbConnect.password) as conn:
        print("Подключен к БД")
        with conn.cursor() as cursor:
            cursor.execute("select sum(reserved_page_count) * 8.0 * 1024 from sys.dm_db_partition_stats")
            row = cursor.fetchone()
            while row:
                print (str(row[0]) + " " + str(row[1]))
                row = cursor.fetchone()


# Запуск скрипта
if __name__ == '__main__':
    DbConnect = DbConnect()
    print("Поделючение к БД ===>\n")
    connect_to_db()

