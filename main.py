import mysql.connector
from mysql.connector import Error
import telepot
from dotenv import load_dotenv
from datetime import datetime
import os

# Load environment variables from .env file
load_dotenv()

# Get environment variables
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Fungsi untuk memeriksa koneksi DB
def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    time_now = datetime.now()
    try:
        connection = mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_name
        )
        if connection.is_connected():
            message = "TIME: " + str(time_now) + "\nSTATUS: DWH UP ✅✅✅"
    except Error as e:
        message = "TIME: " + str(time_now) + f"\nSTATUS: DWH DOWN 🆘🆘🆘 \nREASON: {e}"
    return connection, message

# Buat objek bot
bot = telepot.Bot(TOKEN)

# Periksa koneksi DB
connection, message = create_connection(db_name, db_user, db_password, db_host, db_port)

# Kirim pesan ke Telegram
bot.sendMessage(CHAT_ID, message)

# Tutup koneksi DB jika berhasil dibuat
if connection:
    connection.close()
    print("Database connection closed.")
