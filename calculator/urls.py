from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'calculator'

urlpatterns = [
    path('cost/', views.Cost, name='cost'),
    path('Addtech/<int:tech_id>',views.Addtech,name='Addtech'),
    path('Done/',views.Done,name='Done'),
]