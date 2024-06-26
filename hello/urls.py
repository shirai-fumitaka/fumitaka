from django.urls import path, re_path
from . import views
from .views import HelloView
from .views import FriendList
from .views import FriendDetail

urlpatterns = [
    # path('', views.index, name='index'),
    # path('next', views.next, name='next'),
    # path('form', views.form, name='form'),
    # re_path(r'^$', HelloView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('<int:num>', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'), 
    path('delete/<int:num>', views.delete, name='delete'),
    path('list',FriendList.as_view()),
    path('detail/<int:pk>',FriendDetail.as_view()),
    path('find',views.find,name='find'),
    path('check',views.check,name='check'),
    path('message/',views.message,name='message'),
    path('message/<int:page>',views.message,name='message'),
]