from django.shortcuts import render, HttpResponse, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import Student


# Create your views here.

def home(request):
    return render(request, 'home.html')


def log_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    if request.method == 'POST':
        form = LoginForm(request.POST, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pword = form.cleaned_data['password']
            user = authenticate(username=uname, password=pword)
            if user is not None:
                login(request, user)

            return redirect('course_list')
        return redirect('home')


def course_list(request):
    if request.method == 'GET':
        data = Student.objects.get(user=request.user.id)
        print(data.course)
        return render(request, 'course_list.html', {'data': data})
