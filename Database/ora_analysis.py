import cx_Oracle
import time
from datetime import datetime

try:
    # Conexión a Oracle
    conexion = cx_Oracle.connect(
        user='SYSTEM',
        password='12345',
        dsn='localhost/xe'
    )
except Exception as err:
    print('Error al conectar:', err)
else:
    print('Conectado correctamente', conexion.version)

    try:
        # Archivo donde se guardarán los datos
        archivo = "free_memory_data.txt"

        # Tiempo de inicio
        tiempo_inicio = time.time()
        tiempo_limite = 10 * 60  # 5 minutos en segundos

        while time.time() - tiempo_inicio < tiempo_limite:
            # Crear el cursor para ejecutar la consulta
            cursor = conexion.cursor()

            # Consulta para obtener memoria libre
            query = "SELECT NAME, BYTES / 1024 / 1024 AS VALUE_MB FROM V$SGASTAT WHERE POOL = 'shared pool' AND NAME LIKE '%free memory'"
            cursor.execute(query)
            resultados = cursor.fetchall()

            # Extraer los datos y guardar en formato requerido
            datos = []
            horas = []

            for fila in resultados:
                # Convertir cada fila a un formato de texto separado por comas
                datos.append(", ".join(map(str, fila)))
                horas.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

            # Escribir en el archivo
            with open(archivo, "a") as file:  # Modo "append" para no sobrescribir
                # Agregar datos
                file.write(", ".join(datos) + "\n")
                # Agregar horas correspondientes
                file.write(", ".join(horas) + "\n")

            print("Datos guardados en el archivo.")

            # Esperar 30 segundos antes de la siguiente ejecución
            time.sleep(30)

    except Exception as query_err:
        print("Error al ejecutar las consultas:", query_err)

    finally:
        # Cerrar el cursor y la conexión
        if 'cursor' in locals():
            cursor.close()
        if 'conexion' in locals():
            conexion.close()
