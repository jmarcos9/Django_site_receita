from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        print()
        
        if not nome.strip():
            print('erro nome')
            return redirect('cadastro')
        
        if not email.strip():            
            return redirect('cadastro')
        
        if senha != senha2:
            print('erro senha')
            return redirect('cadastro')
        
        if User.objects.filter(email=email).exists():
            print('user ja cadastrado')
            return redirect('cadastro')        
        user =  User.objects.create_user(username=nome, email=email, password=password)
        user.save
        
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            print('email e senha não podem ficar em branco')
            return redirect('login')
        print(email, senha)        
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)            
            if user is not None:
                auth.login(request, user)                          
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def dashboard(request):
    return render(request, 'usuarios/dashboard.html')

def logout(request):
    pass


