import cx_Oracle
import random
import time


def create_connection():
    try:
        connection = cx_Oracle.connect(
            user='c##bot_insert_4',
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
        INSERT INTO SYSTEM.data_personas (
            id_data_personas,
            nombre,
            apellido,
            celular,
            salario
        ) VALUES (
            :id_data_personas,
            :nombre,
            :apellido,
            :celular,
            :salario
        )
        """

        # Generar datos solo para id_data_personas entre 1 y 50
        data = []
        for i in range(151, 200):  # Esto genera ids desde 1 hasta 50 pa no chocar con otros ids de otros bots
            data.append((
                #nombres y datos de ejemploss pa ser analizados despues
                i,  # id_data_personas
                f'Nombre_{i}',
                f'Apellido_{i}',
                1000000000 + i,
                1500 + i * 50
            ))

        # Seleccionar un número aleatorio de registros a insertar
        for _ in range(num_inserts):
            record = random.choice(data)  # Elegir un registro aleatorio
            cursor.execute(insert_query, {
                'id_data_personas': record[0],
                'nombre': record[1],
                'apellido': record[2],
                'celular': record[3],
                'salario': record[4]
            })

        connection.commit()
        print(f"{num_inserts} datos insertados correctamente.")
    except cx_Oracle.Error as error:
        print("Error al insertar datos:", error)


def main():
    connection = create_connection()
    if connection:
        start_time = time.time()  # Tiempo de inicio
        duration = 300  # tiempo en seg (5 min)

        while time.time() - start_time < duration:
            num_inserts = random.randint(1, 5)  # Num aleatorio de inserts entre 1 y 5
            insert_data(connection, num_inserts)
            print(f"Inserciones realizadas. Esperando 30 segundos...")
            # Esperar 1 minuto antes de hacer otro insert
            time.sleep(60)

        connection.close()
        print("Tiempo de ejecución completado (5 minutos).")


if __name__ == "__main__":
    main()
