from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name="index"),
    path('loadreg',views.loadReg,name="loadreg"),
    path('loadlogin',views.loadLogin, name="loadlogin"),
    path('register',views.register),
    path('userlogin',views.userlogin),
    path('userlogout', views.UserLogout,name='userlogout')

]