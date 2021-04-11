from django.shortcuts import render
from django.http import HttpResponse

from polls.getList import DB_Provider


def index(request):
    list  = DB_Provider().getUnsortedList()
    return HttpResponse(list)


