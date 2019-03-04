from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout

from datetime import date as ddate

from .models import Record
from .forms import RecordForm
from .utils import *

def homepage(request):
    return render(request,'journal/homepage.html')

def logoutpage(request):
    logout(request)
    return render(request,'registration/logout.html')

class JournalStartPage(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,"journal/journal_startpage.html")

class JournalTimeTable(LoginRequiredMixin,View):
    def get(self,request,month,day):
        return render(request,"journal/journal_timetable.html", context=get_journal_timetable_dictionary(month,day,request.user))

class JournalAddRecord(LoginRequiredMixin,View):
    def get(self,request,month,day):
        obj = Record(date=ddate(ddate.today().year,month,day),user=request.user)
        form = RecordForm(instance = obj)
        return render(request,'journal/journal_add_record.html',context={'form':form,'month':month,'day':day})
    def post(self,request,month,day):
        obj = Record(date=ddate(ddate.today().year,month,day),user=request.user)
        bound_form = RecordForm(request.POST,instance = obj)
        if bound_form.is_valid():
            bound_form.save()
            return render(request,'journal/journal_timetable.html',context = get_journal_timetable_dictionary(month,day,request.user))
        else:
            return render(request,'journal/journal_add_record.html',context={'form':bound_form,'month':month,'day':day})

class JournalUpdateRecord(LoginRequiredMixin,View):
    def get(self,request,month,day,slug):
        obj = Record.objects.get(slug__iexact = slug,user = request.user)
        form = RecordForm(instance = obj)
        return render(request,'journal/journal_update_record.html',context={'form':form,'month':month,'day':day,'slug':slug})
    def post(self,request,month,day,slug):
        obj = Record.objects.get(slug__iexact = slug,user = request.user)
        bound_form = RecordForm(request.POST,instance = obj)
        if bound_form.is_valid():
            bound_form.save()
            return render(request,'journal/journal_timetable.html',context = get_journal_timetable_dictionary(month,day,request.user))
        else:
            return render(request,'journal/journal_update_record.html',context={'form':bound_form,'month':month,'day':day,'slug':slug})

class JournalDeleteRecord(LoginRequiredMixin,View):
    def get(self,request,month,day,slug):
        return render(request,'journal/journal_delete_record.html',context={'month':month,'day':day,'slug':slug})
    def post(self,request,month,day,slug):
        obj = Record.objects.get(slug__iexact = slug,user = request.user)
        obj.delete()
        return render(request,'journal/journal_timetable.html',context = get_journal_timetable_dictionary(month,day,request.user))

class UserCreationView(View):
    def get(self,request):
        form = UserCreationForm()
        return render(request,'registration/register.html',context = {'form':form})
    def post(self,request):
        bound_form =UserCreationForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            username = bound_form.cleaned_data['username']
            password = bound_form.cleaned_data['password1']
            user = authenticate(request, username=username,password=password)
            login(request,user)
            return redirect('journal_startpage_url')
        else:
            return render(request,'registration/register.html',context ={'form':bound_form})
