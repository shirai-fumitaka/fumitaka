from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:page>', views.index, name='index'),
    path('add', views.add, name='add'),
    path('creategroup', views.create, name='creategroup'),
    path('groups', views.groups, name='groups'),
    path('post', views.post, name='post'),
    path('good/<int:good_id>', views.good, name='good'),
    path('share/<int:share_id>', views.share, name='share'),
]
