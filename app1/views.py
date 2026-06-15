from django.shortcuts import render
from django.http import HttpResponse

from app1.models import Student

def home(request):
    return render(request, 'index.html')

def save_student(request):
    if request.method == 'POST':
        name = request.POST.get('stud_name')
        email = request.POST.get('email')
        course = request.POST.get('course')

        student = Student(stud_name=name, email=email, course=course)
        student.save()

        return HttpResponse("Student registered successfully!")

    return render(request, 'student_form.html')

def student_form(request):
    return render(request, 'student_form.html')      

def student_list(request):
    students = Student.objects.all().order_by('stud_name')
    return render(request, 'student_list.html', {'students': students})

#return JsonResponse({'students': students_data})


from django.shortcuts import render, redirect, get_object_or_404

# VIEW STUDENT
def view_student(request, id):
    student = get_object_or_404(Student, stud_id=id)
    return render(request, 'view_student.html', {'student': student})


# EDIT / UPDATE STUDENT
def edit_student(request, id):
    student = get_object_or_404(Student, stud_id=id)

    if request.method == 'POST':
        student.stud_name = request.POST.get('stud_name')
        student.email = request.POST.get('email')
        student.course = request.POST.get('course')
        student.save()
        return redirect('student_list')

    return render(request, 'edit_student.html', {'student': student})


# DELETE STUDENT
def delete_student(request, id):
    student = get_object_or_404(Student, stud_id=id)
    student.delete()
    return redirect('student_list')