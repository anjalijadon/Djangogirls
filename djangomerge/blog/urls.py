from django.urls import path
from . import views
#from django.conf import settings
#from django.conf.urls.static import static
app_name="blog"

urlpatterns = [
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
    path('tag/<slug:slug>', views.tag, name='tag'),
    path('profile/edit/',views.profile_edit, name='profile-edit'),
    path('signup/login/',views.login_request,name='login2'),
    path('post/new/', views.post_new, name='post_new'),
    path('signup/', views.signup_request, name='signup'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('profile/',views.profile_request, name='users-profile'),
    path('comment/', views.post_detail, name= 'comment'),
    path('', views.post_list, name='post_list'),
 ]
