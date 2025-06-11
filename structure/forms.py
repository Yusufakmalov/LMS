from django import forms
from .models import AcademicYear, Kafedra, LessonTime
from django.db.models import Q
from account.models import CustomUser


class AcademicYearForm(forms.ModelForm):

    class Meta:
        model = AcademicYear
        fields = ['name', 'season', 'start_date', 'end_date', 'is_active', 'parent']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, instance=None, **kwargs):
        super().__init__(*args, **kwargs)
        if instance:
            self.fields['parent'].queryset = AcademicYear.objects.exclude(Q(pk=instance.pk) | Q(parent=instance))
      
class KafedraForm(forms.ModelForm):

    class Meta:
        model = Kafedra
        fields = ['name', 'code', 'is_active', 'department_user']
       

    def __init__(self, *args, instance=None, request=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        if instance and self.request:
            self.fields['department_user'].queryset = CustomUser.objects.exclude(
                Q(is_worker=False) |
                Q(role__name__in=['dirrector', 'student', 'stylist', 'accountant', 'tutor']) |
                ~Q(school=self.request.user.school)
            )

class LessonTimeForm(forms.ModelForm):

    class Meta:
        model = LessonTime
        fields = ['name', 'start_time', 'end_time', 'is_active']
       