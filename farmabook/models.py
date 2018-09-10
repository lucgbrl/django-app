from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Book(models.Model):
    #author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    obs = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    devolution_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.devolution_date = datetime.now()+timedelta(days=30)
        self.save()

    def __str__(self):
        return self.title


class Card(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Aluno(models.Model):
        author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
        name = models.CharField(max_length=200)
        email = models.CharField(max_length=200)
        phone = models.CharField(max_length=200)
        module = models.CharField(max_length=200)
        address = models.CharField(max_length = 200)
        created_date = models.DateTimeField(
                default = timezone.now)
        published_date = models.DateTimeField(
                blank = True, null = True)

        def publish(self):
                self.published_date = timezone.now()
                self.save
                
        def __str__(self):
                return self.name


class Empregado(models.Model):
        author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
        name = models.CharField(max_length=200)
        email = models.CharField(max_length=200)
        phone = models.CharField(max_length=20)
        address = models.CharField(max_length=200)
        occupation = models.CharField(max_length=100)
        created_date = models.DateTimeField(
                default=timezone.now)
        ṕublished_date = models.DateTimeField(
                blank = True, null = True)

        def __str__(self):
                return self.name


'''
class Loja(models.Model):
        nome = models.CharField(max_length=200, blank = True)
        endereco = models.TextField(blank= True)
        created_date = models.DateTimeField(
                default = timezone.now)
        published_date = models.DateTimeField(
                blank = True, null = True)
        def publish(self):
                self.published_date = timezone.now()
                self.save()
        def __str__(self):
                return self.nome

class Orgao(models.Model):
        nome = models.CharField(max_length=200)
        created_date = models.DateTimeField(
                default = timezone.now)
        published_date = models.DateTimeField(
                blank = True, null = True
        )
        def publish(self):
                self.published_date = timezone.now()
                self.save()
        def __str__(self):
                return self.nome

# class
class Produto(models.Model):
        nome = models.CharField(max_length=200)
        def __str__(self):
                return self.nome

class Corretora(models.Model):
        nome = models.CharField(max_length=200)
        def __str__(self):
                return self.nome
class Cliente(models.Model):
        nome = models.CharField(max_length=200)
        cpf = models.IntegerField()
        telefone = models.CharField(max_length=12, blank = True)
        cidade = models.CharField(max_length=200, blank = True)

        def __str__(self):
                return self.nome

'''