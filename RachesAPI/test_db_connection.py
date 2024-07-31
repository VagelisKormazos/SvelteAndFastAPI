import pyodbc

DATABASE_CONFIG = {
    'DRIVER': 'ODBC Driver 17 for SQL Server',
    'SERVER': 'localhost',  # ή η IP του server σου
    'DATABASE': 'RachesDB',
    'UID': 'sa',
    'PWD': 'v@gelis'
}

try:
    connection_string = (
        f"DRIVER={{{DATABASE_CONFIG['DRIVER']}}};"
        f"SERVER={DATABASE_CONFIG['SERVER']};"
        f"DATABASE={DATABASE_CONFIG['DATABASE']};"
        f"UID={DATABASE_CONFIG['UID']};"
        f"PWD={DATABASE_CONFIG['PWD']}"
    )
    connection = pyodbc.connect(connection_string)
    print("Connection successful!")
except pyodbc.Error as e:
    print(f"Connection failed: {e}")
