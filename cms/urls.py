from django.urls import path

from .views import *

app_name = 'cms'
urlpatterns = [
    path('', TopView.as_view(), name='top'), 
    path('login/', Login.as_view(), name='login'), 
    path('logout/', Logout.as_view(), name='logout'), 
    path('signup/', UserCreate.as_view(), name='signup'),
    # ホーム画面関係 
    path('home/', Home.as_view(), name='home'), 
    path('questions/', QuestionList.as_view(), name='question_list'), 
    path('questions/<int:pk>/', QuestionDetail.as_view(), name='question_detail'), 
    path('home/user_detail/<int:pk>/update', UserUpdate.as_view(), name='user_update'), 
    path('home/user_detail/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('home/user_detail/<int:pk>/delete/', UserDelete.as_view(), name='user_delete'),
    path('users/', UserList.as_view(), name='user_list'), 
]
