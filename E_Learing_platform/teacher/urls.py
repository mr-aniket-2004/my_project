from django.contrib import admin
from django.urls import path
from teacher import views
# from home import views


urlpatterns = [
   path("/teacher",views.index1,name='teacherdashboard'),
   path("/assignment",views.assignment,name='teacherassignment'),
   path("/chat",views.chat,name='teacherchat'),
   path("/profile",views.profile,name='teacherprofile'),
   
#    path("log",views.student_logout,name='log'),
]