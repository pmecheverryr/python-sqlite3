import sqlite3

# Abre una conexión a la base de datos SQLite llamada 'test.db'
with sqlite3.connect("test.db") as conn:
    # Crea un cursor para ejecutar comandos SQL
    cursor = conn.cursor()

    # Actualiza el email del usuario con id = 1
    script = """
    UPDATE users SET email = 'ana.perez@server.com' WHERE id = 1
    """
    conn.execute(script)
    conn.commit()  # Confirma los cambios en la base de datos

    # Consulta todos los usuarios para mostrar el resultado de la actualización
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()

    print(result)