from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserAuthForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.urls import reverse

# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = UserAuthForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', 'digitalportfolio:home')
            return redirect(next_url)
        else:
            return render(request, 'autenticacao/login.html', {'form': form})
    else:
        form = UserAuthForm()
        return render(request, 'autenticacao/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('https://a21807126.pythonanywhere.com')

def registo_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password']
            )
            user = authenticate(username=user.username, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('portfolio:home')
    else:
        form = UserRegistrationForm()

    return render(request, 'autenticacao/registo.html', {'form': form})

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email:
            return render(request, 'autenticacao/redefenir_senha.html', {'error': 'Por favor, insira o seu email.'})

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'autenticacao/redefenir_senha.html', {'error': 'O email inserido não está registado'})

        token = default_token_generator.make_token(user)
        uidb64 = urlsafe_base64_encode(user.pk.to_bytes(4, 'big'))

        reset_link = request.build_absolute_uri(f'/reset/{uidb64}/{token}/')

        send_mail('Definição de palavra chave',
                  f'Olá\n\nPediu para redefinir a sua palavra chave, clique por favor no seguinte link:\n\n{reset_link}',
                  'tome.games09@gmail.com',
                  [email],
                  )

        return render(request, 'autenticacao/redefenir_senha.html', {'success': 'Foi-lhe enviado um email com o link para redefinir a sua senha'})
    else:
        return render(request, 'autenticacao/redefenir_senha.html')

