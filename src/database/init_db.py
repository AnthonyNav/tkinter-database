import sqlite3
def createDB():
    ## Este script preprar la base de datos (En caso de que no este ya creada) para la ejecución correcta del programa completo
    

    # Conectar a la base de datos (si no existe, se creará automáticamente)
    conexion = sqlite3.connect('src/database/movies.db')

    # Crear un cursor para ejecutar comandos SQL
    cursor = conexion.cursor()

    # Crear la tabla Peliculas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Peliculas (
            id_pel INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            duracion TEXT NOT NULL,
            categoria TEXT NOT NULL
        )
    """)

    # Crear la tabla Clientes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Miembros (
            id_mem INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT,
            direccion TEXT NOT NULL
        )
    """)

    # Crear la tabla Copias
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Copias (
            id_copy INTEGER PRIMARY KEY AUTOINCREMENT,
            formato TEXT NOT NULL CHECK (formato IN ('Beta', 'VHS', 'DVD')),
            precio REAL,
            fecharet TEXT,
            calidad TEXT NOT NULL CHECK (calidad IN ('NUEVA', 'BUENA', 'REGULAR', 'MALA', 'INSERVIBLE')),
            id_pelicula INTEGER,
            id_miembro INTEGER,
            FOREIGN KEY (id_pelicula) REFERENCES Peliculas(id_pel),
            FOREIGN KEY (id_miembro) REFERENCES Miembros(id_mem)
        )
    """)

    

    # Confirmar cambios
    conexion.commit()

    # Cerrar la conexión
    conexion.close()
