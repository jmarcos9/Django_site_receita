from django.shortcuts import redirect, render
from django.contrib.auth.models import User

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        print()
        
        if not nome.strip():
            print('erro nome')
            return redirect('cadastro')
        
        if not email.strip():            
            return redirect('cadastro')
        
        if password != password2:
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
    return render(request, 'usuarios/login.html')

def dashboard(request):
    pass

def logout(request):
    pass
