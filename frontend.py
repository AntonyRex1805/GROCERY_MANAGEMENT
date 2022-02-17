from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

def clear_command():
    e1.delete(1,END)
    e2.delete(0,END)
    e3.delete(3,END)
    e4.delete(4,END)

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(SNo_text.get(),Product_text.get(),MRP_text.get(),Quantity_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(SNo_text.get(),Product_text.get(),MRP_text.get(),Quantity_text.get())
    list1.delete(0,END)
    list1.insert(END,(SNo_text.get(),Product_text.get(),MRP_text.get(),Quantity_text.get()))
    clear_command()
    view_command()

def delete_command():
    backend.delete(selected_tuple[0])
    clear_command()
    view_command()

def update_command():
    backend.update(selected_tuple[0],SNo_text.get(),Product_text.get(),MRP_text.get(),Quantity_text.get())
    clear_command()
    view_command()

window=Tk()

window.wm_title("GROCERY MANAGEMENT")

l1=Label(window,text="SNo")
l1.grid(row=0,column=0)

l2=Label(window,text="Product")
l2.grid(row=0,column=2)

l3=Label(window,text="MRP")
l3.grid(row=1,column=0)

l4=Label(window,text="Quantity")
l4.grid(row=1,column=2)

SNo_text=StringVar(value="#")
e1=Entry(window,textvariable=SNo_text)
e1.grid(row=0,column=1)

Product_text=StringVar()
e2=Entry(window,textvariable=Product_text)
e2.grid(row=0,column=3)

MRP_text=StringVar(value="Rs.")
e3=Entry(window,textvariable=MRP_text)
e3.grid(row=1,column=1)

Quantity_text=StringVar(value="Nos.")
e4=Entry(window,textvariable=Quantity_text)
e4.grid(row=1,column=3)

list1=Listbox(window, height=15,width=75)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry", width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry", width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected", width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
