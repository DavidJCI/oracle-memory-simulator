import cx_Oracle
import random
import time


def create_connection():
    try:
        connection = cx_Oracle.connect(
            user='c##bot_select_3',
            password='contra123',
            dsn='localhost/xe'
        )
        print("Conexión exitosa a la base de datos.")
        return connection
    except cx_Oracle.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None


def select_data_from_table(connection, table_name):
    try:
        cursor = connection.cursor()
        select_query = f"SELECT * FROM {table_name} WHERE ROWNUM <= 10"  # Selecciona hasta 10 registros
        cursor.execute(select_query)
        rows = cursor.fetchall()
        print(f"Datos seleccionados de {table_name}:")
        for row in rows:
            print(row)
    except cx_Oracle.Error as error:
        print(f"Error al seleccionar datos de {table_name}:", error)


def main():
    connection = create_connection()
    if connection:
        start_time = time.time()  # Tiempo de inicio
        duration = 300  # Duración en segundos (5 minutos)

        while time.time() - start_time < duration:
            table_to_query = random.choice(
                ["SYSTEM.data_valores", "SYSTEM.data_personas"])  # Elegir aleatoriamente entre las dos tablas
            select_data_from_table(connection, table_to_query)
            print(f"Consulta realizada en {table_to_query}. Esperando 60 segundos...")
            time.sleep(60)  # Esperar 60 segundos antes de la siguiente consulta

        connection.close()
        print("Tiempo de ejecución completado (5 minutos).")


if __name__ == "__main__":
    main()
