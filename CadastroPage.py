from tkinter import *
from tkinter import messagebox
import ast

window=Tk()
window.title("INCREVA-SE")
window.geometry('925x500+300+200')
window.config(bg="#fff")
window.resizable(False, False)

#definindo função de logar
def signup():
    username = user.get()
    password = code.get()
    conform = code.get()

    if password == conform:
        try:
            file=open('datasheet.txt', 'r+')
            d=file.read()
            r=ast.literal_eval(d)

            dict2={username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file=open('datasheet.txt', 'w')
            w=file.write(str(r))

            messagebox.showinfo('Inscrição', 'Realizada com sucesso!')

        except:
            file=open('datasheet.txt', 'w')
            pp=str({'Username': 'password'})
            file.write(pp)
            file.close()
    else:
        messagebox.showerror('Invalido', 'As senha não conferem')

def sign():
    window.destroy()



img = PhotoImage(file='login2.png')
Label(window, image=img, bg='white').place(x=50, y=90)

frame=Frame(window, width=350, height=390, bg='#fff')
frame.place(x=480, y=50)

heading=Label(frame, text='inscreva-se', fg="#57a1f8", bg='white', font=('Arial Narrow', 23, 'bold'))
heading.place(x=100, y=5)

#####------------------------------------------------------------------

def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    if user.get() == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Arial Narrow', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)


#####------------------------------------------------------------------

def on_enter(e):
    code.delete(0, 'end')
def on_leave(e):
    if code.get() == '':
        code.insert(0, 'Password')

code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Arial Narrow', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

#####------------------------------------------------------------------

def on_enter(e):
    conform.delete(0, 'end')
def on_leave(e):
    if conform.get() == '':
        conform.insert(0, 'Confirm Password')

conform = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Arial Narrow', 11))
conform.place(x=30, y=220)
conform.insert(0, 'Confirm Password')
conform.bind('<FocusIn>', on_enter)
conform.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

#####------------------------------------------------------------------

Button(frame, width=39, pady=7, text='Inscrever-se', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)
label= Label(frame, text="Já estou logado", fg='black', bg='white', font=('Arial Narrow', 9))
label.place(x=90, y=340)

signin= Button(frame, width=6, text='Sign In', border=0, bg='white', cursor='hand2', fg='#57a1f8')
signin.place(x=200, y=340)




window.mainloop()

