import json
from django.shortcuts import render, get_object_or_404
from .models import Student
from django.http import JsonResponse
from django.core import serializers
from .forms import StudentForm
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.db.models.query import QuerySet
# Create your views here.

def indexjinja(request):

    test_stud = Student.objects.filter(pk = 1)

    students = get_object_or_404(Student, pk= 1)

    serialized_object = serializers.serialize('json', [students,])

    stud_json = {
        'id': students.id,
        'roll': students.roll,
        'name':students.name,
        'college': students.college,
        'date': students.date
    }

    print([stud_json])

    if isinstance(test_stud, QuerySet):
        print(list(test_stud.values()))
    else:
        print(students)
        # print(students.values())
    # student_list = list(students)


    students_json = {'success':True}

    return render(request, 'index.html', {'students':students_json})


def indexapi(request):
    return render(request,'index2.html')

@csrf_exempt
def addstudent(request):

    form = StudentForm
    
    if request.method == 'POST':
        received_json_data=json.loads(request.body)
        f = StudentForm(received_json_data)
        if f.is_valid():
            mysaved_model = f.save(commit=True)
            serialized_object = serializers.serialize('json', [mysaved_model,])
            context = {'sucess':True,'student': json.loads(serialized_object)}
            return JsonResponse(context)
        else:
            return JsonResponse({'success':False,'errors': json.loads(f.errors.as_json())})
    
    return render(request, 'add.html',{'form':form})

