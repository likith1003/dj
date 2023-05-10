from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.login,name='login'),
    path('freshregister',views.freshregister,name='freshregister'),
    path('expregister',views.expregister,name='expregister'),
    path('pydev',views.pydev,name='pydev'),
    path('django',views.django,name='django'),
    path('mt',views.mt,name='mt'),
    path('at',views.at,name='at'),
    path('web',views.web,name='web'),
    path('sql',views.sql,name='sql'),
    path('apti',views.apti,name='apti'),
    path('verbal',views.verbal,name='verbal')

]