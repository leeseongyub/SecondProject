from django.conf.urls import url, include
from django.contrib.auth import views

urlpatterns = [
    
    url(r'^login/$', views.LoginView.as_view(), name='login'),
]
