from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from portfolio.forms import CadeiraForm, PostForm
from django.contrib.auth.decorators import login_required
from .models import *


def home_view(request):
    return render(request, 'portfolio/home.html')


def projects_view(request):
    context = {'projetos': Projeto.objects.all(), 'tfcs': Tfc.objects.all()}
    return render(request, 'portfolio/projects.html',context)


def technologys_view(request):
    context = {'techs': Tecnologia.objects.all()}
    return render(request, 'portfolio/technologys.html',context)


def labs_view(request):
    context = {'labs': Laboratorio.objects.all()}
    return render(request, 'portfolio/labs.html',context)

def usedtech_view(request):
    return render(request, 'portfolio/usedtech.html')


def javascript_view(request):
    return render(request, 'portfolio/javascript.html')


def university_view(request):
    context = {'cadeiras': Cadeira.objects.all()}
    return render(request, 'portfolio/university.html',context)


def education_view(request):
    return render(request, 'portfolio/education.html')


def skills_view(request):
    return render(request, 'portfolio/skills.html')


def hobbies_view(request):
    context = {'hobbies' : Interesse.objects.all()}
    return render(request, 'portfolio/hobbies.html',context)


def aboutme_view(request):
    return render(request, 'portfolio/aboutme.html')


def blog_view(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'portfolio/blog.html', context)


def contact_view(request):
    return render(request, 'portfolio/contact.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,
                           username=username,
                           password=password)
        
        if user is not None:
            login(request, user)
            return redirect('portfolio:home')
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas',
            })
    return render(request, 'portfolio/login.html')


def logout_view(request):
    logout(request)
    return redirect('portfolio:home')


@login_required
def criar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio:blog')  # Redirecione para uma página de sucesso após a criação do post
    else:
        form = PostForm()
        pessoas = Pessoa.objects.all()
    return render(request, 'portfolio/criar.html', {'form': form, 'autor':pessoas})

@login_required
def edita_comentario(request, comentario_id):
    comentario = Post.objects.get(id=comentario_id)
    form = PostForm(request.POST or None, instance=comentario)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'comentario_id': comentario_id}
    return render(request, 'portfolio/editar.html', context)

def apagar_comentario(request, comentario_id):
    Post.objects.get(id=comentario_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))




# CRIAÇÃO DE NOVA CADEIRA --
@login_required
def criar_cadeira(request):
    if request.method == 'POST':
        form = CadeiraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio:licenciatura')  # Redirecione para uma página de sucesso após a criação do post
    else:
        form = CadeiraForm()
    return render(request, 'portfolio/criarcadeira.html', {'form': form})
