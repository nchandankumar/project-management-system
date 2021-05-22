from django.http.request import HttpRequest
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.db.models import Q
from django.forms import formset_factory
from projects.forms import ValueForm
from register.models import Project
from projects.models import Task
from projects.forms import TaskRegistrationForm
from projects.forms import ProjectRegistrationForm
from projects.forms import ProjectForm
from projects.forms import TaskForm

# Create your views here.
@login_required
def projects(request):
    projects = Project.objects.all()
    avg_projects = Project.objects.all().aggregate(Avg('complete_per'))['complete_per__avg']
    tasks = Task.objects.all()
    overdue_tasks = tasks.filter(due='2')
    context = {
        'avg_projects' : avg_projects,
        'projects' : projects,
        'tasks' : tasks,
        'overdue_tasks' : overdue_tasks,
    }
    return render(request, 'projects/projects.html', context)
@login_required
def newTask(request):
    if request.method == 'POST':
        form = TaskRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'projects/new_task.html', context)
        else:
            return render(request, 'projects/new_task.html', context)
    else:
        form = TaskRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'projects/new_task.html', context)
@login_required
def task(request):
    projects = Project.objects.all()
    avg_projects = Project.objects.all().aggregate(Avg('complete_per'))['complete_per__avg']
    tasks = Task.objects.all()
    overdue_tasks = tasks.filter(due='2')
    context = {
        'avg_projects' : avg_projects,
        'projects' : projects,
        'tasks' : tasks,
        'overdue_tasks' : overdue_tasks,
    }
    return render(request, 'projects/task.html', context)
@login_required
def newProject(request):
    if request.method == 'POST':
        form = ProjectRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            form = ProjectRegistrationForm()
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'projects/new_project.html', context)
        else:
            return render(request, 'projects/new_project.html', context)
    else:
        form = ProjectRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'projects/new_project.html', context)
@login_required
def search(request):
    projects = Project.objects.all()
    avg_projects = Project.objects.all().aggregate(Avg('complete_per'))['complete_per__avg']
    query =None
    results =[]
    if request.method == 'GET':
        query=request.GET.get('search')
        results=Project.objects.filter(Q(name__icontains=query)| Q(description__icontains=query))
    context = {
            'query':query,
            'results':results,
            'avg_projects' : avg_projects,
            'projects' : projects,
    }
    return render(request,'projects/search.html',context)
@login_required
def delete_project(request, project_id):
    project = Project.objects.filter(pk = project_id)
    if project:
        project = Project.objects.get(pk = project_id)
        project.delete()
    return redirect('projects:projects')
@login_required
def edit_project(request, project_id):
    project = get_object_or_404(Project, pk = project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance = project)
        if form.is_valid():
            project = form.save(commit = False)
            project.save()
            return redirect('projects:projects')
    else:
        form = ProjectForm(instance = project)

    return render(request, template_name = 'projects/edit_project.html', context = { 'form': form })
@login_required
def delete_task(request, task_id):
    task = Task.objects.filter(pk = task_id)
    if task:
        task = Task.objects.get(pk = task_id)
        task.delete()
    return redirect('projects:task')
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk = task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            task = form.save(commit = False)
            task.save()
            return redirect('projects:task')
    else:
        form = TaskForm(instance = task)

    return render(request, template_name = 'projects/edit_task.html', context = { 'form': form })

def formset_view(request,project_id):
    project = Project.objects.filter(id=project_id).first()
    assi = project.assign.all()
    FormSet = formset_factory(ValueForm, extra = assi.count())
    formset = FormSet(request.POST or None)
    values = []
    keys = []
    ans=0
    if formset.is_valid():
        sum=0
        for form in formset:
            values.append(100/form.cleaned_data['No_of_days'])
            sum=sum+100/form.cleaned_data['No_of_days']
        ans=round(100/sum)
    for i in range(assi.count()):
        keys.append(i+1)
    d=dict(zip(keys,values))
    context={
    'formset':formset,
    'ans':ans,
    'd':d,
    }
    return render(request, "projects/value.html", context)

def form_view(request,task_id):
    task = Task.objects.filter(id=task_id).first()
    assi = task.assign.all()
    FormSet = formset_factory(ValueForm, extra = assi.count())
    formset = FormSet(request.POST or None)
    ans=0
    if formset.is_valid():
        sum=0
        for form in formset:
            sum=sum+100/form.cleaned_data['value']
        ans=100/sum
    context={
        'formset':formset,
        'ans':ans,
        }
    return render(request, "projects/value.html", context)