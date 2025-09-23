import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="caboose.proxy.rlwy.net",
        port=21524,
        user="root",
        password="ETwRBCQNqljqYEnQmDXBHRJEcmyAKPcA",
        database="expense"
    )
