from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
class ListTodo(generics.ListApiView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer