import pandas as pd
import sqlite3

def excel_to_db(excel_file, db_file):
    # Load Excel file
    xls = pd.ExcelFile(excel_file)
    
    # Connect to SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    for sheet_name in xls.sheet_names:
        # Read each sheet into a DataFrame
        df = xls.parse(sheet_name)
        
        # Save DataFrame to database
        df.to_sql(sheet_name, conn, if_exists='replace', index=False)
    
    # Close connection
    conn.close()

# Example usage
excel_to_db("task_9.xlsx", "task.db")