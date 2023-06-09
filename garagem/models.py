from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)

def __str__(self):
    return self.nome.upper()

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

def __str__(self):
    return self.descricao

class Cor(models.Model):
    descricao = models.CharField(max_length=100)

def __str__(self):
    return self.descricao

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cor  = models.ForeignKey(Cor, on_delete=models.CASCADE)
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)

def __str__(self):
    return f"{self.marca.nome} {self.modelo.nome} {self.ano} {self.cor.nome}"



