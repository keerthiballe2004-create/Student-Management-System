from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.db.models import Q
from django.core.paginator import Paginator
from django.db.models import Count

# Add Student
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('view_students')
    else:
        form = StudentForm()

    return render(request, 'students/add_student.html', {
        'form': form
    })


# View Students

# View Students
def view_students(request):
    query = request.GET.get('search', '')

    students = Student.objects.all()

    if query:
        students = students.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(course__icontains=query)
        )
    course_counts = list(
         Student.objects.values('course')
         .annotate(total=Count('id'))
         .order_by('course')
    )   

    # Total student count
    total_students = Student.objects.count()

    # Course-wise student count
    course_counts = Student.objects.values(
        'course'
    ).annotate(
        total=Count('id')
    ).order_by('course')

    # Total number of different courses
    total_courses = course_counts.count()

    # Pagination
    paginator = Paginator(students, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'students/view_students.html', {
        'students': page_obj,
        'page_obj': page_obj,
        'query': query,
        'total_students': total_students,
        'course_counts': course_counts,
        'total_courses': total_courses
    })

# Student Records Page
def student_records(request):
    query = request.GET.get('search', '')

    students = Student.objects.all()

    if query:
        students = students.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(course__icontains=query)
        )

    paginator = Paginator(students, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'students/student_records.html', {
        'students': page_obj,
        'page_obj': page_obj,
        'query': query
    })



# Edit Student
def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        form = StudentForm(
            request.POST,
            request.FILES,
            instance=student
        )

        if form.is_valid():
            form.save()
            return redirect('view_students')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/edit_student.html', {
        'form': form,
        'student': student
    })


# Delete Student
def delete_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('view_students')

    return render(request, 'students/delete_student.html', {
        'student': student
    })