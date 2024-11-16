from django.shortcuts import render, redirect, get_object_or_404
from .models import Test, Competitions, Submission
from django.http import JsonResponse , Http404
from django.utils import timezone
from .forms import TestForm, TaskFormSet, GradeForm
from users.models import StudentToTeacher
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.contrib.admin.views.decorators import staff_member_required
from .forms import SubmissionForm
from django.contrib.auth import authenticate, logout
def competitions(request):
    competitions = Competitions.objects.all()
    return render(request, 'competitions/competitions.html', {'competitions': competitions})

def get_active_competitions(request):
    now = timezone.now()
    competitions = Competitions.objects.filter(date__gte=now).values('id', 'title')
    return JsonResponse(list(competitions), safe=False)

@login_required
def create_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        formset = TaskFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            test = form.save(commit=False)
            test.author = request.user  # Убедитесь, что поле author существует в модели Test
            test.save()
            formset.instance = test
            formset.save()
            return redirect('test_detail', test_id=test.id)
        else:
            print(form.errors)
            print(formset.errors)
    else:
        form = TestForm()
        formset = TaskFormSet()

    return render(request, 'competitions/create_test.html', {'form': form, 'formset': formset})

def test_detail(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    return render(request, 'competitions/test_detail.html', {'test': test})

@login_required
def take_test(request, test_id):
    # Получение теста
    test = get_object_or_404(Test, id=test_id)
    # Получение всех заданий для данного теста
    tasks = test.tasks.all()

    # Если заданий нет, вернуть ошибку
    if not tasks:
        raise Http404("No tasks available for this test.")

    # Получение всех отправлений текущего пользователя по данному тесту
    user_submissions = Submission.objects.filter(user=request.user, test=test)
    # Создаем список ID заданий, на которые уже есть ответы
    completed_tasks_ids = user_submissions.values_list('task_id', flat=True)

    # Находим первое невыполненное задание
    next_task = None
    for task in tasks:
        if task.id not in completed_tasks_ids:
            next_task = task
            break

    # Если все задания выполнены, редирект на страницу успеха
    if next_task is None:
        return redirect('test_success')

    # Обработка формы отправки задания
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.user = request.user
            submission.test = test
            submission.task = next_task
            submission.save()
            return redirect('take_test', test_id=test.id)  # Переход к следующему заданию
    else:
        form = SubmissionForm()

    return render(request, 'competitions/take_test.html', {'test': test, 'task': next_task, 'form': form})

@login_required
def test_success(request):
    logout(request)
    return render(request, 'competitions/test_success.html')


@staff_member_required
def view_submissions(request):
    submissions = Submission.objects.all()
    return render(request, 'competitions/view_submissions.html', {'submissions': submissions})

@staff_member_required
def grade_submission(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    
    if request.method == 'POST':
        grade = request.POST.get('grade')
        submission.grade = grade
        submission.save()
        return redirect('view_submissions')
    
    return render(request, 'competitions/grade_submission.html', {'submission': submission})


@login_required
def view_grade_submissions(request, student_id):
    if not request.user.is_superuser:
        return redirect('home')

    submissions = Submission.objects.filter(user_id=student_id).select_related('task').all()

    # Обработка POST запроса
    if request.method == 'POST':
        submission_id = request.POST.get('submission_id')
        submission = get_object_or_404(Submission, pk=submission_id)
        form = GradeForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('view_grade_submissions', student_id=student_id)

    # Создание словаря форм для каждого submission
    forms = {submission.id: GradeForm(instance=submission) for submission in submissions}

    return render(request, 'competitions/view_grade_submissions.html', {
        'submissions': submissions,
        'forms': forms,
        'student_id': student_id
    })
@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('home')  # Перенаправляем не-админов на главную страницу

    # Получаем список участников
    students = StudentToTeacher.objects.select_related('id', 'competition_id').all()

    return render(request, 'competitions/admin_dashboard.html', {'students': students})