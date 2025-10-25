import psycopg2
from psycopg2.extras import RealDictCursor

# Database configuration
DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = "postgres"
DB_PASSWORD = "123654789"
DB_NAME = "postgres"

conn = None  # initialize the connection variable

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    #RealDictCursor
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        # CREATE TABLE
        cur.execute("""
            CREATE TABLE IF NOT EXISTS products (
            product_id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            price NUMERIC(6, 2) NOT NULL,
            in_stock BOOLEAN DEFAULT TRUE
);
        """)
        conn.commit()

        # INSERT DATA
        cur.execute("""
            INSERT INTO products (name, price, in_stock) VALUES
             ('Laptop', 3200.50, TRUE),
             ('Mouse', 99.99, TRUE),
             ('Keyboard', 250.00, FALSE),
             ('Monitor', 1190.95, TRUE);
        """)
        conn.commit()

        # SELECT only products that are in stock
        cur.execute("SELECT * FROM products WHERE in_stock = TRUE;")
        results = cur.fetchall()

        #Results
        print("✅ Products currently in stock:")
        for row in results:
            print(row)

except psycopg2.Error as e:
    print("Database error:", e)

except Exception as e:
    print("Unexpected error:", e)

finally:
    if conn:
        conn.close()
        print("🔒 Database connection closed.")#

