import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from news.models import Article
from competitions.models import Competitions
from users.models import AbstractUser, StudentToTeacher
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.utils import timezone
import random
import string
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
import string
from users.models import StudentToTeacher
def index(request):
    username = request.user.username
    articles = Article.objects.all()
    #    competitions = Competitions.objects.filter(date__gte=now()).order_by('date') #Выводит текущие (актульные соревнования), отключено для тестов!
    competitions = Competitions.objects.filter(places__gt=0)
    context = {'articles': articles, 'competitions': competitions, 'username': username}
    if request.user.is_authenticated:
        return render(request, 'main/index.html', {'user': request.user , 'is_authenticated':request.user.is_authenticated } | context)
    return render(request, 'main/index.html', context)

@csrf_exempt
def register_participant(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        competition_id = data.get('competition_id')
        students = data.get('students')

        if not competition_id or not students:
            return JsonResponse({'error': 'Invalid data'}, status=400)

        competition = get_object_or_404(Competitions, id=competition_id)
        
        if competition.places < len(students):
            return JsonResponse({'error': 'Not enough places available'}, status=400)

        User = get_user_model()
        registered_students = []

        for student in students:
            student_name = student.get('name')
            student_email = student.get('email')

            if not student_name or not student_email:
                return JsonResponse({'error': 'Student name and email are required'}, status=400)

            username = student_name.replace(' ', '_').replace('.', '').replace(',', '_')
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

            user = User.objects.create_user(username=username, email=student_email, password=password)
            user.first_name = student_name
            user.save()

            StudentToTeacher.objects.create(id=user, teacher_id=request.user, password=password, competition_id=competition)

            registered_students.append({'username': username, 'email': student_email})

        competition.reduce_places(len(students))

        return JsonResponse({'message': 'Participants successfully registered!', 'students': registered_students})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def teacher_students(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required'}, status=403)

    students = StudentToTeacher.objects.filter(teacher_id=request.user.id)
    print(students)
    return render(request, 'teacher_students.html', {'students': students})            

def about(request):
    return render(request, 'main/about.html')

def admin_panel(request):
    return render(request, 'main/admin_panel.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                try:
                    # Пытаемся найти объект StudentToTeacher для текущего пользователя
                    student_to_teacher = StudentToTeacher.objects.get(id=request.user)
                    competition_id = student_to_teacher.competition_id.id  # Получаем competition_id
                    # Формируем URL для редиректа, заменяя test_id на competition_id
                    redirect_url = f'/competitions/competitions/1/take_test/'
                    return redirect(redirect_url)
                except StudentToTeacher.DoesNotExist:
                    return redirect('/accounts/profile') 
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Перенаправление на главную страницу после выхода

@login_required
def profile_view(request):
    username = request.user.username
    students = StudentToTeacher.objects.filter(teacher_id=request.user.id)

    return render(request, "main/profile.html", {'username': username , 'students': students})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'auth/registration.html', {'form': form})
