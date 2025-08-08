import sqlite3

# Abre una conexión a la base de datos SQLite llamada 'test.db'.
# Si el archivo no existe, se crea automáticamente.
with sqlite3.connect("test.db") as conn:
    # Elimina la tabla 'users' si ya existe para evitar conflictos al crearla de nuevo.
    conn.execute("DROP TABLE IF EXISTS users;")

    # Crea la tabla 'users' con los campos:
    # - id: entero, clave primaria, autoincremental
    # - name: texto, no nulo
    # - email: texto, único y no nulo
    conn.execute("""
         CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             email TEXT UNIQUE NOT NULL
         )
         """)

    # Crea un cursor para ejecutar consultas SQL.
    cursor = conn.cursor()

    # Consulta y muestra todas las tablas existentes en la base de datos.
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    print(cursor.fetchall())

    # Consulta y muestra todos los registros de la tabla 'users'.
    query = cursor.execute("SELECT * FROM users")
    print(query.fetchall())

    # Obtiene y muestra los nombres de las columnas de la tabla 'users'.
    cols = [description[0] for description in query.description]
    print(cols)