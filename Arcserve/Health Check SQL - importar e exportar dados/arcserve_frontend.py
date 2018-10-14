from tkinter import *
import ashc_backend

def get_selected_row(event):
    global blur
    blur=[]
    index=list1.curselection()[0]
    h=int(index)
    listbox2.delete(0,END)
    for row in ashc_backend.lista_servers(ctl[h][0]):
        blur.append(row)
        listbox2.insert(END,row[0])


def view_command():
    global ctl
    ctl=[]
    list1.delete(0,END)
    for row in ashc_backend.lista_cliente():
        ctl.append(row)
        list1.insert(END,row)


def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def output_command():
    global blur
    blur=[]
    index=list1.curselection()[0]
    h=int(index)
    ashc_backend.out_data(ctl[h][0])
    view_command()

def update_command():
    global selected_tuple
    ashc_backend.insert_table()
    view_command()

window=Tk()

window.wm_title("ArcServe Brazil Health Check")

l1=Label(window,text="Cliente")
l1.grid(row=0,column=0, sticky=S, padx=10,pady=10)

l2=Label(window,text="Servidor")
l2.grid(row=2,column=0, sticky=S, padx=10,pady=10)

list1=Listbox(window, selectmode='single', height=6,width=20)
list1.grid(row=0,column=1,rowspan=2,columnspan=2,padx=10,pady=10)

sb1=Scrollbar(window)
sb1.grid(row=0,column=3,rowspan=2)

#lista os servidores
listbox2=Listbox(window, selectmode='single', height=6,width=20)
listbox2.grid(row=2,column=1,rowspan=2,columnspan=2,padx=10,pady=10)

sb2=Scrollbar(window)
sb2.grid(row=2,column=3,rowspan=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
listbox2.configure(yscrollcommand=sb2.set)
sb2.configure(command=listbox2.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

#b4=Button(window,text="Importar novos dados \n Update selecte", width=20,command=update_command)
b4=Button(window,text="Importar novos dados", width=20,command=update_command)
b4.grid(row=0,column=5, sticky=S, padx=10,pady=10)

b5=Button(window,text="Exportar resultados", width=20,command=output_command)
b5.grid(row=1,column=5, sticky=S, padx=10,pady=10)

b6=Button(window,text="Close", width=20,command=window.destroy)
b6.grid(row=2,column=5, sticky=S, padx=10,pady=10)
view_command()
window.mainloop()
