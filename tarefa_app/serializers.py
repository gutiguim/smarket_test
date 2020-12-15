from rest_framework import serializers 
from tarefa_app.models import Usuario
from tarefa_app.models import Tarefa
 
 
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id',
                  'nome')

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ('id',
                  'descricao',
                  'estadoTarefa',
                  'usuario')
