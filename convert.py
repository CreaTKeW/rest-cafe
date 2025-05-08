import psycopg2
import os
import sqlite3
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

# Configure connection
sqlite_db_path = os.getenv('SQLITE_PATH')
postgres_conn_str = os.getenv('POSTGRES_CONN')

# Create SQLAlchemy engine for PostgreSQL for easier saving process
pg_engine = create_engine(postgres_conn_str)

# Connect with SQLite and create a cursor
conn_sqlite = sqlite3.connect(sqlite_db_path)
cursor_sqlite = conn_sqlite.cursor()

# Get a list of tables from SQLite
cursor_sqlite.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor_sqlite.fetchall()

for table_name_tuple in tables:
    table_name = table_name_tuple[0]
    print(f"Converting table: {table_name}")

    # Read data from SQLite tables to DataFrame Pandas
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn_sqlite)

    # Save DataFrame to PostgreSQL
    try:
        df.to_sql(table_name, pg_engine, if_exists='replace', index=False)
        print(f"Table {table_name} has been successfully imported to PostgreSQL.")
    except Exception as e:
        print(f"Error while importing table: {table_name}: {e}")

# Close SQLite connection
conn_sqlite.close()