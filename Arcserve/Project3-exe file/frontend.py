from tkinter import *
import backend

def view_command():
	list1.delete(0,END)
	for row in backend.load_initial():
		list1.insert(END,row[0])

def get_list_row(event):
		try:
			global selected_tuple
			index=list1.curselection()[0]
			selected_tuple=list1.get(index)
#			print(cmp)
			list2.delete(0,END)
			for row in backend.what_servers(selected_tuple):
		    		list2.insert(END,row[0])
		except IndexError:
			pass
	#	print(selected_tuple)
    #print(event)

def get_list2_row(event):
		try:
			global selected_tuple1
			global srv
			index=list2.curselection()[0]
			selected_tuple1=list2.get(index)
			list3.delete(0,END)
			e4.delete(0,END)
			e5.delete(0,END)
			for row in backend.how_many_bkp(selected_tuple1,selected_tuple):
		    		list3.insert(END,row[0])
			for row in backend.find_first(selected_tuple1,selected_tuple):
				e4.insert(END,row)
			for row in backend.find_last(selected_tuple1,selected_tuple):
				e5.insert(END,row)
		except IndexError:
			pass




#		print(selected_tuple)
#		print(selected_tuple1)

    #print(event)

def get_list3_row(event):
		try:
			global selected_tuple2
			global hm
			index=list3.curselection()[0]
			selected_tuple2=list3.get(index)
			e4.delete(0,END)
			e5.delete(0,END)
			for row in backend.find_first(selected_tuple1,selected_tuple):
				e4.insert(END,row)
			for row in backend.find_last(selected_tuple1,selected_tuple):
				e5.insert(END,row)
		except IndexError:
			pass
#		print(selected_tuple)
#		print(selected_tuple1)
#		print(selected_tuple2)



root=Tk()
root.wm_title("Arcserve Backup Information")

l1=Label(root,text="Customer")
l1.grid(row=0,column=0, sticky=S, padx=10,pady=10)

list1=Listbox(root, selectmode='single', height=6,width=20)
list1.grid(row=0,column=1,rowspan=2,columnspan=2,padx=10,pady=10)

sb1=Scrollbar(root)
sb1.grid(row=0,column=3,rowspan=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_list_row)

l2=Label(root,text="Server")
l2.grid(row=2,column=0, sticky=S, padx=10,pady=10)

list2=Listbox(root, selectmode='single', height=6,width=20)
list2.grid(row=2,column=1,rowspan=2,columnspan=2,padx=10,pady=10)

sb2=Scrollbar(root)
sb2.grid(row=2,column=3,rowspan=2)

list2.configure(yscrollcommand=sb2.set)
sb2.configure(command=list2.yview)

list2.bind('<<ListboxSelect>>',get_list2_row)

l3=Label(root,text="# backups")
l3.grid(row=0,column=4, sticky=S, padx=10,pady=10)

list3=Listbox(root, selectmode='single', height=6,width=20)
list3.grid(row=0,column=5,rowspan=2,columnspan=2,padx=10,pady=10)

sb3=Scrollbar(root)
sb3.grid(row=0,column=6,rowspan=2)

list3.configure(yscrollcommand=sb3.set)
sb3.configure(command=list3.yview)

list3.bind('<<ListboxSelect>>',get_list3_row)

l4=Label(root,text="First Backup")
l4.grid(row=2,column=4,padx=10,pady=10)

firstbkp_text=StringVar()
e4=Entry(root,textvariable=firstbkp_text)
e4.grid(row=2,column=5)

l5=Label(root,text="Last Backup")
l5.grid(row=3,column=4,padx=10,pady=10)

lastbkp_text=StringVar()
e5=Entry(root,textvariable=lastbkp_text)
e5.grid(row=3,column=5)

b6=Button(root,text="Close", width=20,command=root.destroy)
b6.grid(row=5,column=5, sticky=S, padx=10,pady=10)

view_command()

root.mainloop()
