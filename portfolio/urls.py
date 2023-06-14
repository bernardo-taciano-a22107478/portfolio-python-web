"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

app_name='portfolio'

urlpatterns = [
    path('', views.home_view, name="home"),
    path('projetos/', views.projects_view, name="projetos"),
    path('tecnologias/', views.technologys_view, name="tecnologias"),
    path('laboratorios/', views.labs_view, name="laboratorios"),
    path('tecnologiasusadas/', views.usedtech_view, name="tecusada"),
    path('javascript/', views.javascript_view, name="javascript"),
    path('licenciatura/', views.university_view, name="licenciatura"),
    path('educacao/', views.education_view, name="educacao"),
    path('skills/', views.skills_view, name="skills"),
    path('hobbies/', views.hobbies_view, name="hobbies"),
    path('sobre/', views.aboutme_view, name="sobre"),
    path('blog', views.blog_view, name='blog'),
    path('contacto/', views.contact_view, name="contacto"),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('criar/', views.criar_post, name='criar'),
    path('editar/<int:comentario_id>', views.edita_comentario, name='editar'),
    path('apagar/<int:comentario_id>', views.apagar_comentario, name='apagar'),
    path('criarcadeira/', views.criar_cadeira, name='criarcadeira'),
    path('apagarcadeira/<int:cadeira_id>', views.apagar_cadeira, name='apagarcadeira'),
]
