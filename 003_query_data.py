import sqlite3

# Abre una conexión a la base de datos SQLite llamada 'test.db'
with sqlite3.connect("test.db") as conn:
    # Crea un cursor para ejecutar comandos SQL
    cursor = conn.cursor()

    # Consulta SQL para seleccionar todos los usuarios cuyo nombre contiene 'Torres'
    script = """
    SELECT * FROM users WHERE name LIKE '%Torres%'
    """
    data_filter = cursor.execute(script).fetchall()
    # Imprime los resultados filtrados por nombre
    print(data_filter)

    # Consulta SQL para seleccionar todos los usuarios ordenados por nombre
    script = """
    SELECT * FROM users ORDER BY name
    """
    data_ordered = cursor.execute(script).fetchall()
    # Imprime los resultados ordenados por nombre
    print(data_ordered)