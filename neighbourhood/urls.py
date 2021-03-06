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
    url('search/', views.search, name='search'),
    url('my_businesses/(\d+)/', views.user_business, name='user_business'),
    url('create-post/', views.create_post, name='post'),
    url('all-posts/', views.postList, name='all_posts'),
    url('join-hood/(\d+)/', views.join_hood, name='join'),
    # url('leave-hood/(\d+)/', views.leave_hood, name='leave'),
    url('create-hood/(\d+)/', views.create_hood, name='create'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)