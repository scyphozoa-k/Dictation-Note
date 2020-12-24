from django.urls import path

from . import views

app_name = 'cms'
urlpatterns = [
    path('', views.TopView.as_view(), name='top'), 
    path('login/', views.Login.as_view(), name='login'), 
    path('logout/', views.Logout.as_view(), name='logout'), 
    path('signup/', views.UserCreate.as_view(), name='signup'),
    # ホーム画面関係 
    path('home/', views.Home.as_view(), name='home'), 
    path('questions/', views.QuestionList.as_view(), name='question_list'), 
    path('questions/<int:pk>/', views.QuestionDetail.as_view(), name='question_detail'), 
    path('home/user_detail/<int:pk>/update', views.UserUpdate.as_view(), name='user_update'), 
    path('home/user_detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('home/user_detail/<int:pk>/delete/', views.UserDelete.as_view(), name='user_delete'),
    path('users/', views.UserList.as_view(), name='user_list'), 
]
