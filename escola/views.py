# from django.http import JsonResponse

# def estudantes(request):
#     if request.method == 'GET':
#         estudante = {
#             'id': '1',
#             'nome': 'Mariane'
#         }
#         return JsonResponse(estudante)

from escola.models import Estudante, Curso, Matricula
from escola.serializer import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaCursoEstudanteSerializer, ListaMatriculasEstudanteSerializer
from rest_framework import viewsets, generics
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated, IsAdminUser

class EstudanteViewSet(viewsets.ModelViewSet):

    # authentication_classes  = [BasicAuthentication]
    # permission_classes      = [IsAdminUser]

    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculaEstudante(generics.ListAPIView):

    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaCursoEstudante(generics.ListAPIView):

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaCursoEstudanteSerializer
   
