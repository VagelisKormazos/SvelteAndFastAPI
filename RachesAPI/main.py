from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pyodbc
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure database connection using environment variables
DATABASE_CONFIG = {
    'DRIVER': os.getenv('DATABASE_DRIVER'),
    'SERVER': os.getenv('DATABASE_SERVER'),
    'DATABASE': os.getenv('DATABASE_NAME'),
    'UID': os.getenv('DATABASE_USER'),
    'PWD': os.getenv('DATABASE_PASSWORD')
}

def get_db_connection():
    try:
        connection_string = (
            f"DRIVER={DATABASE_CONFIG['DRIVER']};"
            f"SERVER={DATABASE_CONFIG['SERVER']};"
            f"DATABASE={DATABASE_CONFIG['DATABASE']};"
            f"UID={DATABASE_CONFIG['UID']};"
            f"PWD={DATABASE_CONFIG['PWD']}"
        )
        connection = pyodbc.connect(connection_string)
        return connection
    except pyodbc.Error as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {e}")

@app.get("/businesses")
async def get_businesses():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM businesses")
        
        # Ανάκτηση των δεδομένων ως λεξικό
        rows = dictfetchall(cursor)
        cursor.close()
        conn.close()
        return rows
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching businesses: {e}")

def dictfetchall(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
