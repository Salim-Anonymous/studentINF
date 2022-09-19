from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import StudentForm
from .models import Student, Search


# Create your views here.

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'SIS/index.html')
    else:
        form = StudentForm()

    return render(request, 'SIS/addStudent.html', {'form': form})


def remove_student(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return render(request, 'SIS/index.html')


# def edit_student(request, pk):
#     student = Student.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = StudentForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#         return render(request, 'SIS/index.html')
#     else:
#         form = StudentForm(instance=student)
#
#     return render(request, 'SIS/editStudent.html', {'form': form})

def index(request):
    students = Student.objects.all()
    return render(request, 'SIS/index.html', {'students': students})


def search_student(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'SIS/search.html', {'student': student})


class HomepageView(ListView):
    model = Student
    template_name = 'SIS/index.html'


class SearchResultView(ListView):
    model = Student
    template_name = 'SIS/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Student.objects.filter(studentID__icontains=query)
        return object_list
