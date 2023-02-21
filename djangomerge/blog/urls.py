from django.urls import path
from . import views
#from django.conf import settings
#from django.conf.urls.static import static
app_name="blog"

urlpatterns = [
    path('signup/', views.signup_request, name='signup'),
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('profile/',views.profile_request, name='users-profile'),
    path('profile/edit/',views.profile_edit, name='profile-edit'),
    path('tag/<slug:slug>', views.tag, name='tag'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('signup/login/',views.login_request,name='login2'),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
    
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('comment/', views.post_detail, name= 'comment'),
 ]
