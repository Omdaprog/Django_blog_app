from django.urls import path 
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.post_list, name ='post_list'),

    path("logout/", LogoutView.as_view(), name="logout_view"),

    path('post<int:pk>/', views.post_detail, name='post_detail'),

    path('post/new/', views.post_new, name='post_new'),

    path('post/edit<int:pk>/', views.post_Edit, name='post_edit'),

    path('post/draft/', views.post_draft_list, name='post_draft_list' ),

    path('post/publish<int:pk>/',views.post_publish, name='post_publish'),

    path('comment/<int:pk>/remove/',views.remove_comment, name="delete"),

    path('comment/<int:pk>/approve/',views.comment_approve, name="approve_comment"),

    path('post/<int:pk>/remove', views.remove_post, name="delete_post"),

    path('signup/', views.signup, name="signup"),
]