from django.contrib.auth import views as auth_views
from django.urls import path   # incluir include
from . import views

app_name = 'autenticacao'
urlpatterns = [
    path('registo/', views.registo_view, name='registo'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('reset_password/', views.forgot_password, name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='autenticacao/reset_done.html'), name='reset_password_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='autenticacao/reset_password_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='reset_password_complete'),
]