from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('users/', include('django.contrib.auth.urls')),  # sistemas de autenticación de django
]

# agregamos acciones de usuarios (login,logout)
from django.contrib.auth import views as auth_views

urlpatterns += [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name='users/reset_pass.html'), 
         name='reset_password'),    
]

# agregamos acciones propias
from . import views

urlpatterns += [
    # homapage
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
]
