
from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_users,name = "show_user"),
    path('users', views.users_form,name ="user_form"),
    path('roles/',views.roles_form,name = "roles_form"),
    path('rights/',views.rights_form,name = "rights_form"),

]