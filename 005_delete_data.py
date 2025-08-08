import sqlite3

# Abre una conexión a la base de datos SQLite llamada 'test.db'
with sqlite3.connect("test.db") as conn:
    # Crea un cursor para ejecutar comandos SQL
    cursor = conn.cursor()

    # Elimina el usuario con id = 5
    script = """
    DELETE FROM users WHERE id = 5
    """
    cursor.execute(script)
    conn.commit()

    # Consulta todos los usuarios para mostrar el resultado de la eliminación
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()

    print(result)