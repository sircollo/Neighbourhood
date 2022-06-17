from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url('$',views.index, name='index'),
    url('signup/', views.signup, name='register'),
    url('signin/', views.signin, name='signin'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)