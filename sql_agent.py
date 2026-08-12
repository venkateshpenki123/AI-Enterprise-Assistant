import sqlite3
import pandas as pd


def get_tables():

    connection = sqlite3.connect(
        "enterprise.db"
    )

    cursor = connection.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        AND name NOT LIKE 'sqlite_%'
    """)

    tables = cursor.fetchall()

    connection.close()

    return [
        table[0]
        for table in tables
    ]


def execute_sql(query):

    connection = sqlite3.connect(
        "enterprise.db"
    )

    try:

        data = pd.read_sql_query(
            query,
            connection
        )

        return data

    finally:

        connection.close()