from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tarefa_app.models import Usuario, Tarefa
from tarefa_app.serializers import UsuarioSerializer, TarefaSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def usuario_list(request):
    # GET list of usuarios, POST a new usuario, DELETE all usuarios
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        
        nome = request.GET.get('nome', None)
        if nome is not None:
            usuarios = usuarios.filter(nome__icontains=nome)
    
        usuarios_serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(usuarios_serializer.data, safe=False)
    elif request.method == 'POST':
        usuario_data = JSONParser().parse(request)
        usuario_serializer = UsuarioSerializer(data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse(usuario_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Usuario.objects.all().delete()
        return JsonResponse({'message': '{} Todos os usuários foram deletados!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def usuario_detail(request, pk):
    # find usuario by pk (id)
    try: 
        usuario = Usuario.objects.get(pk=pk) 
    except Usuario.DoesNotExist: 
        return JsonResponse({'message': 'O usuario não existe'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET': 
        usuario_serializer = UsuarioSerializer(usuario) 
        return JsonResponse(usuario_serializer.data)
    elif request.method == 'PUT': 
        usuario_data = JSONParser().parse(request) 
        usuario_serializer = UsuarioSerializer(usuario, data=usuario_data) 
        if usuario_serializer.is_valid(): 
            usuario_serializer.save() 
            # return JsonResponse(usuario_serializer.data) 
            return JsonResponse({'message': 'Usuario foi atualizado!'}, status=status.HTTP_200_OK) 
        return JsonResponse(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': 
        usuario.delete() 
        return JsonResponse({'message': 'Usuario foi deletado!'}, status=status.HTTP_204_NO_CONTENT)

        
@api_view(['GET', 'POST', 'DELETE'])
def tarefa_list(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id', None)
        tarefas = Tarefa.objects.filter(usuario__id=user_id)
        tarefas_serializer = TarefaSerializer(tarefas, many=True)
        return JsonResponse(tarefas_serializer.data, safe=False)
    elif request.method == 'POST':
        tarefa_data = JSONParser().parse(request)
        tarefa_serializer = TarefaSerializer(data=tarefa_data)
        if tarefa_serializer.is_valid():
            tarefa_serializer.save()
            return JsonResponse(tarefa_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tarefa_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def tarefa_detail(request, pk):
    # find tarefa by pk (id)
    try: 
        tarefa = Tarefa.objects.get(pk=pk) 
    except Tarefa.DoesNotExist: 
        return JsonResponse({'message': 'O tarefa não existe'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET': 
        tarefa_serializer = TarefaSerializer(tarefa) 
        return JsonResponse(tarefa_serializer.data)
    elif request.method == 'PUT': 
        tarefa_data = JSONParser().parse(request) 
        tarefa_serializer = TarefaSerializer(tarefa, data=tarefa_data) 
        if tarefa_serializer.is_valid(): 
            tarefa_serializer.save() 
            # return JsonResponse(tarefa_serializer.data) 
            return JsonResponse({'message': 'Tarefa foi atualizada!'}, status=status.HTTP_200_OK) 
        return JsonResponse(tarefa_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': 
        tarefa.delete() 
        return JsonResponse({'message': 'Tarefa foi deletada!'}, status=status.HTTP_204_NO_CONTENT)