from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
]

"""
# agrega autenticación (for login, logout, password management)
# utilizando el sistema propio de django 2.1 y los templates
# ubicados en templates/registration
urlpatterns += [
    path('profiles/', include('django.contrib.auth.urls')),
]

# The URLs provided by auth are:
# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']

"""

# agregamos nuestra
from django.contrib.auth import views as auth_views

urlpatterns += [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


from . import views

urlpatterns += [
    # homapage
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
]



