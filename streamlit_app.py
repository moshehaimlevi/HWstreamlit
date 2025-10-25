import streamlit as st
import psycopg2
from psycopg2.extras import RealDictCursor

########### SECTION A ###########

########### Calculator UI ###########

########### Title ###########
st.title("Calculator App by [Moshe]")

########### Input fields ###########
num1 = st.text_input("Enter first number:")
num2 = st.text_input("Enter second number:")

########### Button to perform addition ###########
if st.button("Add"):
    try:
        # Convert to float and add
        result = float(num1) + float(num2)
        st.success(f"The result is: {result}")
    except ValueError:
        st.error("Please enter valid numbers.")


########### SECTION B ###########

st.subheader("Section B: Available Products")

if st.button("Show Products"):
    try:
        # Database
        DB_HOST = "localhost"
        DB_PORT = 5432
        DB_USER = "postgres"
        DB_PASSWORD = "123654789"
        DB_NAME = "postgres"

        # Connect to PostgreSQL
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )

        #Running query
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM products WHERE in_stock = TRUE;")
            products = cur.fetchall()

            if products:
                st.success("✅ Products currently in stock:")
                st.table(products)
            else:
                st.warning("No products available right now.")

    except psycopg2.Error as e:
        st.error(f"Database error: {e}")

    except Exception as e:
        st.error(f"Unexpected error: {e}")

    finally:
        if 'conn' in locals() and conn:
            conn.close()