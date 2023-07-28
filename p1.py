from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import requests
import pandas as pd
import matplotlib.pyplot as plt
from pylab import plot,show,xlabel,ylabel
import numpy as np

mw = Tk()
mw.title("E.M.S")
mw.geometry("1030x700+300+50")
mw.configure(bg="DarkSeaGreen2")

def f1():
	mw.withdraw()
	aw.deiconify()
def f2():
	aw.withdraw()
	mw.deiconify()
def f3():
	mw.withdraw()
	vw.deiconify()
	vw_empdata.delete(1.0,END)
	info = ""
	con = None
	try:
		con = connect("rj.db")
		cursor = con.cursor()
		sql = ("select * from employee;")
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data:
			info += " Id = " + str(d[0]) + ",Name =  " + str(d[1]) + ",Salary = " + str(d[2]) + "\n"
		vw_empdata.insert(INSERT,info)		
	except Exception as e:
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close

def f4():
	vw.withdraw()
	mw.deiconify()
def f5():
	mw.withdraw()
	uw.deiconify()
def f6():
	uw.withdraw()
	mw.deiconify()
def f7():
	mw.withdraw()
	dw.deiconify()
def f8():
	dw.withdraw()
	mw.deiconify()
def f9():
	mw.withdraw()
	cw.deiconify()
def f10():
	cw.withdraw()
	mw.deiconify()


def save():
	con = None
	try:
		con = connect("rj.db")
		cursor = con.cursor()
		sql = ("insert into employee values('%s','%s','%s');")
		id = aw_entid.get()
		name = aw_entname.get()
		salary = aw_entsal.get()

		if id.isnumeric is False:
			showerror("Id","Enter Positive Integers Only")
		elif id.isalpha() is True:
			showerror("Id","Enter Positive integers only not alphabets")
		elif int(id) <= 0:
			showerror("Id","Enter Positive integers only")
		elif name.isnumeric() is True:
			showerror("Name","Enter Alphabets only not integers")
		elif (any(x.isalpha() for x in name)) and all(x.isalpha or x.isspace() for x in name) is False:
			showerror("Name","Enter only alphabets")
		elif len(name)<2:
			showerror("Name","Enter min. 2 alphabets")
		
		elif salary.isnumeric() is False:
			showerror("Salary","Enter positive integers only")
		elif float(salary) < 8000:
			showerror("Salary","Salary should be min of 8k")
		else:
			cursor.execute(sql%(id,name,salary))
			con.commit()
			showinfo("Success","Employee added")
		
		aw_entid.delete(0,END)
		aw_entname.delete(0,END)
		aw_entsal.delete(0,END)
		aw_entid.focus()
	except Exception as e:
		showerror("Mistake",e)
	finally:
		if con is not None:
			con.close



def update():
	con = None
	try:
		con = connect("rj.db")
		cursor = con.cursor()
		sql = ("update employee set name = '%s' , salary = '%s' where id = %s;")
		id = uw_entid.get()
		name = uw_entname.get()
		salary = uw_entsal.get()
		
		
		if id.isnumeric is False:
			showerror("Id","Invalid Id")
		elif id.isalpha() is True:
			showerror("Id","Enter Positive integers only not alphabets")
		elif int(id) <= 0:
			showerror("Id","Enter Positive integers only")
		elif name.isnumeric() is True:
			showerror("Name","Enter Alphabets only not integers")
		elif (any(x.isalpha() for x in name)) and all(x.isalpha or x.isspace() for x in name) is False:
			showerror("Name","Enter only alphabets")
		elif len(name)<2:
			showerror("Name","Enter min. 2 alphabets")
		
		elif salary.isnumeric() is False:
			showerror("Salary","Enter positive integers only")
		elif float(salary) < 8000:
			showerror("Salary","Salary should be min of 8k")
		else:
			cursor.execute(sql%(name,salary,id))
			if cursor.rowcount == 1:
				con.commit()
				showinfo("Success","record updated")
			else:
				showerror("Error", "Invalid Id")

		uw_entid.delete(0,END)
		uw_entname.delete(0,END)
		uw_entsal.delete(0,END)
		uw_entid.focus()
	except Exception as e:
		showerror("Mistake",e)
		con.rollback()
	finally:
		if con is not None:
			con.close


def delete():
	con = None
	try:
		con = connect("rj.db")
		cursor = con.cursor()
		sql = ("delete from employee where id = '%s';")
		id = dw_entid.get()
		
		if id.isnumeric is False:
			showerror("Id","Enter Positive Integers Only")
		elif id.isalpha() is True:
			showerror("Id","Enter Positive integers only not alphabets")
		elif int(id) <= 0:
			showerror("Id","Enter Positive integers only")
		
		else:
			cursor.execute(sql%(id))
			if cursor.rowcount == 1:
				showinfo("Success","Employee deleted")
				con.commit()
			else:
				showerror("Error","Employee does not exists")
		dw_entid.delete(0,END)
		dw_entid.focus()
	except Exception as e:
		showerror("Mistake",e)
	finally:
		if con is not None:
			con.close


def bar():
	con = None
	try:
		con = connect("rj.db")
		cursor = con.cursor()
		sql = "select * from employee order by salary desc limit 5 ;"
		cursor.execute(sql)
		data = cursor.fetchall()
		employeeIds = [i[0] for i in data]
		employeeSalary = [i[2] for i in data]
		plt.bar(employeeIds,employeeSalary,color=["red"],width=.3)
		plt.title('Top 5 Employee Salray Bar Chart')
		plt.xlabel('employeeIds')
		plt.ylabel('employeeSalary')
		plt.show()
	except Exception as e:
		showerror("Mistake",e)
	finally:
		if con is not None:
			con.close






y = 10
f = ("Comic Sans MS",30,"bold")
btnadd = Button(mw,text="Add",font=f,width=8,height=1,command=f1)
btnadd.pack(pady=y)
btnview = Button(mw,text="View",font=f,width=8,height=1,command=f3)
btnview.pack(pady=y)
btnupdate = Button(mw,text="Update",font=f,width=8,height=1,command=f5)
btnupdate.pack(pady=y)
btndelete = Button(mw,text="Delete",font=f,width=8,height=1,command=f7)
btndelete.pack(pady=y)
btncharts = Button(mw,text="Charts",font=f,width=8,height=1,command=f9)
btncharts.pack(pady=y)


labloc = Label(mw,font=f,bg="DarkSeaGreen2",height=1)
labloc.place(x=10,y=600)
labtemp = Label(mw,font=f,bg="DarkSeaGreen2",width=40,height=1)
labtemp.place(x=330,y=600)

try:
	wa = "https://ipinfo.io/"
	response = requests.get(wa)
	print(response)
	data = response.json()
	cityname = data["city"]
	labloc.configure(text="Location:" + cityname)
	a1 = "https://api.openweathermap.org/data/2.5/weather"
	a2 = "?q=" + cityname
	a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
	a4 = "&units=" + "metric"
	wa = a1 + a2 + a3 + a4
	res = requests.get(wa)
	data = res.json()
	temp = data["main"]["temp"]
	labtemp.configure(text="Temprature:" + str(temp) + "Dc")
except Exception as e:
	print("issue",e)

aw = Toplevel(mw)
aw.title("Add Employee")
aw.geometry("1000x700+300+50")
aw.configure(bg="LightSteelBlue2")

aw_labid = Label(aw,text="enter id:",font=f)
aw_entid = Entry(aw,font=f)
aw_labname = Label(aw,text="enter name:",font=f)
aw_entname = Entry(aw,font=f)
aw_labsal  = Label(aw,text="enter salary:",font=f)
aw_entsal = Entry(aw,font=f)
aw_btnsave = Button(aw,text="Save",font=f,width=8,height=1,command=save)
aw_btnback = Button(aw,text="Back",font=f,command=f2,width=8,height=1)
aw_labid.pack(pady=y)
aw_entid.pack(pady=y)
aw_labname.pack(pady=y)
aw_entname.pack(pady=y)
aw_labsal.pack(pady=y)
aw_entsal.pack(pady=y)
aw_btnsave.pack(pady=y)
aw_btnback.pack(pady=y) 
aw.withdraw()


vw = Toplevel(mw)
vw.title("View Employee")
vw.geometry("1200x700+200+50")
vw.configure(bg="MistyRose2")
vw_empdata = ScrolledText(vw,width=45,height=10,font=f)
vw_btnback = Button(vw,text="Back",font=f,command=f4)
vw_empdata.pack(pady=y) 
vw_btnback.pack(pady=y) 
vw.withdraw()
		

uw = Toplevel(mw)
uw.title("Update Employee")
uw.geometry("1000x700+300+50")
uw.configure(bg="PeachPuff2")
uw_labid = Label(uw,text="enter id:",font=f)
uw_entid = Entry(uw,font=f)
uw_labname = Label(uw,text="enter name:",font=f)
uw_entname = Entry(uw,font=f)
uw_labsal  = Label(uw,text="enter salary:",font=f)
uw_entsal = Entry(uw,font=f)
uw_btnsave = Button(uw,text="Save",font=f,width=8,height=1,command=update)
uw_btnback = Button(uw,text="Back",font=f,command=f6,width=8,height=1,)
uw_labid.pack(pady=y)
uw_entid.pack(pady=y)
uw_labname.pack(pady=y)
uw_entname.pack(pady=y)
uw_labsal.pack(pady=y)
uw_entsal.pack(pady=y)
uw_btnsave.pack(pady=y)
uw_btnback.pack(pady=y) 
uw.withdraw()





dw = Toplevel(mw)
dw.title("Delete Employee")
dw.geometry("1000x700+300+50")
dw.configure(bg="SkyBlue2")
dw_labid = Label(dw,text="enter id:",font=f)
dw_entid = Entry(dw,font=f)
dw_btnsave = Button(dw,text="Save",font=f,width=8,height=1,command=delete)
dw_btnback = Button(dw,text="Back",font=f,command=f8,width=8,height=1,)
dw_labid.pack(pady=y)
dw_entid.pack(pady=y)
from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import requests
import pandas as pd
import matplotlib.pyplot as plt
from pylab import plot,show,xlabel,ylabel
import numpy as np

mw = Tk()
mw.title("E.M.S")
mw.geometry("1030x700+300+50")
mw.configure(bg="DarkSeaGreen2")

def f1():
	mw.withdraw()
	aw.deiconify()
def f2():
	aw.withdraw()
	mw.deiconify()
def f3():
	mw.withdraw()
	vw.deiconify()
	vw_empdata.delete(1.0,END)
	info = ""
	con = None
	try:
		con = connect("rj.db")
		cursor = con.cursor()
		sql = ("select * from employee;")
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data:
			info += " Id = " + str(d[0]) + ",Name =  " + str(d[1]) + ",Salary = " + str(d[2]) + "\n"
		vw_empdata.insert(INSERT,info)		
	except Exception as e:
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close

def f4():
	vw.withdraw()
	mw.deiconify()
def f5():
	mw.withdraw()
	uw.deiconify()
def f6():
	uw.withdraw()
	mw.deiconify()
def f7():
	mw.withdraw()
	dw.deiconify()
def f8():
	dw.withdraw()
	mw.deiconify()
def f9():
	mw.withdraw()
	cw.deiconify()
def f10():
	cw.withdraw()
	mw.deiconify()


def save():
	con = None
	try:
		con = connect("rj.db")
		cursor = con.cursor()
		sql = ("insert into employee values('%s','%s','%s');")
		id = aw_entid.get()
		name = aw_entname.get()
		salary = aw_entsal.get()

		if id.isnumeric is False:
			showerror("Id","Enter Positive Integers Only")
		elif id.isalpha() is True:
			showerror("Id","Enter Positive integers only not alphabets")
		elif int(id) <= 0:
			showerror("Id","Enter Positive integers only")
		elif name.isnumeric() is True:
			showerror("Name","Enter Alphabets only not integers")
		elif (any(x.isalpha() for x in name)) and all(x.isalpha or x.isspace() for x in name) is False:
			showerror("Name","Enter only alphabets")
		elif len(name)<2:
			showerror("Name","Enter min. 2 alphabets")
		
		elif salary.isnumeric() is False:
			showerror("Salary","Enter positive integers only")
		elif float(salary) < 8000:
			showerror("Salary","Salary should be min of 8k")
		else:
			cursor.execute(sql%(id,name,salary))
			con.commit()
			showinfo("Success","Employee added")
		
		aw_entid.delete(0,END)
		aw_entname.delete(0,END)
		aw_entsal.delete(0,END)
		aw_entid.focus()
	except Exception as e:
		showerror("Mistake",e)
	finally:
		if con is not None:
			con.close



def update():
	con = None
	try:
		con = connect("rj.db")
		cursor = con.cursor()
		sql = ("update employee set name = '%s' , salary = '%s' where id = %s;")
		id = uw_entid.get()
		name = uw_entname.get()
		salary = uw_entsal.get()
		
		
		if id.isnumeric is False:
			showerror("Id","Invalid Id")
		elif id.isalpha() is True:
			showerror("Id","Enter Positive integers only not alphabets")
		elif int(id) <= 0:
			showerror("Id","Enter Positive integers only")
		elif name.isnumeric() is True:
			showerror("Name","Enter Alphabets only not integers")
		elif (any(x.isalpha() for x in name)) and all(x.isalpha or x.isspace() for x in name) is False:
			showerror("Name","Enter only alphabets")
		elif len(name)<2:
			showerror("Name","Enter min. 2 alphabets")
		
		elif salary.isnumeric is False:
			showerror("Salary","Enter integers only")
		elif float(salary) < 8000:
			showerror("Salary","Salary should be min of 8k")
		else:
			cursor.execute(sql%(name,salary,id))
			if cursor.rowcount == 1:
				con.commit()
				showinfo("Success","record updated")
			else:
				showerror("info", "Invalid Id")

		uw_entid.delete(0,END)
		uw_entname.delete(0,END)
		uw_entsal.delete(0,END)
		uw_entid.focus()
	except Exception as e:
		showerror("Mistake",e)
		con.rollback()
	finally:
		if con is not None:
			con.close


def delete():
	con = None
	try:
		con = connect("rj.db")
		cursor = con.cursor()
		sql = ("delete from employee where id = '%s';")
		id = dw_entid.get()
		
		if id.isnumeric is False:
			showerror("Id","Enter Positive Integers Only")
		elif id.isalpha() is True:
			showerror("Id","Enter Positive integers only not alphabets")
		elif int(id) <= 0:
			showerror("Id","Enter Positive integers only")
		
		else:
			cursor.execute(sql%(id))
			if cursor.rowcount == 1:
				showinfo("Success","Employee deleted")
				con.commit()
			else:
				showerror("Info","Employee does not exists")
		dw_entid.delete(0,END)
		dw_entid.focus()
	except Exception as e:
		showerror("Mistake",e)
	finally:
		if con is not None:
			con.close


def bar():
	con = None
	try:
		con = connect("rj.db")
		cursor = con.cursor()
		sql = "select * from employee order by salary desc limit 5 ;"
		cursor.execute(sql)
		data = cursor.fetchall()
		employeeIds = [i[0] for i in data]
		employeeSalary = [i[2] for i in data]
		plt.bar(employeeIds,employeeSalary,color=["red"],width=.3)
		plt.title('Top 5 Employee Salray Bar Chart')
		plt.xlabel('employeeIds')
		plt.ylabel('employeeSalary')
		plt.show()
	except Exception as e:
		showerror("Mistake",e)
	finally:
		if con is not None:
			con.close






y = 10
f = ("Comic Sans MS",30,"bold")
btnadd = Button(mw,text="Add",font=f,width=8,height=1,command=f1)
btnadd.pack(pady=y)
btnview = Button(mw,text="View",font=f,width=8,height=1,command=f3)
btnview.pack(pady=y)
btnupdate = Button(mw,text="Update",font=f,width=8,height=1,command=f5)
btnupdate.pack(pady=y)
btndelete = Button(mw,text="Delete",font=f,width=8,height=1,command=f7)
btndelete.pack(pady=y)
btncharts = Button(mw,text="Charts",font=f,width=8,height=1,command=f9)
btncharts.pack(pady=y)


labloc = Label(mw,font=f,bg="DarkSeaGreen2",height=1)
labloc.place(x=10,y=600)
labtemp = Label(mw,font=f,bg="DarkSeaGreen2",width=40,height=1)
labtemp.place(x=330,y=600)

try:
	wa = "https://ipinfo.io/"
	response = requests.get(wa)
	print(response)
	data = response.json()
	cityname = data["city"]
	labloc.configure(text="Location:" + cityname)
	a1 = "https://api.openweathermap.org/data/2.5/weather"
	a2 = "?q=" + cityname
	a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
	a4 = "&units=" + "metric"
	wa = a1 + a2 + a3 + a4
	res = requests.get(wa)
	data = res.json()
	temp = data["main"]["temp"]
	labtemp.configure(text="Temprature:" + str(temp) + "Dc")
except Exception as e:
	print("issue",e)

aw = Toplevel(mw)
aw.title("Add Employee")
aw.geometry("1000x700+300+50")
aw.configure(bg="LightSteelBlue2")

aw_labid = Label(aw,text="enter id:",font=f)
aw_entid = Entry(aw,font=f)
aw_labname = Label(aw,text="enter name:",font=f)
aw_entname = Entry(aw,font=f)
aw_labsal  = Label(aw,text="enter salary:",font=f)
aw_entsal = Entry(aw,font=f)
aw_btnsave = Button(aw,text="Save",font=f,width=8,height=1,command=save)
aw_btnback = Button(aw,text="Back",font=f,command=f2,width=8,height=1)
aw_labid.pack(pady=y)
aw_entid.pack(pady=y)
aw_labname.pack(pady=y)
aw_entname.pack(pady=y)
aw_labsal.pack(pady=y)
aw_entsal.pack(pady=y)
aw_btnsave.pack(pady=y)
aw_btnback.pack(pady=y) 
aw.withdraw()


vw = Toplevel(mw)
vw.title("View Employee")
vw.geometry("1200x700+200+50")
vw.configure(bg="MistyRose2")
vw_empdata = ScrolledText(vw,width=45,height=10,font=f)
vw_btnback = Button(vw,text="Back",font=f,command=f4)
vw_empdata.pack(pady=y) 
vw_btnback.pack(pady=y) 
vw.withdraw()
		

uw = Toplevel(mw)
uw.title("Update Employee")
uw.geometry("1000x700+300+50")
uw.configure(bg="PeachPuff2")
uw_labid = Label(uw,text="enter id:",font=f)
uw_entid = Entry(uw,font=f)
uw_labname = Label(uw,text="enter name:",font=f)
uw_entname = Entry(uw,font=f)
uw_labsal  = Label(uw,text="enter salary:",font=f)
uw_entsal = Entry(uw,font=f)
uw_btnsave = Button(uw,text="Save",font=f,width=8,height=1,command=update)
uw_btnback = Button(uw,text="Back",font=f,command=f6,width=8,height=1,)
uw_labid.pack(pady=y)
uw_entid.pack(pady=y)
uw_labname.pack(pady=y)
uw_entname.pack(pady=y)
uw_labsal.pack(pady=y)
uw_entsal.pack(pady=y)
uw_btnsave.pack(pady=y)
uw_btnback.pack(pady=y) 
uw.withdraw()





dw = Toplevel(mw)
dw.title("Delete Employee")
dw.geometry("1000x700+300+50")
dw.configure(bg="SkyBlue2")
dw_labid = Label(dw,text="enter id:",font=f)
dw_entid = Entry(dw,font=f)
dw_btnsave = Button(dw,text="Save",font=f,width=8,height=1,command=delete)
dw_btnback = Button(dw,text="Back",font=f,command=f8,width=8,height=1,)
dw_labid.pack(pady=y)
dw_entid.pack(pady=y)
dw_btnsave.pack(pady=y)
dw_btnback.pack(pady=y) 
dw.withdraw()

cw = Toplevel(mw)
cw.title("Chart of Employees")
cw.geometry("1000x700+300+50")
cw.configure(bg="snow2")
cw_btnsave = Button(cw,text="Show Chart",font=f,width=10,height=1,command=bar)
cw_btnsave.pack(pady=y)
cw_btnback = Button(cw,text="Back",font=f,command=f10,width=8,height=1,)
cw_btnback.pack(pady=y) 
cw.withdraw()




mw.mainloop()




dw_btnsave.pack(pady=y)
dw_btnback.pack(pady=y) 
dw.withdraw()

cw = Toplevel(mw)
cw.title("Chart of Employees")
cw.geometry("1000x700+300+50")
cw.configure(bg="snow2")
cw_btnsave = Button(cw,text="Show Chart",font=f,width=10,height=1,command=bar)
cw_btnsave.pack(pady=y)
cw_btnback = Button(cw,text="Back",font=f,command=f10,width=8,height=1,)
cw_btnback.pack(pady=y) 
cw.withdraw()




mw.mainloop()



