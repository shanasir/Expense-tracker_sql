
import csv
from datetime import datetime
from db_config import get_connection

def import_csv_to_mysql(csv_file):
    conn = get_connection()
    cursor = conn.cursor()
    print("Starting CSV import...")

    inserted_count = 0
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                # Convert date format
                date_obj = datetime.strptime(row["date"], "%d-%m-%Y")
                formatted_date = date_obj.strftime("%Y-%m-%d")

                cursor.execute("""
                    INSERT INTO expenses (date, amount, category, description)
                    VALUES (%s, %s, %s, %s)
                """, (formatted_date, float(row["amount"]), row["category"], row["description"]))
                inserted_count += 1
            except Exception as e:
                print(f"Error inserting row {row}: {e}")

    conn.commit()
    conn.close()
    print(f"{inserted_count} rows imported successfully.")

if __name__ == "__main__":
    import_csv_to_mysql("finance.csv")
