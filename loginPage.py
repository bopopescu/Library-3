import tkinter as tk
def onClick():
    m.destroy()
    import dashboard
m = tk.Tk()
m.title("Login Page")
lable1 = tk.Label(m, text="username ")
lable1.grid(row=0, column=0)
Entry1 = tk.Entry(m, width="15")
Entry1.grid(row=0, column=1)
lable2 = tk.Label(m, text="Password ")
lable2.grid(row=1, column=0)
Entry2 = tk.Entry(m, width="15")
Entry2.grid(row=1, column=1)
button1 = tk.Button(m, text="Login", command=onClick, width="10", height="1")
button1.grid(column=1, row=2)
lable3 = tk.Label(m, text="")
lable3.grid(row=2, column=0)
m.mainloop()