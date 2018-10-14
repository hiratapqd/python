import tkinter
from tkinter import *
from tkinter import messagebox

# import  backend

def view_command():
#	list1.delete(0,END)
#	for row in backend.view():
#		list1.insert(END,row)
		e1=server_text.get()
		e2=dbacost_text.get()
		e3=dailymin_text.get()
		e4=downt_text.get()

		l=[]
		l.append(e1)
		l.append(e2)
		l.append(e3)
		l.append(e4)

		savehours = 96+(260*int(e1)*int(e3))/60-130/60
		mgmtsavings=savehours*int(e2)-1495
		mgmtsavings="{:,.2f}".format(mgmtsavings, grouping=True)
		downsavings=23*int(e4)
		downsavings="{:,.2f}".format(downsavings, grouping=True)
		sav="Based in the given data, your company \nsaved US$" + str(mgmtsavings) + " using AimBetter" + "\n\nIf we considering the downtime savings, \nyour company saved more US$" + str(downsavings)

		messagebox.showinfo("AimBetter Savings", sav)
		print (l)

window=Tk()
window.wm_title("AimBetter ROI calculator")
l1=Label(window,text="# servers")
l1.grid(row=0,column=0,pady=10,padx=5)

l2=Label(window,text="DBA hourly Cost")
l2.grid(row=1,column=0,pady=10,padx=5)

l3=Label(window,text="Daily minutes spent \n monitoring activities")
l3.grid(row=2,column=0,pady=10,padx=5)

lbl_assumptions="Assumptions \n -the DBA spent 8 hours \ncreating management reports\n \n -4 events per year \nthat requires \n6 DBA hours \nto fix it."

l4=Label(window,text= lbl_assumptions)
l4.grid(row=0,column=2,rowspan=4,pady=10,padx=15)

l5=Label(window,text="Downtime Cost")
l5.grid(row=3,column=0,pady=10,padx=5)


server_text=StringVar(window,value=1)
e1=Entry(window,textvariable=server_text)
e1.grid(row=0,column=1,pady=10)

dbacost_text=StringVar(window,value=40)
e2=Entry(window,textvariable=dbacost_text)
e2.grid(row=1,column=1,pady=10)

dailymin_text=StringVar(window,value=30)
e3=Entry(window,textvariable=dailymin_text)
e3.grid(row=2,column=1,pady=10)

downt_text=StringVar(window,value=10000)
e4=Entry(window,textvariable=downt_text)
e4.grid(row=3,column=1,pady=10)


b1=Button(window,text="Calculate ROI",width=12,command=view_command)
b1.grid(row=4,column=1)

b2=Button(window,text="Close",width=12,command=window.destroy)
b2.grid(row=5,column=2)


window.mainloop()
