import mysql.connector
try:
    con = mysql.connector.connect(host="127.0.0.1", username="root", password="", database="edu_connect")
    if con.is_connected():  # check if successfully connected
        db = con.cursor()  # hold connection response and data
       # sql = "INSERT STUDENT(fname, lname, email,password) VALUES('Muyizere','Berissa', '@alustudent', '123' )"
        sql = "SELECT *FROM student"
        db.execute(sql)
        users = db.fetchall()
        for user in users:
            print(user)
except Exception as error:  # if error caught then print it
    print(f"\033[32mError{error}")  # print error
print()
