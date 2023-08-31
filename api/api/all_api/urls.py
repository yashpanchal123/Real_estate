from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # main page
    path('agent-list/', views.Agent_lists.as_view()),  # you will get all the data    available.
    path('agent-list/<int:pk>/', views.RUD.as_view()),  # you can add the id after agent-list/pk = id number ,and find the specific data.
    path('create-superuser/', views.CreateSuperuserView.as_view(), name='create-superuser') # to create new user by entering username, password and email in body.
]

