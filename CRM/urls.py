from django.urls import path

from . import views
from .models import Task, Clients
from .serializers import TaskSerializer, ClientsSerializer
from .views import TaskList, ClientsList

urlpatterns = [
    path('task/', TaskList.as_view(queryset=Task.objects.all(), serializer_class=TaskSerializer),name='task-list'),
    path('task/<int:pk>/',views.TaskRetrieveUpdateDeleteView.as_view(queryset=Task.objects.all(), serializer_class=TaskSerializer),name='task-list'),
    path('task/?search=<query>', views.SearchTaskAPIView.as_view()),
    path('clients/', ClientsList.as_view(queryset=Clients.objects.all(), serializer_class=ClientsSerializer), name='clients-list'),
    path('clients/<int:pk>/', views.ClientsRetrieveUpdateDeleteView.as_view(queryset=Clients.objects.all(), serializer_class=ClientsSerializer), name='clients-list')
]
