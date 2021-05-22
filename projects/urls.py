from django.urls import path
from django.urls.conf import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'projects'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('new-project/', views.newProject, name='new-project'),
    path('new-task/', views.newTask, name='new-task'),
    path('task/', views.task, name='task'),
    path('search/', views.search,name='search'),
    path('project/<int:project_id>/delete', views.delete_project, name = 'delete_project'),
    path('project/<int:project_id>/edit', views.edit_project, name = 'edit_project'),
    path('task/<int:task_id>/delete', views.delete_task, name = 'delete_task'),
    path('task/<int:task_id>/edit', views.edit_task, name = 'edit_task'),
    path('value/<int:project_id>', views.formset_view, name='formset_view'),
    path('task/<int:task_id>', views.form_view, name='form_view'),
]