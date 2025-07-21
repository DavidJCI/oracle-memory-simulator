import cx_Oracle
import random
import time


def create_connection():
    try:
        connection = cx_Oracle.connect(
            user='c##bot_insert_11',
            password='contra123',
            dsn='localhost/xe'
        )
        print("Conexión exitosa a la base de datos.")
        return connection
    except cx_Oracle.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None


def insert_data(connection, num_inserts):
    try:
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO SYSTEM.data_valores (
            id_data_valores,
            num1,
            num2,
            hora
        ) VALUES (
            :id_data_valores,
            :num1,
            :num2,
            SYSTIMESTAMP
        )
        """

        # Generar datos solo para id_data_valores entre 1 y 50
        data = []
        for i in range(1, 50):  # Esto genera ids desde 1 hasta 50
            data.append((
                i,  # id_data_valores
                random.randint(1, 100),  # num1 (número aleatorio entre 1 y 100)
                random.randint(1, 100)  # num2 (número aleatorio entre 1 y 100)
            ))

        # Seleccionar un número aleatorio de registros a insertar
        for _ in range(num_inserts):
            record = random.choice(data)  # Elegir un registro aleatorio
            cursor.execute(insert_query, {
                'id_data_valores': record[0],
                'num1': record[1],
                'num2': record[2]
            })

        connection.commit()
        print(f"{num_inserts} datos insertados correctamente.")
    except cx_Oracle.Error as error:
        print("Error al insertar datos:", error)


def main():
    connection = create_connection()
    if connection:
        start_time = time.time()  # Tiempo de inicio
        duration = 300  # Duración en segundos (5 minutos)

        while time.time() - start_time < duration:
            num_inserts = random.randint(1, 5)  # Número aleatorio de inserciones entre 1 y 5
            insert_data(connection, num_inserts)
            print(f"Inserciones realizadas. Esperando 30 segundos...")
            time.sleep(30)  # Esperar 30 segundos antes de la siguiente inserción

        connection.close()
        print("Tiempo de ejecución completado (5 minutos).")


if __name__ == "__main__":
    main()
