import mysql.connector as con

con1 = con.connect(host = "localhost", user = "root", password = "shubham@1234", database = "train")
cur1 = con1.cursor()

sql = "select * from train_stations"
cur1.execute(sql)

rec = cur1.fetchall()

lst = []

for i in rec:
    lst.append(i[2])

print(lst)