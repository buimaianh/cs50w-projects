from django.urls import path
from . import views

urlpatterns = [
    path('emails/', views.compose_new_email, name='compose_new_email'),
    path('emails/<str:mailbox>/', views.load_mailbox, name='load_mailbox'),
    path('emails/<int:email_id>/', views.email_detail, name='email_detail'),
    path('register/', views.register_new_account, name='register_new_account'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view')
]
