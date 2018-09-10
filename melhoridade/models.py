from django.db import models
from django.utils import timezone

# Create your models here.

class Loja(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nome_loja = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200, blank = True, null = True)
    observacao = models.TextField('Observação', blank = True, null = True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome_loja

class Funcionario(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nome_funcionario = models.CharField(max_length=200)
    cpf = models.CharField(max_length=12, blank = True, null = False)
    endereco = models.CharField(max_length=200, blank = True, null = True)
    telefone = models.CharField(max_length=12, blank = True, null = True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome_funcionario


class Cliente(models.Model):
    author = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    nome_cliente = models.CharField(max_length=200)
    cpf = models.CharField(max_length=12, blank = True, null = False)
    endereco = models.CharField(max_length=200, blank = True, null = True)
    observacao = models.TextField('Observação', blank = True, null = True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome_cliente

class Banco(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nome_banco = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome_banco

class Promotora(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nome_promotora = models.CharField(max_length=200)

    banco = models.ForeignKey(Banco, on_delete = models.CASCADE, blank = True, null = False)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome_promotora

class Prazo(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    parcelas_choice = (
            ("36", "36 Vezes"),
            ("48", "48 Vezes"),
            ("72", "72 Vezes"),
    )
    parcelas = models.CharField(max_length = 8, choices = parcelas_choice, default = "36")
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.parcelas


class Produto(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    banco = models.ForeignKey(Banco, on_delete = models.CASCADE, blank = True, null = False)
    nome_produto = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome_produto

class Orgao(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nome_orgao = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome_orgao

class Contrato(models.Model):
    author = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null = False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null = False)
    id = models.CharField(max_length=14, unique=True, primary_key=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor = models.FloatField()
    parcelas = models.ForeignKey(Prazo, on_delete=models.CASCADE)
    promotora = models.ForeignKey(Promotora, on_delete=models.CASCADE)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    detalhes = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome_orgao
