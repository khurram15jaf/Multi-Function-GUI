class MyClass():#Class
	
	def DaysInWeek(day):#Week display function
		for e,d in enumerate(day):#Index+Array For loop
			print(e+1,d)
	
	
	def TodayNow(self):#Today Function
		from datetime import date,datetime#Library for Date
		
		tody=date.today()#date today
		tday=datetime.date(datetime.now())#date now only
		tim=datetime.time(datetime.now())#time now
		print("Today: ",tody,tday.strftime("%a,%d %B'%y"),tim)#prints variables
	
			
	def TodayDelta(self):#Today Function
		from datetime import datetime#Library for DateTime
		from datetime import timedelta#Library for Time Change
		
		tod=datetime.now()#date today
		y=input("Enter added years:")
		m=input("Enter added months:")
		d=input("Enter added days:")
		h=input("Enter added hours:")
		mi=input("Enter added minutes:")
		d=int(d)+int(m)*30+int(y)*365
		h=int(h);mi=int(mi)
		a1y=timedelta(days=d,hours=h,minutes=mi)#time delta
		print("After 1 year, 1 months and 2 hours: ",str(tod+a1y))#prints variables
	
			
	def DaysLeft(self):#Days Left Function
		from datetime import date#Library for Date and time
		
		now=date.today()#date today
		y=input("Enter year:")
		m=input("Enter month:")
		d=input("Enter day:")
		y=int(y);m=int(m);d=int(d)
		jand=date(y,m,d)#time delta
		if now>jand:
			print(jand.strftime("%a-%d %B'%y"),"has passed by",(now-jand))
		elif now<jand:
			print(jand.strftime("%a-%d %B'%y"),"is coming on",(jand-now))
		else:
			print("Today is",jand.strftime("%a-%d %B'%y"))
	
					
	def calder(self):#
		import calendar
		
		c=calendar.TextCalendar(calendar.SUNDAY)#initializing Text based Calendar
		st=c.formatmonth(2020,2,0)#formating calendar
		print(st)#prints calendar
	
					
	def hcalder(self):#
		import calendar
		
		hc=calendar.HTMLCalendar(calendar.SUNDAY)#initializing HTML based Calendar
		st=hc.formatmonth(2020,1,0)#formating calendar
		print(st)#prints calendar	


class MyClass1():#Class

	def DaysNMonth(self):#Days and Months display function
		import calendar
		
		for dys in calendar.day_name:
			print(dys)
		for mom in calendar.month_name:
			print(mom)
#print('Hi')


	def Friday1st(self):#First Friday of every month display function
		import calendar
		
		for m in range(1,13):
			cal=calendar.monthcalendar(2020,m)
			weekone=cal[0]
			weektwo=cal[1]
			if weekone[calendar.FRIDAY]!=0:
				meetday=weekone[calendar.FRIDAY]
			else:
				meetday=weektwo[calendar.FRIDAY]
			print("%10s %2d" %(calendar.month_name[m],meetday))

						
	def opnl(self):#First Friday of every month display function
		f=open("textfile.txt","a")
		m=input("Enter text: ")
		f.write(m)
		f.write("\n")
		f.close()

		
	def redl(self):
		x=open("textfile.txt","r")
#		if x.mode()=="r":
		fl=x.read()
		print(fl)
		fl.close()
		
	
	def chkl(self):#First Friday of every month display function		
		import os
		from os import path
		import datetime
		from datetime import date,time,timedelta
		import time
		
		print(os.name)
		print("Item Exists:" +str(path.exists("textfile.txt")))
		print("Item Exists:" +str(path.isfile("textfile.txt")))
		print("Item Exists:" +str(path.isdir("textfile.txt")))
		print("Path Location:" +str(path.realpath("textfile.txt")))
		print("Path Location:" +str(path.split(path.realpath("textfile.txt"))))
		t=time.ctime(path.getmtime("textfile.txt"))
		print("Modified: ",t)
		print("Modified: ",datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))
		td=datetime.datetime.now()-datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
		print("Days since Modified: ",td.total_seconds())
		
		
	def rezp(self):#First Friday of every month display function
		import os
		from os import path
		import shutil
		from shutil import make_archive
		from zipfile import ZipFile
		
		if path.exists("textfile.txt"):
			src=path.realpath("textfile.txt")
			dst=src+".bak"
			shutil.copy(src,dst)
			shutil.copystat(src,dst)
			os.rename("textfile.txt.bak","newfile.txt")
			root_dir,tail=path.split(src)
			shutil.make_archive("archive","zip",root_dir)
			with ZipFile("testzip.zip","w") as newzip:
				newzip.write("textfile.txt")
				newzip.write("newfile.txt")	
				
				
				
class MyClass2():#Class
		
	def weburl(self):#First Friday of every month display function
		import urllib.request
		
		webUr=urllib.request.urlopen("http://:www.google.com")
		print("URL code: "+ str(webUr.getcode()))
		data=webUr.read()
		print(data)

def input_string():
    while True:
        value = input("Enter Option: \n")
        try:
            value = int(value)
            break
        except ValueError:
            print("I said enter an integer")
    return value    
	
					
def main():
	import calendar
	
	error="N"
	opt=["Weekdays","Today","Delta","Days Left","Text Calendar","HTML Calendar","Days and months","Friday","Open File","Read File","Check File","Rename and ZIP","Web"]#array	
	for z,y in enumerate(opt):
		print(z+1,":",y)
	
#	days
#	for mn,ds in enumerate(calendar.day_name):
#			days[mn]=ds
	
	cd=MyClass()#declaring class
	dc=MyClass1()#declaring class
	dcd=MyClass2()#declarin g class
			
	while ((error=="N")):#While Condition
		k=input_string()#input always in INTEGER
		#if (k==opt[0]):#If Input is 'Weekdays'
		if (k==1):#If Input is 'Weekdays'
			cd.TodayNow()#call method TodayNow(self)
#            cd.DaysInWeek(days)#call method DaysInWeek(argment)"
		#elif (k==opt[1]):#else if input is 'Today'
		elif (k==2):#else if input is 'Today'
			cd.TodayNow()#call method TodayNow(self)
			
		#elif (k==opt[2]):#else if input is 'Delta'
		elif (k==3):#else if input is 'Delta'
			cd.TodayDelta()#call method TodayDelta(self)
			
		#elif (k==opt[3]):#else if input is 'Days Left'
		elif (k==4):#else if input is 'Days Left'
			cd.DaysLeft()#call method DaysLeft(self)
			
		#elif (k==opt[4]):#else if input is 'Calendar')			
		elif (k==5):#else if input is 'Calendar'
			cd.calder()#call method calder(self)
			
		#elif (k==opt[5]):#else if input is 'HTMLCalendar'
		elif (k==6):#else if input is 'HTMLCalendar'			
			cd.hcalder()#call method hcalder(self)
			
		#elif (k==opt[6]):#else if input is 'Days and Month'	
		elif (k==7):#else if input is 'Days and Month'	
			dc.DaysNMonth()#call method hcalder(self)
			
		#elif (k==opt[7]):#else if input is '1st Friday'
		elif (k==8):#else if input is '1st Friday'
			dc.Friday1st()#call method Friday1st(self)
			
		#elif (k==opt[8]):#else if input is 'Open Fild'
		elif (k==9):#else if input is 'Open Fild'
			dc.opnl()#call method opnl(self)
			
		#elif (k==opt[9]):#else if input is 'Read File'
		elif (k==10):#else if input is 'Read File'
			dc.redl()#call method redl(self)
			
		#elif (k==opt[10]):#else if input is 'Check File'
		elif (k==11):#else if input is 'Check File'
			dc.chkl()#call method chkl(self)
			
		#elif (k==opt[11]):#else if input is 'Rename and Zip'
		elif (k==12):#else if input is 'Rename and Zip'
			dc.rezp()#call method rezp(self)
			
		#elif (k==opt[12]):#else if input is 'Rename and ZIP'
		elif (k==13):#else if input is 'Rename and ZIP'
			dcd.weburl()#call method Friday1st(self)
#		elif (k==opt[13]):#else if input is 'Rename and ZIP'
#		elif (k==14):#else if input is 'Rename and ZIP'
#			dc.redl()#call method Friday1st(self)
		else:#if none of the above
			print("Error")#prints error message
		error=input("Done?(Y/N) ")#input
#		print.cls
		
			
if __name__ == "__main__":#initialize main
	main()#calls main()
