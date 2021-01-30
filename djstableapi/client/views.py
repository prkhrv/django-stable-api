from django.shortcuts import render
from .models import Student

# Create your views here.

def indexjinja(request):

    students = Student.objects.all()

    return render(request, 'index.html', {'students':students})


def indexapi(request):
    return render(request,'index2.html')
