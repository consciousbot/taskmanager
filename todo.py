import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user="root", passwd="", database = "TODO")

mycursor = mydb.cursor()
#mycursor.execute("SELECT * FROM TODOS")
#res = mycursor.fetchall()
#for i in res:
#    print(i)

def print_data(res):
    for i in res:
        print(i)


def add_data(todo, start, end):
    mycursor.execute("INSERT INTO TODOS(TODO, DATE_OF_CREATION, TO_BE_COMPLETED_BY) VALUES(%s,%s,%s)", (todo, start, end))
    mydb.commit()
    print("SUCCESS")

def clear_table():
    mycursor.execute("DELETE FROM TODOS")
    mydb.commit()
    print("SUCCESS")

print("----------TASK MANAGER----------")
print("OPTIONS:")
print("1)SHOW ALL THE TASKS")
print("2)ADD A TASK")
print("3)CLEAR THE TABLE")
option = int(input("OPTION:"))
if option == 1:
    mycursor.execute("SELECT * FROM TODOS")
    res = mycursor.fetchall()
    print_data(res)
elif option == 2:
    string = str(input("ADD A TODO:"))
    start_date = str(input("ENTER THE START DATE(YYYY-MM-DD) :"))
    end_date = str(input("ENTER THE END DATE(YYYY-MM-DD)     :"))
    add_data(string, start_date, end_date)
elif option == 3:
    clear_table()






