import mysql.connector
try:
    con = mysql.connector.connect(host="127.0.0.1", username="root", password="", database="edu_connect")
    if con.is_connected():  # check if successfully connected
        db = con.cursor()  # hold connection response and data
        db.execute("SHOW tables")
      #data = db.fetchall()
        #print(data)
except Exception as error:  # if error caught then print it
    print(f"\033[32mError{error}")  # print error
print()
# *******************inserting*************************

"""try:
    con = mysql.connector.connect(host="127.0.0.1", username="root", password="", database="edu_connect")
    if con.is_connected():  # check if successfully connected
        db = con.cursor()  # hold connection response and data
       # sql = "INSERT STUDENT(fname, lname, email,password) VALUES('Muyizere','Berissa', '@alustudent', '123' )"
        fname = input("enter first name")
        lname = input("enter last name: ")
        email = input("enter email")
        password = input("enter password")
        values = (fname, lname, email,password )
        sql = "INSERT STUDENT(fname, lname, email,password) VALUES(%s,%s,%s, %s)"
        db.execute(sql, values)
        con.commit()
        if db.rowcount > 0:
            print("inserted well")
        else:
            print("insertion unsuccessful")
except Exception as error:  # if error caught then print it
    print(f"\033[32mError{error}")  # print error
print()"""
