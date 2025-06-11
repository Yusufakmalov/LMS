from django.shortcuts import render, redirect

from .models import AcademicYear, Kafedra, LessonTime
from .forms import AcademicYearForm, KafedraForm, LessonTimeForm

def academic_year(request):
    academic_years = AcademicYear.objects.all()
    return render(request, 'structure/academic-year.html', {'academic_years': academic_years})

def academic_year_delete(request, pk):
    academic_year = AcademicYear.objects.get(pk=pk)
    academic_year.delete()
    return redirect('structure:academic_year')


def academic_year_detail(request, pk):
    academic_year = AcademicYear.objects.get(pk=pk)
    return render(request, 'structure/academic_year_detail.html', {'academic_year': academic_year})


def academic_year_update(request, pk):
    academic_year = AcademicYear.objects.get(pk=pk)
    if request.method == 'POST':
        form = AcademicYearForm(request.POST, instance=academic_year)
        if form.is_valid():
            form.save()
            return redirect('structure:academic_year')
    else:
        form = AcademicYearForm(instance=academic_year)
    return render(request, 'structure/academic-year-update.html', {'form': form})


def academic_year_create(request):
    if request.method == 'POST':
        form = AcademicYearForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('structure:academic_year')
    
    else:
        form = AcademicYearForm()
        return render(request, 'structure/academic-year-update.html', {'form': form})
        

def kafedra_list(request):
    kafedra = Kafedra.objects.all()
    return render(request, 'structure/kafedra.html', {'kafedra': kafedra})


def kafedra_detail(request, pk):
    kafedra = Kafedra.objects.get(pk=pk)
    return render(request, 'structure/kafedra-detail.html', {'kafedra': kafedra})


def kafedra_delete(request, pk):
    kafedra = Kafedra.objects.get(pk=pk)
    kafedra.delete()
    return redirect('structure:kafedra_list')

def kafedra_update(request, pk):
    kafedra = Kafedra.objects.get(pk=pk)
    if request.method == 'POST':
        form = KafedraForm(request.POST, instance=kafedra, request=request)
        if form.is_valid():
            form.save()
            return redirect('structure:kafedra_list')
    else:
        form = KafedraForm(instance=kafedra, request=request)
    return render(request, 'structure/kafedra-update.html', {'form': form})

def kafedra_create(request):
    if request.method == 'POST':
        form = KafedraForm(request.POST, request=request)
        if form.is_valid():
            kafedra = form.save(commit=False)
            kafedra.school = request.user.school
            kafedra.save()
            return redirect('structure:kafedra_list')
    else:
        form = KafedraForm(request=request)
    return render(request, 'structure/kafedra-update.html', {'form': form})


def lesson_time_list(request):
    lesson_time = LessonTime.objects.all()
    return render(request, 'structure/lesson_time.html', {'lesson_time': lesson_time})


def lesson_time_detail(request, pk):
    lesson_time = LessonTime.objects.get(pk=pk)
    return render(request, 'structure/lesson-time-detail.html', {'lesson_time': lesson_time})


def lesson_time_delete(request, pk):
    lesson_time = LessonTime.objects.get(pk=pk)
    lesson_time.delete()
    return redirect('structure:lesson_time_list')

def lesson_time_update(request, pk):
    lesson_time = LessonTime.objects.get(pk=pk)
    if request.method == 'POST':
        form = LessonTimeForm(request.POST, instance=lesson_time)
        if form.is_valid():
            form.save()
            return redirect('structure:lesson_time_list')
    else:
        form = LessonTimeForm(instance=lesson_time)
    return render(request, 'structure/lesson-time-update.html', {'form': form})

def lesson_time_create(request):
    if request.method == 'POST':
        form = LessonTimeForm(request.POST)
        if form.is_valid():
            lesson_time = form.save(commit=False)
            lesson_time.school = request.user.school
            lesson_time.save()
            return redirect('structure:lesson_time_list')
    else:
        form = LessonTimeForm()
    return render(request, 'structure/lesson-time-update.html', {'form': form})