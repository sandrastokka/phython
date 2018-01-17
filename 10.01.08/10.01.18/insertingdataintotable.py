import sqlite3

def updateTable(updateSql):
    with sqlite3.connect("ShoeStore.db")as myDatabase:
        cursor = myDatabase.cursor()
        cursor.execute(updateSql)
        myDatabase.commit()

updateSql = "UPDATE costumer SET phone = 98753652 WHERE custumerID=1"

updateTable(updateSql)

