from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views 
from django.contrib.auth import views as auth_views


app_name='users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('profile/', user_views.profile, name="profile"),
]