from django.urls import re_path as url
from . import views
urlpatterns = [
    url('$',views.index, name='index'),
    url('signup/', views.signup, name='register'),
    url('signin/', views.signin, name='signin'),
]
