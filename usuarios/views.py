from django.shortcuts import redirect, render

def cadastro(request):
    if request.method == 'POST':
        print('cadastro efetuado')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    return render(request, 'usuarios/login.html')

def dashboard(request):
    pass

def logout(request):
    pass
