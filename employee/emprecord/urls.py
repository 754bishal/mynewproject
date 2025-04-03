from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    
    # Employee URLs
    path('employees/', views.EmployeeListView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('employees/new/', views.EmployeeCreateView.as_view(), name='employee-create'),
    path('employees/<int:pk>/edit/', views.EmployeeUpdateView.as_view(), name='employee-update'),
    path('employees/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee-delete'),
    
    # Factory URLs
    path('factories/', views.FactoryListView.as_view(), name='factory-list'),
    path('factories/<int:pk>/', views.FactoryDetailView.as_view(), name='factory-detail'),
    path('factories/new/', views.FactoryCreateView.as_view(), name='factory-create'),
    path('factories/<int:pk>/edit/', views.FactoryUpdateView.as_view(), name='factory-update'),
    path('factories/<int:pk>/delete/', views.FactoryDeleteView.as_view(), name='factory-delete'),
    
    # Stream URLs
    path('streams/', views.StreamListView.as_view(), name='stream-list'),
    path('streams/new/', views.StreamCreateView.as_view(), name='stream-create'),
    path('streams/<int:pk>/edit/', views.StreamUpdateView.as_view(), name='stream-update'),
    path('streams/<int:pk>/delete/', views.StreamDeleteView.as_view(), name='stream-delete'),
]
