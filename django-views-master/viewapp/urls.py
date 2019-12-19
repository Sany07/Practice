from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClassView.as_view(), name='home'),
    path('func/', views.FunctionViews, name='func')
]