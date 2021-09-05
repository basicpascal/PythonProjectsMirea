import datetime
from datetime import datetime,timedelta,date
import calendar
import re
def weeks():
        date = datetime.today()
        date = date.isocalendar()
        m=[]
        for i in date:
                m.append(i)
        m[2]=1
        a=int(m[0])
        b=int(m[1])
        c=int(m[2])
        date = datetime.today()
        dt4 = date.fromisocalendar(a,b,c)
        dt5 = dt4+timedelta(weeks=1,days=-1)
        dt3 = dt4-timedelta(weeks=1)
        dt2 = dt3-timedelta(weeks=1)
        dt = dt2-timedelta(weeks=1)
        mass=[]
        a=str(dt4.strftime("%d.%m.%Y"))+"-"+str(dt5.strftime("%d.%m.%Y"))
        dt4=dt4-timedelta(days=1)
        b=str(dt3.strftime("%d.%m.%Y"))+"-"+str(dt4.strftime("%d.%m.%Y"))
        dt3=dt3-timedelta(days=1)
        c=str(dt2.strftime("%d.%m.%Y"))+"-"+str(dt3.strftime("%d.%m.%Y"))
        dt2=dt2-timedelta(days=1)
        d=str(dt.strftime("%d.%m.%Y"))+"-"+str(dt2.strftime("%d.%m.%Y"))
        mass.append(a)
        mass.append(b)
        mass.append(c)
        mass.append(d)
        return(mass)
def months():
        from datetime import date, timedelta
        from calendar import monthrange
        mass=[]
        days_in_month = lambda dt: monthrange(dt.year, dt.month)[1]
        start = date.today()
        start=start.replace(day=1)
        end = date.today()
        end = end.replace(day=1) + timedelta(days_in_month(end))-timedelta(days=1)
        a=str(start.strftime("%d.%m.%Y"))+"-"+str(end.strftime("%d.%m.%Y"))
        
        end2=start-timedelta(days=1)
        start2=end2.replace(day=1)
        b=str(start2.strftime("%d.%m.%Y"))+"-"+str(end2.strftime("%d.%m.%Y"))
        
        end3=start2-timedelta(days=1)
        start3=end3.replace(day=1)
        c=str(start3.strftime("%d.%m.%Y"))+"-"+str(end3.strftime("%d.%m.%Y"))
        
        end4=start3-timedelta(days=1)
        start4=end4.replace(day=1)
        d=str(start4.strftime("%d.%m.%Y"))+"-"+str(end4.strftime("%d.%m.%Y"))
        mass.append(a)
        mass.append(b)
        mass.append(c)
        mass.append(d)
        return(mass)
        #l =a.find('-')
        #print (a[:l])
def cvarts():
        startq = date.today()
        q = startq.month
        year = startq.year
        mass=[]
        if (q == 1) or (q == 2) or (q == 3):
            startq=startq.replace(month=1,day=1)
            endq=startq.replace(month=4)-timedelta(days=1)
            mass.append(startq.strftime("%d.%m.%Y")+"-"+endq.strftime("%d.%m.%Y"))
        if (q == 4) or (q == 5) or (q == 6):
            startq=startq.replace(month=4,day=1)
            endq=startq.replace(month=7)-timedelta(days=1)
            mass.append(startq.strftime("%d.%m.%Y")+"-"+endq.strftime("%d.%m.%Y"))
        if (q == 7) or (q == 8) or (q == 9):
            startq=startq.replace(month=7,day=1)
            endq=startq.replace(month=10)-timedelta(days=1)
            mass.append(startq.strftime("%d.%m.%Y")+"-"+endq.strftime("%d.%m.%Y"))
        if (q == 10) or (q == 11) or (q == 12):
            startq=startq.replace(month=10,day=1)
            endq=startq.replace(year=year+1,month=1)-timedelta(days=1)
            mass.append(startq.strftime("%d.%m.%Y")+"-"+endq.strftime("%d.%m.%Y"))
        for i in range(0,3):
            if startq.month-1 == 0 :
                endq=startq-timedelta(days=1)
                startq=endq.replace(day=1,month=10)
            else:
                endq=startq-timedelta(days=1)
            q=endq.month
            if (q == 1) or (q == 2) or (q == 3):
                startq=startq.replace(month=1,day=1)
                endq=startq.replace(month=4)-timedelta(days=1)
                mass.append(startq.strftime("%d.%m.%Y")+"-"+endq.strftime("%d.%m.%Y"))
            if (q == 4) or (q == 5) or (q == 6):
                startq=startq.replace(month=4,day=1)
                endq=startq.replace(month=7)-timedelta(days=1)
                mass.append(startq.strftime("%d.%m.%Y")+"-"+endq.strftime("%d.%m.%Y"))
            if (q == 7) or (q == 8) or (q == 9):
                startq=startq.replace(month=7,day=1)
                endq=startq.replace(month=10)-timedelta(days=1)
                mass.append(startq.strftime("%d.%m.%Y")+"-"+endq.strftime("%d.%m.%Y"))
            if (q == 10) or (q == 11) or (q == 12):
                startq=startq.replace(month=10,day=1)
                endq=startq.replace(year=year,month=1)-timedelta(days=1)
                mass.append(startq.strftime("%d.%m.%Y")+"-"+endq.strftime("%d.%m.%Y"))
        return (mass)
def years():
        mass=[]
        years1=date.today()
        year=years1.year
        years1=years1.replace(day=1,month=1)
        yeare1=years1.replace(year=year+1)-timedelta(days=1)
        a=(years1.strftime("%d.%m.%Y")+"-"+yeare1.strftime("%d.%m.%Y"))
        mass.append(a)
        years1=years1.replace(year=year-1)
        yeare1=yeare1.replace(year=year-1)
        year=year-1
        a=(years1.strftime("%d.%m.%Y")+"-"+yeare1.strftime("%d.%m.%Y"))
        mass.append(a)
        years1=years1.replace(year=year-1)
        yeare1=yeare1.replace(year=year-1)
        year=year-1
        a=(years1.strftime("%d.%m.%Y")+"-"+yeare1.strftime("%d.%m.%Y"))
        mass.append(a)
        years1=years1.replace(year=year-1)
        yeare1=yeare1.replace(year=year-1)
        a=(years1.strftime("%d.%m.%Y")+"-"+yeare1.strftime("%d.%m.%Y"))
        mass.append(a)
        return(mass)


