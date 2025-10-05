import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="maglev.proxy.rlwy.net",
        port=54922,
        user="root",
        password="EoBoENuYHtKPkLOFpUVEXoOCrQWiCMYf",
        database="railway"
    )
