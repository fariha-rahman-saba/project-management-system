from django.urls import path
from . import views
from .views import  ProjectDetail, AddProject, Delete, LikeView


urlpatterns = [
    path('project/<int:pk>', ProjectDetail.as_view(), name='project-detail'),
    path('add-project', AddProject.as_view(), name='add-project'),
    # path('project/<int:pk>/remove', Delete.as_view(), name='delete-project'),
    # path('like/<int:pk>', views.LikeView, name='like-project'),
    path('about', views.about, name='about'),
    path('myprojects', views.home, name='my-projects'),

]
