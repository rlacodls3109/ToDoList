from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer
from .models import Todo

# Create your views here.

@api_view(["GET"])
def todolist(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def todocreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["DELETE"])
def tododelete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return Response("Delete Success")

@api_view(["PUT"])
def todoupdate(request,pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


