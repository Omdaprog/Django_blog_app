from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.post_list, name ='post_list'),

    path('post<int:pk>/', views.post_detail, name='post_detail'),

    path('post/new/', views.post_new, name='post_new'),

    path('post/edit<int:pk>/', views.post_Edit, name='post_edit'),

    path('post/draft/', views.post_draft_list, name='post_draft_list' ),

    path('post/publish<int:pk>/',views.post_publish, name='post_publish'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name="login"),
]