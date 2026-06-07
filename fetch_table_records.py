"""Fetch records from a specific MySQL table."""

import os

from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password, db_name):
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name,
        )
        if connection.is_connected():
            print(f"Connected to database '{db_name}'")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    return None


def fetch_records(connection, table_name, limit=None):
    try:
        cursor = connection.cursor()
        query = f"SELECT * FROM `{table_name}`"
        if limit is not None:
            query += f" LIMIT {int(limit)}"
        cursor.execute(query)
        rows = cursor.fetchall()
        print(f"Fetched {len(rows)} record(s) from table '{table_name}'")
        for row in rows:
            print(row)
        return rows
    except Error as e:
        print(f"Error fetching records from '{table_name}': {e}")
        return []


if __name__ == "__main__":
    load_dotenv()

    host = os.getenv("MYSQL_HOST", "localhost")
    user = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD")
    database = os.getenv("MYSQL_DATABASE")
    table = os.getenv("MYSQL_TABLE", "employees")
    row_limit = os.getenv("MYSQL_ROW_LIMIT")
    row_limit = int(row_limit) if row_limit and row_limit.isdigit() else None

    if not user or not password or not database:
        print("Missing MySQL credentials in .env. Please set MYSQL_USER, MYSQL_PASSWORD, and MYSQL_DATABASE.")
    else:
        conn = create_connection(host, user, password, database)
        if conn:
            try:
                fetch_records(conn, table, row_limit)
            finally:
                conn.close()
                print("MySQL connection closed")
