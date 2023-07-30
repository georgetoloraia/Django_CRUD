from django.shortcuts import render

from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer
from django.http import Http404, HttpResponse, HttpResponseRedirect


# class TodoList(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

# class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer



# class TodoCreate(APIView):
#     def post(self, request):
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class TodoList(APIView):
#     def get(self, request):
#         todos = Todo.objects.all()
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data)

# class TodoDetail(APIView):
#     def get_object(self, id):
#         try:
#             return Todo.objects.get(id=id)
#         except Todo.DoesNotExist:
#             raise Http404

#     def get(self, request, id):
#         todo = self.get_object(id)
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data)




# class TodoUpdate(APIView):
#     def get_object(self, id):
#         try:
#             return Todo.objects.get(id=id)
#         except Todo.DoesNotExist:
#             raise Http404

#     def put(self, request, id):
#         todo = self.get_object(id)
#         serializer = TodoSerializer(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class TodoUpdate(APIView):
#     def get_object(self, id):
#         try:
#             return Todo.objects.get(id=id)
#         except Todo.DoesNotExist:
#             raise Http404

#     def put(self, request, id):
#         todo = self.get_object(id)
#         serializer = TodoSerializer(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# class TodoDelete(APIView):
#     def get_object(self, id):
#         try:
#             return Todo.objects.get(id=id)
#         except Todo.DoesNotExist:
#             raise Http404

#     def delete(self, request, id):
#         todo = self.get_object(id)
#         todo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    # Add your logic here to fetch all todos from the database
    todos = []  # Placeholder for demonstration

    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)




# html todo functions

def get_all_todos(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'get_all_todos.html', context)

def get_todo(request):
    if request.method == "POST":
        id_from_site = request.POST["get_todo_id"]
        todos = Todo.objects.get(id=id_from_site)
        print(todos)
        context = {
            'id': todos.id,
            'title': todos.title,
            'description': todos.description

        }
        print(context)
        return render(request, 'get_todo.html', context)

    
    # try:
    #     todo = Todo.objects.get(id=id)
    # except Todo.DoesNotExist:
    #     todo = None
    # context = {
    #     'todo': todo
    # }
    # print(context)
    # return render(request, 'get_todo.html', context)

def create_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        # Create the Todo object with the received data
        todo = Todo.objects.create(title=title, description=description)
        return HttpResponseRedirect('/todos/get_all_todos/')  # Redirect to the list of todos
    return render(request, 'create_todo.html')

def update_todo(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        todo = None
    
    if request.method == 'POST':
        if todo:
            todo.title = request.POST['title']
            todo.description = request.POST['description']
            # Update the Todo object with the received data
            todo.save()
        return HttpResponseRedirect('/api/todos/')  # Redirect to the list of todos
    
    context = {
        'todo': todo
    }
    return render(request, 'update_todo.html', context)

def delete_todo(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        todo = None
    
    if request.method == 'POST' and todo:
        todo.delete()
        return HttpResponseRedirect('todos')  # Redirect to the list of todos
    
    context = {
        'todo': todo
    }
    return render(request, 'delete_todo.html', context)



