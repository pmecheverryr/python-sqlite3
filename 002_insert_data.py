import sqlite3

# Lista de usuarios de ejemplo, cada uno representado como una tupla (nombre, correo electrónico)
usuarios = [
    ("Ana Pérez", "ana.perez@example.com"),
    ("Luis Gómez", "luis.gomez@example.com"),
    ("María López", "maria.lopez@example.com"),
    ("Carlos Ruiz", "carlos.ruiz@example.com"),
    ("Sofía Torres", "sofia.torres@example.com"),
]

# Conexión a la base de datos SQLite llamada 'test.db'
with sqlite3.connect("test.db") as conn:
    cursor = conn.cursor()
    # Inserta múltiples usuarios en la tabla 'users' usando una consulta parametrizada
    cursor.executemany(
        "INSERT INTO users (name, email) VALUES (?, ?)", usuarios
    )
    conn.commit()  # Guarda los cambios en la base de datos
    # Recupera y muestra todos los registros de la tabla 'users'
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())
