# --- users/views.py ---
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm, LoginForm, AdminLoginForm

def index(request): 
    return render(request, 'index.html')

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kayıt başarılı! Giriş yapabilirsiniz.')
            return redirect('login_user')
        else:
            messages.error(request, 'Kayıt başarısız. Lütfen bilgilerinizi kontrol edin.')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and not user.is_library_admin:
                login(request, user)
                return redirect('books:list_books')  # Replace with the appropriate redirect URL
            else:
                messages.error(request, 'Hatalı kullanıcı adı veya şifre.')
        else:
            messages.error(request, 'Lütfen geçerli bir form doldurun.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def login_library_admin(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_library_admin:
                login(request, user)
                return redirect('admin_dashboard')  # Replace with the appropriate redirect URL
            else:
                messages.error(request, 'Hatalı kullanıcı adı veya şifre.')
        else:
            messages.error(request, 'Lütfen geçerli bir form doldurun.')
    else:
        form = AdminLoginForm()
    return render(request, 'admin_login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, 'Başarıyla çıkış yaptınız.')
    return redirect('login_user')  # Redirect to the login page after logout