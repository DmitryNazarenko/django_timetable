from .models import Record

from calendar import Calendar
from datetime import date

def make_month(dayslist):
    res =[]
    for i in range(0,6):
        week = dayslist[:7]
        dayslist = dayslist[7:]
        res+=[week]
    return res

def get_journal_timetable_dictionary(month,day,user):
    _weekday = 0
    _year = date.today().year

    record_db = Record.objects.filter(date=date(_year,month,day),user=user)

    cal = Calendar(_weekday)
    dayslist = [day for day in cal.itermonthdays(_year,month)]

    return {'year':_year,'month':month,'day':day,'daysinmonth':make_month(dayslist),'record_db':record_db}
