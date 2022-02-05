
from django.urls import re_path
from .import views

urlpatterns = [
    re_path(r'^index$', views.index, name='index'),
    re_path(r'^$', views.profiledash,name='profiledash'),
    re_path(r'^Training$', views.Training,name='Training'),
    re_path(r'^trainingteam1$', views.trainingteam1,name='trainingteam1'),
    re_path(r'^trainerstable$', views.trainerstable,name='trainerstable'),
    re_path(r'^topictable$', views.topictable,name='topictable'),
    re_path(r'^completedtasktable$', views.completedtasktable,name='completedtasktable'),
    re_path(r'^trainingprofile$', views.trainingprofile,name='trainingprofile'),
    
]
