from django.urls import path
from .views import *

urlpatterns = [
    path('',JournalStartPage.as_view(),name ='journal_startpage_url'),
    path('<int:month>/<int:day>/',JournalTimeTable.as_view(),name = 'journal_timetable_url'),
    path("<int:month>/<int:day>/journal_add_record/",JournalAddRecord.as_view(),name='journal_add_record_url'),
    path("<int:month>/<int:day>/<str:slug>/journal_update_record/",JournalUpdateRecord.as_view(),name='journal_update_record_url'),
    path("<int:month>/<int:day>/<str:slug>/journal_delete_record/",JournalDeleteRecord.as_view(),name='journal_delete_record_url'),
]
