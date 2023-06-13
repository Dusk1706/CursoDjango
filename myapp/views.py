from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Task
from .forms import CreateTask
# Create your views here.
def index(request):
    title="Creando cosas"
    return render(request,'index.html',{
        'title':title
    })

def hello(request,user):
    return HttpResponse("Hello %s!" % user)

def about(request):
    return render(request, 'about.html')

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request,"projects.html",{
        'projects':projects
    })

def tasks(request):
    # task = Task.objects.get(id=id)
    tasks=Task.objects.all()
    return render(request, 'tasks.html',{
        'tasks':tasks
    })
    
def create_task(request):
    if request.method == 'GET':
        return render(request,'create_task.html',{
            'form': CreateTask()
        })
    else:
        Task.objects.create(title=request.POST['title'],
        descripcion = request.POST['descripcion'], project_id=1)
        return redirect('/tasks/')
    
