from django.shortcuts import render
from .models import Students
from django.http import HttpResponseRedirect
from .forms import StudentForm

# Create your views here.


def index(request): return render(request, 'students/index.html',
                                  {'students': Students.objects.all()})


def student_details(request, student_id):
    student = Students.objects.get(pk=student_id)
    return render(request, 'students/studenDetail.html', {'student': student})


def student_delete(request, student_id):
    student = Students.objects.get(pk=student_id)
    student.delete()
    return render(request, 'students/index.html', {'students': Students.objects.all()})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'students/index.html', {'students': Students.objects.all()})
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {'form': form})


def edit_student(request, student_id):
    student = Students.objects.get(pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/index.html', {'students': Students.objects.all()})
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})
