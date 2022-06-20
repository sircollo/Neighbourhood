from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *

urlpatterns = [
    url('$',views.index, name='index'),
    url('signup/', views.signup, name='register'),
    url('signin/', views.signin, name='signin'),
    url('logout/', SignOutView.as_view(), name='logout'),
    url('^profile/(\d+)', views.profile, name='profile'),
    url('^post_business/(\d+)/', views.businesspost, name='post_a_business'),
    url('^businesses/', views.business, name='business'),
    url('^neighbourhoods/', views.neighbourhoods, name='neighbourhood'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)