from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('dias/', views.dias_view, name='dias'),
    path('palcos/', views.palcos_view, name='palcos'),
    path('dia/<int:dia_id>/', views.dia_view, name='dia'),
    path('palco/<int:palco_id>/', views.palco_view, name='palco'),
    path('concerto/<int:concerto_id>/', views.concerto_view, name='concerto'),
]