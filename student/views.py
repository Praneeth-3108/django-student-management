from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def student_list(request):
    # Handle adding a new student from the homepage form
    if request.method == 'POST':
        roll_no = request.POST.get('roll_no')
        name = request.POST.get('name')
        branch = request.POST.get('branch')
        if roll_no and name and branch:
            Student.objects.create(roll_no=roll_no, name=name, branch=branch)
        return redirect('home')

    # Handle searching students
    query = request.GET.get('q', '')
    if query:
        students = (
            Student.objects.filter(name__icontains=query) |
            Student.objects.filter(roll_no__icontains=query) |
            Student.objects.filter(branch__icontains=query)
        )
    else:
        students = Student.objects.all()

    return render(request, 'index.html', {'students': students, 'query': query})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('home')