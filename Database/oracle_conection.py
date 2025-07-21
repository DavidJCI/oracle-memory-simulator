import cx_Oracle

try:
    conexion=cx_Oracle.connect(
        user='SYSTEM',
        password='12345',
        dsn='localhost/xe')
except Exception as err:
    print('Error a conectar', err)
else:
    print('conectado correctamente', conexion.version)

cursor_bot_1=conexion.cursor()
cursor_bot_1.execute('create table ')

conexion.close()

