from django import forms
from django.forms.models import inlineformset_factory

from .models import Test, Task, Submission, Competitions  # Убедитесь, что импортирована модель Competition

class TestForm(forms.ModelForm):
    due_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Test
        fields = ['title', 'description', 'competition', 'due_date']

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        # Получение списка ID соревнований, для которых уже есть тесты
        existing_competitions_ids = Test.objects.values_list('competition_id', flat=True)
        self.fields['competition'].queryset = Competitions.objects.exclude(id__in=existing_competitions_ids)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'image']


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['file']


class GradeForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['grade']

TaskFormSet = inlineformset_factory(Test, Task, form=TaskForm, extra=1, can_delete=True)
