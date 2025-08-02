from db_config import get_connection

def add_transaction(date, amount, category, description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO expenses (date, amount, category, description)
        VALUES (%s, %s, %s, %s)
    """, (date, amount, category, description))
    conn.commit()
    conn.close()

def get_transactions(start_date, end_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT date, amount, category, description
        FROM expenses
        WHERE date BETWEEN %s AND %s
        ORDER BY date
    """, (start_date, end_date))
    results = cursor.fetchall()
    conn.close()
    return results

def get_totals_by_category():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
    """)
    results = cursor.fetchall()
    conn.close()
    return results

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            date DATE,
            amount DECIMAL(10, 2),
            category VARCHAR(255),
            description TEXT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
