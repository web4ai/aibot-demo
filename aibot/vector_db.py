import psycopg2
from pgvector.psycopg2 import register_vector

DATABASE_URL = "postgresql://user:password@localhost/dbname"


def get_connection():
    conn = psycopg2.connect(DATABASE_URL)
    register_vector(conn)
    return conn


def insert_vector(table_name, vector):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"INSERT INTO {table_name} (embedding) VALUES (%s)", (vector,))
    conn.commit()
    cursor.close()
    conn.close()


def query_similar_vectors(table_name, vector, top_k=5):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT id, embedding <-> %s AS distance
        FROM {table_name}
        ORDER BY distance
        LIMIT %s
    """, (vector, top_k))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
