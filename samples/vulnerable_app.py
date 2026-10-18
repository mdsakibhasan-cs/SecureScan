import os
import hashlib
import sqlite3

password = "admin123"
api_key = "ABC123SECRET"

user_input = input("Enter command: ")
os.system(user_input)

query = "SELECT * FROM users WHERE name = '" + user_input + "'"
connection = sqlite3.connect("users.db")
connection.execute(query)

hashlib.md5(password.encode())

with open(user_input, "r") as file:
    data = file.read()

eval(user_input)
