from django.urls import path
from . import views

urlpatterns = [
	path('', views.ApiOverview, name='home'),
    path('create/', views.add_employee, name='add_employee'),
    path('all/', views.view_employee, name='view_employee'),
    path('update/<int:pk>/', views.update_employee, name='update-employee'),
    path('delete/<int:pk>/', views.delete_employee, name='delete-employee'),
]
