import os
from dotenv import load_dotenv
import snowflake.connector

# Load credentials from .env
load_dotenv()

conn = snowflake.connector.connect(
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA"),
    role=os.getenv("SNOWFLAKE_ROLE")
)

cur = conn.cursor()
cur.execute("SELECT CURRENT_VERSION(), CURRENT_DATABASE(), CURRENT_SCHEMA();")
row = cur.fetchone()
print(f"\nConnected successfully!")
print(f"Snowflake Version: {row[0]}")
print(f"Current Database : {row[1]}")
print(f"Current Schema   : {row[2]}\n")

cur.close()
conn.close()