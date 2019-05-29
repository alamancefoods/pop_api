from django.urls import path
from api import views

urlpatterns = [
    path('item/', views.ItemList.as_view()),
    path('item/<int:pk>/', views.ItemDetail.as_view()),
    path('employee/', views.EmployeeList.as_view()),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view()),
    path('shift/', views.ShiftList.as_view()),
    path('shift/<int:pk>/', views.ShiftDetail.as_view()),
    path('line/', views.LineList.as_view()),
    path('line/<int:pk>/', views.LineDetail.as_view()),
    path('machine/', views.MachineList.as_view()),
    path('machine/<int:pk>/', views.MachineDetail.as_view()),
]
