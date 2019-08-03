from django.shortcuts import render
from django.http import HttpResponse

def student(request):
    return HttpResponse('<h1>This is my page</h1>')
def stud(request):
    return render(request,'student.html')
