from tkinter import*
from tkinter import messagebox
import sqlite3 as sql

def add_task():
    task_string=task_field.get()
    if len(task_string)==0:
        messagebox.showinfo('Error','Field is Empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks values(?)',(task_string))
        list_update()
        task_field.delete(0,'end')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end',task)

def delete_task():
    try:
        the_value=task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
            the_cursor.execute('delete from tasks where title=?',(the_value,))
    except:
        messagebox.showinfo('Error','No Task Selected.Cannot Delete.')
    
def delete_all_tasks():
    message_box=messagebox.askyesno('Delete All','Are you sure?')
    if message_box==True:
        while(len(tasks)!=0):
            tasks.pop()
        the_cursor.execute('delete from tasks')
        list_update()

def clear_list():
    task_listbox.delete(0,'end')

def close():
    print(tasks)
    guiWindow.destroy()

def retrieve_database():
    while(len(tasks)!=0):
        tasks.pop()
    for row in the_cursor.execute('Select title from tasks'):
        tasks.append(row[0])

if __name__=="__main__":
    guiWindow=Tk()
    guiWindow.title("TO-DO List")
    guiWindow.geometry("500*450+750+250")
    guiWindow.resizable(0,0)
    guiWindow.configure(bg="#C5E5CF")

    the_connection=sql.connect('List of Tasks.db')
    the_cursor=the_connection.cursor()
    the_cursor.execute('create table if not exists tasks(title text)')

    tasks=[]

    functions_frame=Frame(guiWindow,bg="#8FF5FF")

    functions_frame.pack(side="top",expand=True,fill="both")

    task_label=Label(functions_frame,text="TO-DO-LIST\n Enter the Task title:",
        font=("alice","12","bold"),
        background="#8FF5FF",
        foreground="#EE6104",
    )
    task_label.place(X=30,Y=60)

    task_field=Entry(
        functions_frame,
        font=("alice","12","bold"),
        width=42,
        foreground="orange",
        background="white",
    )
    task_field.place(X=160,Y=40)

    add_button=Button(
        functions_frame,
        text="Add",
        width=12,
        bg="#D4BD0C",
        font=("alice","12","bold"),
        command=add_task,
    )
    
    del_button=Button(
        functions_frame,
        text="Remove",
        width=12,
        bg="#D4BD0C",
        font=("alice","12","bold"),
        command=delete_task,
    )

    del_all_button=Button(
        functions_frame,
        text="Delete All",
        width=12,
        font=("alice","12","bold"),
        bg="#D4BD0C",
        command=delete_all_tasks,
    )

    exit_button=Button(
        functions_frame,
        text="Exit"/"Close",
        width=52,
        bg="#D4BD0C",
        font=("alice","12","bold"),
        command=close
    )
    add_button.place(X=18,Y=90)
    del_button.place(X=240,Y=90)
    del_all_button.place(X=460,Y=90)
    exit_button.place(X=17,Y=330)

    task_listbox=Listbox(
        functions_frame,
        width=70,
        height=9,
        font="bold",
        selectmode='SINGLE',
        background="WHITE",
        foreground="ORANGE",
        selectbackground="#FF8C00",
        selectforeground="ORANGE"
    )
    task_listbox.place(X=16,Y=130)

    retrieve_database()
    list_update()
    guiWindow.mainloop()
    the_connection.commit()
    the_cursor.close()

    
    

    






    


