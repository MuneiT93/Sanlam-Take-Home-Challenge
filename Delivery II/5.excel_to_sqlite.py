import pandas as pd
import sqlite3

# 1. Read the Excel file (adjust the filename if needed)
excel_file = "Consolidated United Nations Security Council Sanctions List.xlsx"
df = pd.read_excel(excel_file, sheet_name=0, engine="openpyxl")  # Reads the first sheet

# 2. Clean the data (remove empty rows)
df = df.dropna(how='all')

# 3. Store in SQLite database
conn = sqlite3.connect("sanctions.db")
df.to_sql("sanctions_list", conn, if_exists="replace", index=False)
conn.close()

print("Ingestion complete! Data is now in sanctions.db")
