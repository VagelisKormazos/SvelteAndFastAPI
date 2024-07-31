from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pyodbc

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure database connection
DATABASE_CONFIG = {
    'DRIVER': 'ODBC Driver 17 for SQL Server',
    'SERVER': 'localhost',  # ή η IP του server σου
    'DATABASE': 'RachesDB',
    'UID': 'sa',
    'PWD': 'v@gelis'
}

def get_db_connection():
    connection_string = (
        f"DRIVER={{{DATABASE_CONFIG['DRIVER']}}};"
        f"SERVER={DATABASE_CONFIG['SERVER']};"
        f"DATABASE={DATABASE_CONFIG['DATABASE']};"
        f"UID={DATABASE_CONFIG['UID']};"
        f"PWD={DATABASE_CONFIG['PWD']}"
    )
    try:
        conn = pyodbc.connect(connection_string)
        return conn
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {str(e)}")

@app.get("/businesses")
async def get_businesses():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM businesses")
        rows = cursor.fetchall()
        businesses = []
        for row in rows:
            businesses.append({
                "id": row[0],
                "name": row[1],
                "address": row[2],
                "phone": row[3],
                "email": row[4]
            })
        return {"businesses": businesses}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database query error: {str(e)}")
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
