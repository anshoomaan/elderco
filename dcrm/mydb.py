#install mysql on  your desktop
#pip install mysql
#pip install mysql-connector
#pip install mysql-connnectro-python


#setting up a database
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost' ,
    user = 'root' ,
    passwd = 'anshoomaan' ,
    
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE elderco")

print ("All done !")