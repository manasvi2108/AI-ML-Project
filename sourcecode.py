import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression

conn = sqlite3.connect("mess.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS mess_data (
    day INTEGER,
    menu_type INTEGER,
    attendance INTEGER
)
""")
conn.commit()

sample_data = [
    (1, 1, 120),
    (2, 2, 150),
    (3, 1, 130),
    (4, 3, 180),
    (5, 2, 160),
    (6, 1, 110),
    (7, 3, 170)
]

cursor.executemany("INSERT INTO mess_data VALUES (?, ?, ?)", sample_data)
conn.commit()

df = pd.read_sql_query("SELECT * FROM mess_data", conn)

X = df[['day', 'menu_type']]
y = df['attendance']

model = LinearRegression()
model.fit(X,y)

print("Enter details for prediction:")

day = int(input("Day (1-7): "))
menu = int(input("Menu Type (1-Veg, 2-Mixed, 3-Special): "))

prediction = model.predict([[day, menu]])

print(f"\nPredicted Mess Demand: {int(prediction[0])} students")

actual = int(input("Enter actual attendance (for learning): "))

cursor.execute("INSERT INTO mess_data VALUES (?, ?, ?)", (day,menu, actual))
conn.commit()
