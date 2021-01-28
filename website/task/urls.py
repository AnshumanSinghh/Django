from django.urls import path
from . import views

app_name = "task"
urlpatterns = [
            path('', views.index, name="index"),   
            path('add/', views.add, name="add"),   
]

# sometimes name  collision may occur and we will be redirected to another url as we are using name of path 
# instead of url itself, actually it occurs when we have same path names in different apps of a same project
# so to fix it we will add app_name = "whatever the app name is". This just helps uniquely identfying all of the
# URLs. And one more thing to do is goto and replace the path name with 'app_name: path_name'. That's it now 
# Django will uniquely identify all of the URLs now.