from django.shortcuts import render, redirect

from .models import AcademicYear, Kafedra
from .forms import AcademicYearForm, KafedraForm

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


    