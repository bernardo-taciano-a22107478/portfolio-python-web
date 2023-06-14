from django.db import models

# Create your models here.

#CRIAÇÃO BASES DADOS


class Pessoa(models.Model):
   

    funcao = [
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
    ]
        
    nome = models.CharField(max_length=70)
    funcao = models.CharField(choices=funcao, blank=True, default='aluno', max_length=10)
    linkLusofona = models.URLField(max_length = 200, blank=True)
    linkLinkedin = models.URLField(max_length = 200, blank=True)

    def __str__(self):
        return self.nome


#Uma pessoa pode ter varios comentários
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey(Pessoa, on_delete = models.CASCADE, related_name = "autor")
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(max_length=1000)
    link = models.CharField(max_length=200, blank=True)
    imagem = models.ImageField(upload_to="static/portfolio/images", blank=True)

    def __str__(self):
        return self.titulo[:50]
    

class Tecnologia(models.Model):
    nome = models.CharField(max_length=30)
    ano = models.DateTimeField(auto_now_add=True)
    criador = models.CharField(max_length=40)
    logo = models.ImageField(upload_to="static/portfolio/images", blank=True)
    link = models.URLField(max_length = 200)
    descricao = models.TextField(max_length=1000)

    def __str__(self):
        return self.nome[:50]
    
class Projeto(models.Model):
    titulo = models.CharField(max_length=50)
    descricao =  models.TextField(max_length=2000)
    imagem = models.ImageField(upload_to="static/portfolio/images", blank=True)
    ano = models.IntegerField(default=2023)
    linkGithub = models.URLField(max_length=1000,  blank=True)
    linkYoutube = models.URLField(max_length=1000,  blank=True)
    participantes = models.ManyToManyField(Pessoa)
    tecnologias = models.ManyToManyField(Tecnologia)

    def __str__(self):
        return self.titulo[:50]
    


class Cadeira(models.Model):
    ano = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    ]

    semestre = [
        ('1', '1'),
        ('2', '2'),
    ]

    rank = [
        ('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),
    ]

    nome = models.CharField(max_length=40)
    anoLectivo = models.CharField(max_length=10,choices= ano, default=1)
    semestre = models.CharField(max_length=4,choices= semestre, default=1)
    ano = models.IntegerField(default=2021)
    ects = models.IntegerField()
    topicosAbordados = models.TextField(max_length=1000, blank=True)
    linguagens = models.ManyToManyField(Tecnologia, blank=True)
    ranking = models.CharField(max_length=2,choices= rank)
    docente_teorica = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    docentes_praticas = models.ManyToManyField(Pessoa, related_name='docentes')
    link = models.URLField(max_length = 200)
    projetos = models.ManyToManyField(Projeto, blank=True)

    def __str__(self):
        return self.nome[:50]
    

class Competencia(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=1000)
    projetos = models.ManyToManyField(Projeto)
    disciplinas = models.ManyToManyField(Cadeira)
    
    def __str__(self):
        return self.titulo[:50]

class Interesse(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=1000)
    imagem = models.ImageField(upload_to="static/portfolio/images", blank=True)
    link = models.URLField(max_length = 200, blank=True)

    def __str__(self):
        return self.titulo[:50]
    
class Laboratorio(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=1000)
    link = models.URLField(max_length = 200)

    def __str__(self):
        return self.titulo[:50]
    

class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    imagem = models.ImageField(upload_to="static/portfolio/images", blank=True)

    def __str__(self):
        return self.titulo[:50]
    

class Tfc(models.Model):
    autor = models.ManyToManyField(Pessoa, related_name = "autorTFC")
    orientadores = models.ManyToManyField(Pessoa, related_name='orientadores')
    ano = models.IntegerField(default=2023)
    titulo = models.CharField(max_length=50)
    resumo = models.CharField(max_length=1000)
    imagem = models.ImageField(upload_to="static/portfolio/images", blank=True)
    relatorio = models.URLField(max_length=1000)
    linkGithub = models.URLField(max_length=1000, blank=True)
    video = models.URLField(max_length=1000)

    def __str__(self):
        return self.titulo[:50]
    
