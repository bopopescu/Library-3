import tkinter as tk
import globalVar
import mysql.connector

class bookissue :
    def onclick ( self, Entry1, Entry2, bi, lable3, lable4 ) :
        lable3.configure(text="")
        lable4.configure(text="")
        if Entry1.get() == '' or Entry2.get() == '' :
            lable3.configure(text="Entry Cannot be empty")
        else :
            bookref = Entry1.get()
            nameref = Entry2.get()
            if bookref.isdigit() :
                sql = "SELECT * FROM books WHERE bookId =%s"
                val = (bookref,)
                globalVar.db1 = mysql.connector.connect(host="localhost", user=globalVar.username,passwd=globalVar.password, database="LIBRARY")
                c = globalVar.db1.cursor()
                c.execute(sql, val)
                resbook = c.fetchall()
                if len(resbook) == 0 :
                    lable3.configure(text="Book Not Found ")
                    globalVar.db1.close()
                else :
                    row = resbook[0]
                    lable3.configure(text="Book ID : " + str(row[0]) + " \n" + "Book Name : " + row[1] + " \n" + "Quantity : " + str(row[2]))
                    globalVar.db1.close()
            else :
                sql = "SELECT * FROM books WHERE bookName =%s"
                val = (bookref,)
                globalVar.db1 = mysql.connector.connect(host="localhost", user=globalVar.username,passwd=globalVar.password, database="LIBRARY")
                c = globalVar.db1.cursor()
                c.execute(sql, val)
                resbook = c.fetchall()
                if len(resbook) == 0 :
                    lable3.configure(text="Book Not Found ")
                    globalVar.db1.close()
                else :
                    row = resbook[0]
                    lable3.configure(text="Book ID : " + str(row[0]) + " \n" + "Book Name : " + row[1] + " \n" + "Quantity : " + str(row[2]))
                    globalVar.db1.close()
            if nameref.isdigit() :
                sql = "SELECT * FROM student WHERE idNo =%s"
                val = (nameref,)
                globalVar.db1 = mysql.connector.connect(host="localhost", user=globalVar.username,passwd=globalVar.password, database="LIBRARY")
                c = globalVar.db1.cursor()
                c.execute(sql, val)
                resstud = c.fetchall()
                if len(resstud) == 0 :
                    lable4.configure(text="Student Not Found ")
                    globalVar.db1.close()
                else :
                    row = resstud[0]
                    lable4.configure(text="Student ID : " + str(row[0]) + " \n" + "Student Name : " + row[1])
                    globalVar.db1.close()
            else :
                sql = "SELECT * FROM student WHERE name =%s"
                val = (nameref,)
                globalVar.db1 = mysql.connector.connect(host="localhost", user=globalVar.username,passwd=globalVar.password, database="LIBRARY")
                c = globalVar.db1.cursor()
                c.execute(sql, val)
                resstud = c.fetchall()
                if len(resstud) == 0 :
                    lable4.configure(text="Student Not Found ")
                    globalVar.db1.close()
                else :
                    row = resstud[0]
                    lable4.configure(text="Student ID : " + str(row[0]) + " \n" + "Student Name : " + row[1])
                    c.close()
            if len(resstud) != 0 and len(resbook) != 0 and resbook[0][2] != 0:
                rows = resstud[0]
                rowb = resbook[0]
                sql = "INSERT INTO issue(bookId,idNo,issueDate,name,bookName) VALUES(%s,%s,current_Date(),%s,%s)"
                val = (rowb[0], rows[0], rows[1], rowb[1],)
                try :
                    globalVar.db1 = mysql.connector.connect(host="localhost", user=globalVar.username,passwd=globalVar.password, database="LIBRARY")
                    c = globalVar.db1.cursor()
                    c.execute(sql, val)
                    globalVar.db1.commit()
                    sql = "UPDATE books SET Quantity = %s WHERE books.bookId = %s"
                    val = (str(int(rowb[2]) - 1), rowb[0])
                    c.execute(sql, val)
                    globalVar.db1.commit()
                    globalVar.db1.close()
                except :
                    lable3.configure(text="Book Already issued")
                    lable4.configure(text="")
                    c.close()
            else :

                if len(resbook)==0:
                    lable3.configure(text="Book Not Found")
                    lable4.configure(text="")
                elif len(resstud)==0 :
                    lable3.configure(text="Student Not Found")
                    lable4.configure(text="")
                else:
                    lable3.configure(text="Book Out Of Stock")
                    lable4.configure(text="")

    def ui ( self ) :
        bi = tk.Tk()
        bi.geometry('800x150+550+300')
        Entry1 = tk.Entry(bi, width="15")
        Entry1.grid(row=0, column=1)
        Entry2 = tk.Entry(bi, width="15")
        Entry2.grid(row=1, column=1)
        bi.title("Book Issue")
        lable2 = tk.Label(bi, text="Student Name or Id")
        lable2.grid(row=1, column=0)
        lable1 = tk.Label(bi, text="Book Name or Id")
        lable1.grid(row=0, column=0)
        lable4 = tk.Label(bi, text="")
        lable4.grid(row=4, column=3)
        button1 = tk.Button(bi, text="ISSUE",command=lambda : bookissue.onclick(bookissue, Entry1, Entry2, bi, lable3, lable4),width="10", height="1")
        button1.grid(column=0, row=2)
        lable3 = tk.Label(bi, text="")
        lable3.grid(row=4, column=2)
        bi.mainloop()
