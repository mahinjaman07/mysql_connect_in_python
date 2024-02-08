import mysql.connector
conn = mysql.connector.connect(host='localhost', password='Mahin##@@11', user='root')

if conn.is_connected:
    print('Connected')

else:
    print('Something is wrong')
                               
