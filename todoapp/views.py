from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    return HttpResponse('Hello Azure')

# ToDoの一覧表示機能
class TodoListView(generic.ListView):
    model = Task
    paginate_by = 5

# ToDoの詳細表示機能
class TodoDetailView(generic.DetailView):
    model = Task

# ToDoの作成機能
class TodoCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('todo:list')

# ToDoの編集機能
class TodoUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('todo:list')

# ToDoの削除機能
class TodoDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('todo:list')

