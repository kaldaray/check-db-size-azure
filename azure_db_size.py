import pyodbc
import sys


# Server and driver to connect db
class DbConnect:
    server = 'tzzrt0aqpb.database.secure.windows.net'
    driver = '{ODBC Driver 13 for SQL Server}'


def connect_to_db(database, username, password):
    # Init connect DB
    with pyodbc.connect(
            'DRIVER=' + DbConnect.driver + ';'
            'SERVER=' + DbConnect.server + ';'
            'PORT=1433;DATABASE=' + database + ';'
            'UID=' + username + ';'
            'PWD=' + password) as conn:
        # Create cursor for make query
        with conn.cursor() as cursor:
            # select database query
            cursor.execute("select sum(reserved_page_count) * 8.0 * 1024 from sys.dm_db_partition_stats")
            row = cursor.fetchone()
            while row:
                # Print results
                print(str(row[0]))
                row = cursor.fetchone()


# Start script
if __name__ == '__main__':
    print("=== Connect to DB ===")
    connect_to_db(sys.argv[1], sys.argv[2], sys.argv[3])