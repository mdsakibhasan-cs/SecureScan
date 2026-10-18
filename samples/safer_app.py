import os
import sqlite3
from pathlib import Path

password = os.environ.get("APP_PASSWORD")

user_input = input("Enter username: ").strip()

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute(
    "SELECT * FROM users WHERE name = ?",
    (user_input,)
)

safe_directory = Path("data").resolve()
requested_file = (safe_directory / "example.txt").resolve()

if requested_file.is_relative_to(safe_directory):
    with requested_file.open("r", encoding="utf-8") as file:
        data = file.read()

print(data)
