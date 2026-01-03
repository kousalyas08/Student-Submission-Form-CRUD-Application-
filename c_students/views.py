from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# READ
def student_list(request):
    students = Student.objects.all()
    return render(request, 'c_students/list.html', {'students': students})

# CREATE
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'c_students/form.html', {'form': form})

# UPDATE
def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'c_students/form.html', {'form': form})

# DELETE
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')

#create a custom 404 error handler
from django.shortcuts import render

def page_not_found(request, exception):
    return render(request, 'c_students/404.html', status=404)

