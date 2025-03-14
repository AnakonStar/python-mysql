from .connection import get_connection
import mysql

def execute_query(query, fetch_one=False, params=None):
    conn = get_connection()
    if not conn:
        return None

    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(query, params or ())
        if query.strip().lower().startswith("select"):
            result = cursor.fetchone() if fetch_one else cursor.fetchall()
            cursor.fetchall()
            return result
        else:
            conn.commit()
            return cursor.rowcount
    except mysql.connector.Error as err:
        print(f"Erro no banco de dados: {err}")
        return None
    finally:
        cursor.close()
        conn.close()
