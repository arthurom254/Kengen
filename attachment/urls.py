from django.urls import path
from . import views
urlpatterns=[
    path('', views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('signup',views.signup, name='signup'),
    path('my',views.index, name='index'),
    path('logs',views.logs, name='logs'),
    path('view/<str:id>', views.studentlog, name='studenylogs'),
    ]
