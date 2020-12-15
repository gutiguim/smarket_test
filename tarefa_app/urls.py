from django.conf.urls import url 
from tarefa_app import views 
 
urlpatterns = [ 
    url(r'^api/usuarios$', views.usuario_list),
    url(r'^api/usuarios/(?P<pk>[0-9]+)$', views.usuario_detail),
    url(r'^api/tarefas$', views.tarefa_list),
    url(r'^api/tarefas/(?P<pk>[0-9]+)$', views.tarefa_detail)
]
