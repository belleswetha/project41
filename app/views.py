from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.views.generic import ListView


class SchoolList(ListView):
    model=School
    context_object_name='Schools'
    ordering=['sname']
    #template_name='app/school_list.html'
    #queryset=School.objects.filter(id=1)


    