import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='password')

cursor = connection.cursor()

# 創建資料庫
cursor.execute("CREATE DATABASE `database`;")


# 取得所有資料庫名稱
# cursor.execute("SHOW DATABASES;")
# records = cursor.fetchall()
# for r in records:
#     print(r)


# 選擇資料庫
# cursor.execute("USE `sql_tutorial`;")


# 創建表格
# cursor.execute('CREATE TABLE `qq`(qq INT);')

cursor.close()
connection.close()
