from django.db import models

'''
Dados necessários:

Id
Nome
E-mail
    Não pode estar em branco
CPF
    Máximo de 11 caracteres
Data de Nascimento
Número de Celular
    Máximo de 14 caracteres

'''

class Estudante(models.Model):
    nome            = models.CharField(max_length = 100)
    email           = models.EmailField(blank = False, max_length = 30)
    cpf             = models.CharField(max_length = 11)
    data_nascimento = models.DateField()
    celular         = models.CharField(max_length = 14)

    def __str__(self):
        return self.nome


'''
Dados necessários:
Id
Código
    Máximo de 10 caracteres
Descrição
    Não pode estar em Branco
Nível (Básico, Intermediário e Avançado)
    Não pode estar em Branco
    Não pode ser Nulo
    Por padrão deve ser Básico
'''

class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    codigo      = models.CharField(max_length = 10)
    descricao   = models.CharField(blank = False, max_length = 100)
    nivel       = models.CharField(choices = NIVEL, blank = False, max_length = 1, null = False, default = 'B')


    def __str__(self):
        return self.codigo
    

class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )
    estudante = models.ForeignKey(Estudante, on_delete = models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    periodo     = models.CharField(choices = PERIODO, blank = False, max_length = 1, null = False, default = 'M')
